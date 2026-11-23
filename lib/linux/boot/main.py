from lib.linux.boot.cmd import LinuxBootCmd
from lib.linux.boot.info import LinuxBootInfo


class LinuxBoot(
        LinuxBootCmd,
        LinuxBootInfo
        ):
    def __init__(self):
        LinuxBootCmd.__init__(self)
        LinuxBootInfo.__init__(self)
