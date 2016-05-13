// Copyright (c) 2016, Baidu.com, Inc. All Rights Reserved
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "mounter.h"

#include "util/error_code.h"

#include "boost/filesystem/path.hpp"
#include "boost/thread/thread_time.hpp"
#include "boost/filesystem/operations.hpp"

#include <sys/mount.h>

#include <string>


namespace baidu {
    namespace galaxy {
        namespace volum {
            baidu::galaxy::util::ErrorCode MountProc(const std::string& target) {
                boost::filesystem::path path(target);
                boost::system::error_code ec;
                
                if (!boost::filesystem::exists(path, ec)) {
                    return ERRORCODE(-1, "target(%s) donot exist", target.c_str());
                }
                
                if (!boost::filesystem::is_directory(path, ec)) {
                    return ERRORCODE(-1, "target(%s) is not directory", target.c_str());
                }
                
                if (0 != ::mount("proc", target.c_str(), "proc", 0, NULL)) {
                    return PERRORCODE(-1, errno, "mount target(%s) failed", target.c_str());
                }
                
                return ERRORCODE_OK;
            }
            
            baidu::galaxy::util::ErrorCode MountDir(const std::string& source, const std::string& target) {
                boost::filesystem::path source_path(source);
                boost::system::error_code ec;
                if (!boost::filesystem::exists(source_path, ec)) {
                    return ERRORCODE(-1, "source(%s) donot exist", source.c_str());
                }
                
                if (!boost::filesystem::is_directory(source_path, ec)) {
                    return ERRORCODE(-1, "target(%s) is not directory", source.c_str());
                }
                
                boost::filesystem::path target_path(target);
                if (!boost::filesystem::exists(target_path, ec)) {
                    return  ERRORCODE(-1, "target(%s) donot exist", target.c_str());
                }
                
                if (!boost::filesystem::is_directory(target_path, ec)) {
                    return ERRORCODE(-1, "target(%s) is not directory", target.c_str());
                }
                
                if (0 != ::mount(source.c_str(), target.c_str(), "", MS_BIND, NULL)) {
                    return PERRORCODE(-1, errno, "mount %s to %s failed", source.c_str(), target.c_str());
                }
                return ERRORCODE_OK;
            }
            
            baidu::galaxy::util::ErrorCode MountTmpfs(const std::string& target, uint64_t size, bool readonly) {
               
                boost::system::error_code ec;
                boost::filesystem::path target_path(target);
                if (!boost::filesystem::exists(target_path, ec)) {
                    return  ERRORCODE(-1, "target(%s) donot exist", target.c_str());
                }
                
                std::stringstream ss;
                ss << "size=" << size;
                
                int flag = 0; 
                if (readonly) {
                    flag |= MS_RDONLY;
                }
                
                if (0 != ::mount("tmpfs", target.c_str(), "tmpfs", flag,  ss.str().c_str())) {
                    return PERRORCODE(-1, errno, "mount tmpfs to %s failed", target.c_str());
                }
                return ERRORCODE_OK;
            }
        }
    }
}