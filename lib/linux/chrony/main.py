from lib.linux.chrony.cmd import LinuxChronyCmd
from lib.linux.chrony.info import LinuxChronyInfo


class LinuxChrony(
        LinuxChronyCmd,
        LinuxChronyInfo
        ):
    def __init__(self):
        LinuxChronyCmd.__init__(self)
        LinuxChronyInfo.__init__(self)
