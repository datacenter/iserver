from lib.linux.container_policy.cmd import LinuxContainerPolicyCmd
from lib.linux.container_policy.info import LinuxContainerPolicyInfo


class LinuxContainerPolicy(
        LinuxContainerPolicyCmd,
        LinuxContainerPolicyInfo
        ):
    def __init__(self):
        LinuxContainerPolicyCmd.__init__(self)
        LinuxContainerPolicyInfo.__init__(self)
