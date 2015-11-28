# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: galaxy.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='galaxy.proto',
  package='baidu.galaxy',
  serialized_pb='\n\x0cgalaxy.proto\x12\x0c\x62\x61idu.galaxy\"%\n\x06Volume\x12\r\n\x05quota\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x86\x01\n\x08Resource\x12\x12\n\nmillicores\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x03\x12\r\n\x05ports\x18\x03 \x03(\x05\x12#\n\x05\x64isks\x18\x04 \x03(\x0b\x32\x14.baidu.galaxy.Volume\x12\"\n\x04ssds\x18\x05 \x03(\x0b\x32\x14.baidu.galaxy.Volume\"\xce\x02\n\x0eTaskDescriptor\x12\x0e\n\x06\x62inary\x18\x01 \x01(\x0c\x12\x15\n\rstart_command\x18\x02 \x01(\t\x12\x14\n\x0cstop_command\x18\x03 \x01(\t\x12+\n\x0brequirement\x18\x04 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12\x0e\n\x06labels\x18\x05 \x03(\t\x12\x0b\n\x03\x65nv\x18\x06 \x03(\t\x12\x0e\n\x06offset\x18\x07 \x01(\x05\x12-\n\x0bsource_type\x18\x08 \x01(\x0e\x32\x18.baidu.galaxy.SourceType\x12:\n\x12mem_isolation_type\x18\t \x01(\x0e\x32\x1e.baidu.galaxy.MemIsolationType\x12:\n\x12\x63pu_isolation_type\x18\n \x01(\x0e\x32\x1e.baidu.galaxy.CpuIsolationType\"\xa7\x01\n\rPodDescriptor\x12+\n\x05tasks\x18\x01 \x03(\x0b\x32\x1c.baidu.galaxy.TaskDescriptor\x12+\n\x0brequirement\x18\x02 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12\x1b\n\x0cpin_on_agent\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"\x97\x01\n\nTaskStatus\x12\x0e\n\x06taskid\x18\x01 \x01(\t\x12\x11\n\texit_code\x18\x02 \x01(\x05\x12-\n\rresource_used\x18\x03 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12\x0f\n\x07version\x18\x04 \x01(\t\x12&\n\x05state\x18\x05 \x01(\x0e\x32\x17.baidu.galaxy.TaskState\"\x88\x02\n\tPodStatus\x12\r\n\x05podid\x18\x01 \x01(\t\x12\r\n\x05jobid\x18\x02 \x01(\t\x12(\n\x06status\x18\x03 \x03(\x0b\x32\x18.baidu.galaxy.TaskStatus\x12-\n\rresource_used\x18\x04 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\t\x12%\n\x05state\x18\x07 \x01(\x0e\x32\x16.baidu.galaxy.PodState\x12%\n\x05stage\x18\x08 \x01(\x0e\x32\x16.baidu.galaxy.PodStage\x12\x13\n\x0bpod_gc_path\x18\t \x01(\t\x12\x0f\n\x07version\x18\n \x01(\t\"\x83\x02\n\tAgentInfo\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12%\n\x05total\x18\x02 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12(\n\x08\x61ssigned\x18\x03 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12$\n\x04used\x18\x05 \x01(\x0b\x32\x16.baidu.galaxy.Resource\x12%\n\x04pods\x18\x07 \x03(\x0b\x32\x17.baidu.galaxy.PodStatus\x12\'\n\x05state\x18\x08 \x01(\x0e\x32\x18.baidu.galaxy.AgentState\x12\x0f\n\x07version\x18\t \x01(\x05\x12\x0c\n\x04tags\x18\n \x03(\t*\xfd\x01\n\x06Status\x12\x07\n\x03kOk\x10\x00\x12\x0c\n\x08kUnknown\x10\x01\x12\n\n\x06kQuota\x10\x02\x12\x10\n\x0ckJobNotFound\x10\x03\x12\x10\n\x0ckPodNotFound\x10\x04\x12\x12\n\x0ekAgentNotFound\x10\x05\x12\x12\n\x0ekJobSubmitFail\x10\x06\x12\x12\n\x0ekJobUpdateFail\x10\x07\x12\r\n\tkNotFound\x10\x10\x12\x0f\n\x0bkInputError\x10\x11\x12\x15\n\x11kPersistenceError\x10\x12\x12\x15\n\x11kJobTerminateFail\x10\x13\x12\r\n\tkRpcError\x10\x14\x12\x13\n\x0fkLabelAgentFail\x10\x15*\x82\x01\n\x08PodState\x12\x0f\n\x0bkPodPending\x10\x00\x12\x11\n\rkPodDeploying\x10\x01\x12\x0f\n\x0bkPodRunning\x10\x02\x12\x11\n\rkPodTerminate\x10\x03\x12\x0f\n\x0bkPodSuspend\x10\x04\x12\x0e\n\nkPodFinish\x10\x05\x12\r\n\tkPodError\x10\x06*h\n\x08PodStage\x12\x11\n\rkStagePending\x10\x00\x12\x11\n\rkStageRunning\x10\x01\x12\x0f\n\x0bkStageDeath\x10\x02\x12\x11\n\rkStageRemoved\x10\x03\x12\x12\n\x0ekStageFinished\x10\x04*\x87\x01\n\tTaskState\x12\x10\n\x0ckTaskPending\x10\x00\x12\x0f\n\x0bkTaskDeploy\x10\x01\x12\x10\n\x0ckTaskRunning\x10\x02\x12\x12\n\x0ekTaskTerminate\x10\x03\x12\x10\n\x0ckTaskSuspend\x10\x04\x12\x0f\n\x0bkTaskFinish\x10\x05\x12\x0e\n\nkTaskError\x10\x06*7\n\nSourceType\x12\x15\n\x11kSourceTypeBinary\x10\x00\x12\x12\n\x0ekSourceTypeFTP\x10\x01*#\n\nAgentState\x12\n\n\x06kAlive\x10\x00\x12\t\n\x05kDead\x10\x01*C\n\x10MemIsolationType\x12\x17\n\x13kMemIsolationCgroup\x10\x00\x12\x16\n\x12kMemIsolationLimit\x10\x01*@\n\x10\x43puIsolationType\x12\x15\n\x11kCpuIsolationHard\x10\x00\x12\x15\n\x11kCpuIsolationSoft\x10\x01\x42\x03\x80\x01\x01')

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='baidu.galaxy.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kOk', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kUnknown', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kQuota', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kJobNotFound', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodNotFound', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kAgentNotFound', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kJobSubmitFail', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kJobUpdateFail', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kNotFound', index=8, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kInputError', index=9, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPersistenceError', index=10, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kJobTerminateFail', index=11, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRpcError', index=12, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kLabelAgentFail', index=13, number=21,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1397,
  serialized_end=1650,
)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_PODSTATE = _descriptor.EnumDescriptor(
  name='PodState',
  full_name='baidu.galaxy.PodState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kPodPending', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodDeploying', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodRunning', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodTerminate', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodSuspend', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodFinish', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPodError', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1653,
  serialized_end=1783,
)

