from lib.linux.sysctl.cmd import LinuxSysctlCmd
from lib.linux.sysctl.info import LinuxSysctlInfo


class LinuxSysctl(
        LinuxSysctlCmd,
        LinuxSysctlInfo
        ):
    def __init__(self):
        LinuxSysctlCmd.__init__(self)
        LinuxSysctlInfo.__init__(self)
