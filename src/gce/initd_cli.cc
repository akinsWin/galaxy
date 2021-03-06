// Copyright (c) 2015, Baidu.com, Inc. All Rights Reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/select.h>
#include <sys/ioctl.h>
#include <termios.h>
#include <signal.h>

#include "gflags/gflags.h"
#include "proto/agent.pb.h"
#include "proto/initd.pb.h"
#include "rpc/rpc_client.h"
#include "tprinter.h"
#include "string_util.h"

DEFINE_string(initd_endpoint, "", "initd endpoint");
DEFINE_string(user, "galaxy", "use user");
DEFINE_string(chroot, "", "chroot path");
DEFINE_string(LINES, "39", "env values");
DEFINE_string(COLUMNS, "139", "env values");
DEFINE_string(TERM, "xterm-256color", "env values");
DECLARE_string(agent_port);
DECLARE_string(agent_default_user);
DECLARE_string(flagfile);
DEFINE_string(pod_id, "", "pod id");

const std::string SInitdCliUsage = "initd client.\n"
                                   "Usage: \n"
                                   "     ./initd_cli ps --flagfile=galaxy.flag\n"
                                   "     ./initd_cli attach --pod_id=<podid> --user=galaxy --flagfile=galaxy.flag\n";

bool TerminateContact(int fdm) {
    if (fdm < 0) {
        return false; 
    }
    struct termios temp_termios;
    struct termios orig_termios;

    ::signal(SIGINT, SIG_IGN);
    ::signal(SIGTERM, SIG_IGN);
    ::tcgetattr(0, &orig_termios);
    temp_termios = orig_termios;
    // 去掉输入同步的输出, 以及不等待换行符
    temp_termios.c_lflag &= ~(ICANON | ECHO | ECHOE | ECHOK | ECHONL | ECHOPRT | ECHOKE | ICRNL);
    temp_termios.c_cc[VTIME] = 1;   // 终端等待延迟时间（十分之一秒为单位）
    temp_termios.c_cc[VMIN] = 1;    // 终端接收字符数
    ::tcsetattr(0, TCSANOW, &temp_termios);

    const int INPUT_BUFFER_LEN = 1024 * 10;
    char input[INPUT_BUFFER_LEN];
    fd_set fd_in; 
    int ret = 0;
    while (1) {
        FD_ZERO(&fd_in); 
        FD_SET(0, &fd_in);
        FD_SET(fdm, &fd_in);
        ret = ::select(fdm + 1, &fd_in, NULL, NULL, NULL);
        switch (ret) {
            case -1 :  
                fprintf(stderr, "select err[%d: %s]\n", 
                        errno, strerror(errno));
                break;
            default : {
                if (FD_ISSET(0, &fd_in))  {
                    ret = ::read(0, input, sizeof(input)); 
                    if (ret > 0) {
                        ::write(fdm, input, ret); 
                    } else {
                        if (ret < 0) {
                            fprintf(stderr, "read err[%d: %s]\n",
                                    errno,
                                    strerror(errno)); 
                            break;
                        }
                    }
                }         
                if (FD_ISSET(fdm, &fd_in)) {
                    ret = ::read(fdm, input, sizeof(input)); 
                    if (ret > 0) {
                        ::write(1, input, ret);
                    } else {
                        if (ret < 0) {
                            fprintf(stderr, "read err[%d: %s]\n",
                                    errno,
                                    strerror(errno)); 
                            break;
                        } 
                    }
                }
            }
        }
        if (ret < 0) {
            break; 
        }
    }

    ::tcsetattr(0, TCSANOW, &orig_termios);
    if (ret < 0) {
        return false; 
    }
    return true;
} 

bool PreparePty(int* fdm, std::string* pty_file) {
    if (pty_file == NULL || fdm == NULL) {
        return false; 
    }
    *fdm = -1;
    *fdm = ::posix_openpt(O_RDWR);
    if (*fdm < 0) {
        fprintf(stderr, "posix_openpt err[%d: %s]",
                errno, strerror(errno)); 
        return false;
    }

    int ret = ::grantpt(*fdm);
    if (ret != 0) {
        fprintf(stderr, "grantpt err[%d: %s]", 
                errno, strerror(errno)); 
        ::close(*fdm);
        return false;
    }

    ret = ::unlockpt(*fdm);
    if (ret != 0) {
        fprintf(stderr, "unlockpt err[%d: %s]", 
                errno, strerror(errno));
        ::close(*fdm);
        return false;
    }
    pty_file->clear();
    pty_file->append(::ptsname(*fdm));
    return true;
}