PodState = enum_type_wrapper.EnumTypeWrapper(_PODSTATE)
_PODSTAGE = _descriptor.EnumDescriptor(
  name='PodStage',
  full_name='baidu.galaxy.PodStage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kStagePending', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStageRunning', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStageDeath', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStageRemoved', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStageFinished', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1785,
  serialized_end=1889,
)

PodStage = enum_type_wrapper.EnumTypeWrapper(_PODSTAGE)
_TASKSTATE = _descriptor.EnumDescriptor(
  name='TaskState',
  full_name='baidu.galaxy.TaskState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kTaskPending', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTaskDeploy', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTaskRunning', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTaskTerminate', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTaskSuspend', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTaskFinish', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTaskError', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1892,
  serialized_end=2027,
)

TaskState = enum_type_wrapper.EnumTypeWrapper(_TASKSTATE)
_SOURCETYPE = _descriptor.EnumDescriptor(
  name='SourceType',
  full_name='baidu.galaxy.SourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kSourceTypeBinary', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSourceTypeFTP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2029,
  serialized_end=2084,
)

SourceType = enum_type_wrapper.EnumTypeWrapper(_SOURCETYPE)
_AGENTSTATE = _descriptor.EnumDescriptor(
  name='AgentState',
  full_name='baidu.galaxy.AgentState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kAlive', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kDead', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2086,
  serialized_end=2121,
)

AgentState = enum_type_wrapper.EnumTypeWrapper(_AGENTSTATE)
_MEMISOLATIONTYPE = _descriptor.EnumDescriptor(
  name='MemIsolationType',
  full_name='baidu.galaxy.MemIsolationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kMemIsolationCgroup', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMemIsolationLimit', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2123,
  serialized_end=2190,
)

