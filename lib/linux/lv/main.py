from lib.linux.lv.cmd import LinuxLvCmd
from lib.linux.lv.info import LinuxLvInfo


class LinuxLv(
        LinuxLvCmd,
        LinuxLvInfo
        ):
    def __init__(self):
        LinuxLvCmd.__init__(self)
        LinuxLvInfo.__init__(self)
