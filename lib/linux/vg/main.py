from lib.linux.vg.cmd import LinuxVgCmd
from lib.linux.vg.info import LinuxVgInfo


class LinuxVg(
        LinuxVgCmd,
        LinuxVgInfo
        ):
    def __init__(self):
        LinuxVgCmd.__init__(self)
        LinuxVgInfo.__init__(self)
