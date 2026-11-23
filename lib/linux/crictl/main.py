from lib.linux.crictl.cmd import LinuxCrictlCmd
from lib.linux.crictl.info import LinuxCrictlInfo


class LinuxCrictl(
        LinuxCrictlCmd,
        LinuxCrictlInfo
        ):
    def __init__(self):
        LinuxCrictlCmd.__init__(self)
        LinuxCrictlInfo.__init__(self)
