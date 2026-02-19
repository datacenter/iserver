from lib.linux.lsblk.cmd import LinuxLsblkCmd
from lib.linux.lsblk.info import LinuxLsblkInfo


class LinuxLsblk(
        LinuxLsblkCmd,
        LinuxLsblkInfo
        ):
    def __init__(self):
        LinuxLsblkCmd.__init__(self)
        LinuxLsblkInfo.__init__(self)
