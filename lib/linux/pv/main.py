from lib.linux.pv.cmd import LinuxPvCmd
from lib.linux.pv.info import LinuxPvInfo


class LinuxPv(
        LinuxPvCmd,
        LinuxPvInfo
        ):
    def __init__(self):
        LinuxPvCmd.__init__(self)
        LinuxPvInfo.__init__(self)
