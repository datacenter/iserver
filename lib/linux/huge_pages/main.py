from lib.linux.huge_pages.cmd import LinuxHugePagesCmd
from lib.linux.huge_pages.info import LinuxHugePagesInfo


class LinuxHugePages(
        LinuxHugePagesCmd,
        LinuxHugePagesInfo
        ):
    def __init__(self):
        LinuxHugePagesCmd.__init__(self)
        LinuxHugePagesInfo.__init__(self)