MemIsolationType = enum_type_wrapper.EnumTypeWrapper(_MEMISOLATIONTYPE)
_CPUISOLATIONTYPE = _descriptor.EnumDescriptor(
  name='CpuIsolationType',
  full_name='baidu.galaxy.CpuIsolationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kCpuIsolationHard', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kCpuIsolationSoft', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2192,
  serialized_end=2256,
)

CpuIsolationType = enum_type_wrapper.EnumTypeWrapper(_CPUISOLATIONTYPE)
kOk = 0
kUnknown = 1
kQuota = 2
kJobNotFound = 3
kPodNotFound = 4
kAgentNotFound = 5
kJobSubmitFail = 6
kJobUpdateFail = 7
kNotFound = 16
kInputError = 17
kPersistenceError = 18
kJobTerminateFail = 19
kRpcError = 20
kLabelAgentFail = 21
kPodPending = 0
kPodDeploying = 1
kPodRunning = 2
kPodTerminate = 3
kPodSuspend = 4
kPodFinish = 5
kPodError = 6
kStagePending = 0
kStageRunning = 1
kStageDeath = 2
kStageRemoved = 3
kStageFinished = 4
kTaskPending = 0
kTaskDeploy = 1
kTaskRunning = 2
kTaskTerminate = 3
kTaskSuspend = 4
kTaskFinish = 5
kTaskError = 6
kSourceTypeBinary = 0
kSourceTypeFTP = 1
kAlive = 0
kDead = 1
kMemIsolationCgroup = 0
kMemIsolationLimit = 1
kCpuIsolationHard = 0
kCpuIsolationSoft = 1



_VOLUME = _descriptor.Descriptor(
  name='Volume',
  full_name='baidu.galaxy.Volume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quota', full_name='baidu.galaxy.Volume.quota', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='baidu.galaxy.Volume.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=67,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='baidu.galaxy.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='millicores', full_name='baidu.galaxy.Resource.millicores', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory', full_name='baidu.galaxy.Resource.memory', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ports', full_name='baidu.galaxy.Resource.ports', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disks', full_name='baidu.galaxy.Resource.disks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssds', full_name='baidu.galaxy.Resource.ssds', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=70,
  serialized_end=204,
)


_TASKDESCRIPTOR = _descriptor.Descriptor(
  name='TaskDescriptor',
  full_name='baidu.galaxy.TaskDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary', full_name='baidu.galaxy.TaskDescriptor.binary', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_command', full_name='baidu.galaxy.TaskDescriptor.start_command', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_command', full_name='baidu.galaxy.TaskDescriptor.stop_command', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requirement', full_name='baidu.galaxy.TaskDescriptor.requirement', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='baidu.galaxy.TaskDescriptor.labels', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='env', full_name='baidu.galaxy.TaskDescriptor.env', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='baidu.galaxy.TaskDescriptor.offset', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_type', full_name='baidu.galaxy.TaskDescriptor.source_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_isolation_type', full_name='baidu.galaxy.TaskDescriptor.mem_isolation_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_isolation_type', full_name='baidu.galaxy.TaskDescriptor.cpu_isolation_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=207,
  serialized_end=541,
)


_PODDESCRIPTOR = _descriptor.Descriptor(
  name='PodDescriptor',
  full_name='baidu.galaxy.PodDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='baidu.galaxy.PodDescriptor.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requirement', full_name='baidu.galaxy.PodDescriptor.requirement', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pin_on_agent', full_name='baidu.galaxy.PodDescriptor.pin_on_agent', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='baidu.galaxy.PodDescriptor.labels', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='baidu.galaxy.PodDescriptor.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=544,
  serialized_end=711,
)


_TASKSTATUS = _descriptor.Descriptor(
  name='TaskStatus',
  full_name='baidu.galaxy.TaskStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskid', full_name='baidu.galaxy.TaskStatus.taskid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='baidu.galaxy.TaskStatus.exit_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_used', full_name='baidu.galaxy.TaskStatus.resource_used', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='baidu.galaxy.TaskStatus.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='baidu.galaxy.TaskStatus.state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=714,
  serialized_end=865,
)