void ListPods() {
    ::baidu::galaxy::Agent_Stub* agent;        
    ::baidu::galaxy::RpcClient* rpc_client = 
        new ::baidu::galaxy::RpcClient();

    std::string endpoint("127.0.0.1:");
    endpoint.append(FLAGS_agent_port); 
    rpc_client->GetStub(endpoint, &agent);
    
    ::baidu::galaxy::ShowPodsRequest request;
    ::baidu::galaxy::ShowPodsResponse response;
    bool ret = rpc_client->SendRequest(agent,
            &::baidu::galaxy::Agent_Stub::ShowPods,
            &request,
            &response, 5, 1); 
    if (!ret) {
        fprintf(stderr, "rpc failed\n"); 
        return;
    } else if (response.has_status() 
                && response.status() != ::baidu::galaxy::kOk) {
        fprintf(stderr, "response status %s\n", 
                ::baidu::galaxy::Status_Name(response.status()).c_str()); 
        return;
    }

    ::baidu::common::TPrinter tp(7);
    tp.AddRow(7, "", "podid", "jobid", "job name", "state", "cpu usage", "mem usage");
    for (int i = 0; i < response.pods_size(); ++i) {
        const ::baidu::galaxy::PodPropertiy& pod = response.pods(i);
        std::vector<std::string> vs;
        vs.push_back(::baidu::common::NumToString(i + 1));
        vs.push_back(pod.pod_id());
        vs.push_back(pod.job_id());
        vs.push_back(pod.job_name());
        vs.push_back(::baidu::galaxy::PodState_Name(
                    pod.pod_status().state()));
        vs.push_back(::baidu::common::NumToString(
                    pod.pod_status().resource_used().millicores()));
        vs.push_back(::baidu::common::NumToString(
                    pod.pod_status().resource_used().memory()));
        //vs.push_back(pod.initd_endpoint());
        tp.AddRow(vs);
    }
    fprintf(stdout, "%s\n", tp.ToString().c_str());
    return;
}

void AttachPod() {
    ::baidu::galaxy::Agent_Stub* agent;    
    ::baidu::galaxy::RpcClient* rpc_client = 
        new ::baidu::galaxy::RpcClient();
    std::string endpoint("127.0.0.1:");
    endpoint.append(FLAGS_agent_port);
    rpc_client->GetStub(endpoint, &agent);

    ::baidu::galaxy::ShowPodsRequest request;
    ::baidu::galaxy::ShowPodsResponse response;
    request.set_podid(FLAGS_pod_id);
    bool ret = rpc_client->SendRequest(agent,
            &::baidu::galaxy::Agent_Stub::ShowPods,
            &request,
            &response, 5, 1);
    if (!ret) {
        fprintf(stderr, "rpc failed\n");  
        return;
    } else if (response.has_status()
            && response.status() != ::baidu::galaxy::kOk) {
        fprintf(stderr, "response status %s\n",
                ::baidu::galaxy::Status_Name(response.status()).c_str()); 
        return;
    }

    if (response.pods_size() != 1) {
        fprintf(stderr, "pod size not 1[%d]\n", 
                        response.pods_size()); 
        return;
    }

    const ::baidu::galaxy::PodPropertiy& pod = response.pods(0);

    FLAGS_initd_endpoint = pod.initd_endpoint();
    FLAGS_chroot = pod.pod_path();
    ::baidu::galaxy::Initd_Stub* initd;
    std::string initd_endpoint(FLAGS_initd_endpoint);
    rpc_client->GetStub(initd_endpoint, &initd);

    std::string pty_file;
    int pty_fdm = -1;
    if (!PreparePty(&pty_fdm, &pty_file)) {
        fprintf(stderr, "prepare pty failed\n"); 
        return;
    }

    baidu::galaxy::ExecuteRequest exec_request;
    // TODO unqic key 
    exec_request.set_key("client");
    exec_request.set_commands("/bin/bash");
    exec_request.set_path(".");
    exec_request.set_pty_file(pty_file);
    if (FLAGS_user != "") {
        exec_request.set_user(FLAGS_user);
    }
    if (FLAGS_chroot != "") {
        exec_request.set_chroot_path(FLAGS_chroot); 
    }
    std::string* lines_env = exec_request.add_envs();
    lines_env->append("LINES=");
    lines_env->append(FLAGS_LINES);
    std::string* columns_env = exec_request.add_envs();
    columns_env->append("COLUMNS=");
    columns_env->append(FLAGS_COLUMNS);
    std::string* xterm_env = exec_request.add_envs();
    xterm_env->append("TERM=");
    xterm_env->append(FLAGS_TERM);
    baidu::galaxy::ExecuteResponse exec_response;
    ret = rpc_client->SendRequest(initd,
                            &baidu::galaxy::Initd_Stub::Execute,
                            &exec_request,
                            &exec_response, 5, 1);
    if (ret && exec_response.status() == baidu::galaxy::kOk) {
        fprintf(stdout, "terminate starting...\n");
        ret = TerminateContact(pty_fdm); 
        if (ret) {
            fprintf(stdout, "terminate contact over\n"); 
        } else {
            fprintf(stderr, "terminate contact interrupt\n"); 
        }
        return;
    } 
    fprintf(stderr, "exec in initd failed %s\n", 
            baidu::galaxy::Status_Name(exec_response.status()).c_str());
    return;
}

int main(int argc, char* argv[]) {
    FLAGS_flagfile="galaxy.flag";
    ::google::SetUsageMessage(SInitdCliUsage);
    ::google::ParseCommandLineFlags(&argc, &argv, true);
    if (argc < 2) {
        fprintf(stderr, "%s", SInitdCliUsage.c_str()); 
        return -1;
    } 

    if (strcmp(argv[1], "ps") == 0) {
        ListPods(); 
    } else if (strcmp(argv[1], "attach") == 0) {
        AttachPod(); 
    } else {
        fprintf(stderr, "%s", SInitdCliUsage.c_str()); 
        return -1;
    }
    return 0;
}

/* vim: set ts=4 sw=4 sts=4 tw=100 */
