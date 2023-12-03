from lib.linux.bond.cmd import LinuxBondCmd
from lib.linux.bond.info import LinuxBondInfo


class LinuxBond(
        LinuxBondCmd,
        LinuxBondInfo
        ):
    def __init__(self):
        LinuxBondCmd.__init__(self)
        LinuxBondInfo.__init__(self)