_PODSTATUS = _descriptor.Descriptor(
  name='PodStatus',
  full_name='baidu.galaxy.PodStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='podid', full_name='baidu.galaxy.PodStatus.podid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jobid', full_name='baidu.galaxy.PodStatus.jobid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='baidu.galaxy.PodStatus.status', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_used', full_name='baidu.galaxy.PodStatus.resource_used', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='baidu.galaxy.PodStatus.endpoint', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='baidu.galaxy.PodStatus.state', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage', full_name='baidu.galaxy.PodStatus.stage', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pod_gc_path', full_name='baidu.galaxy.PodStatus.pod_gc_path', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='baidu.galaxy.PodStatus.version', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=868,
  serialized_end=1132,
)


_AGENTINFO = _descriptor.Descriptor(
  name='AgentInfo',
  full_name='baidu.galaxy.AgentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='baidu.galaxy.AgentInfo.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='baidu.galaxy.AgentInfo.total', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assigned', full_name='baidu.galaxy.AgentInfo.assigned', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='baidu.galaxy.AgentInfo.used', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pods', full_name='baidu.galaxy.AgentInfo.pods', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='baidu.galaxy.AgentInfo.state', index=5,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='baidu.galaxy.AgentInfo.version', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='baidu.galaxy.AgentInfo.tags', index=7,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1135,
  serialized_end=1394,
)

_RESOURCE.fields_by_name['disks'].message_type = _VOLUME
_RESOURCE.fields_by_name['ssds'].message_type = _VOLUME
_TASKDESCRIPTOR.fields_by_name['requirement'].message_type = _RESOURCE
_TASKDESCRIPTOR.fields_by_name['source_type'].enum_type = _SOURCETYPE
_TASKDESCRIPTOR.fields_by_name['mem_isolation_type'].enum_type = _MEMISOLATIONTYPE
_TASKDESCRIPTOR.fields_by_name['cpu_isolation_type'].enum_type = _CPUISOLATIONTYPE
_PODDESCRIPTOR.fields_by_name['tasks'].message_type = _TASKDESCRIPTOR
_PODDESCRIPTOR.fields_by_name['requirement'].message_type = _RESOURCE
_TASKSTATUS.fields_by_name['resource_used'].message_type = _RESOURCE
_TASKSTATUS.fields_by_name['state'].enum_type = _TASKSTATE
_PODSTATUS.fields_by_name['status'].message_type = _TASKSTATUS
_PODSTATUS.fields_by_name['resource_used'].message_type = _RESOURCE
_PODSTATUS.fields_by_name['state'].enum_type = _PODSTATE
_PODSTATUS.fields_by_name['stage'].enum_type = _PODSTAGE
_AGENTINFO.fields_by_name['total'].message_type = _RESOURCE
_AGENTINFO.fields_by_name['assigned'].message_type = _RESOURCE
_AGENTINFO.fields_by_name['used'].message_type = _RESOURCE
_AGENTINFO.fields_by_name['pods'].message_type = _PODSTATUS
_AGENTINFO.fields_by_name['state'].enum_type = _AGENTSTATE
DESCRIPTOR.message_types_by_name['Volume'] = _VOLUME
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['TaskDescriptor'] = _TASKDESCRIPTOR
DESCRIPTOR.message_types_by_name['PodDescriptor'] = _PODDESCRIPTOR
DESCRIPTOR.message_types_by_name['TaskStatus'] = _TASKSTATUS
DESCRIPTOR.message_types_by_name['PodStatus'] = _PODSTATUS
DESCRIPTOR.message_types_by_name['AgentInfo'] = _AGENTINFO

class Volume(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VOLUME

  # @@protoc_insertion_point(class_scope:baidu.galaxy.Volume)

class Resource(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESOURCE

  # @@protoc_insertion_point(class_scope:baidu.galaxy.Resource)

class TaskDescriptor(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKDESCRIPTOR

  # @@protoc_insertion_point(class_scope:baidu.galaxy.TaskDescriptor)

class PodDescriptor(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PODDESCRIPTOR

  # @@protoc_insertion_point(class_scope:baidu.galaxy.PodDescriptor)

class TaskStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKSTATUS

  # @@protoc_insertion_point(class_scope:baidu.galaxy.TaskStatus)

class PodStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PODSTATUS

  # @@protoc_insertion_point(class_scope:baidu.galaxy.PodStatus)

class AgentInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AGENTINFO

  # @@protoc_insertion_point(class_scope:baidu.galaxy.AgentInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\200\001\001')
# @@protoc_insertion_point(module_scope)
