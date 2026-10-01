from lib.linux.helm.cmd import LinuxHelmCmd
from lib.linux.helm.chart import LinuxHelmChartInfo
from lib.linux.helm.repo import LinuxHelmRepoInfo


class LinuxHelm(
        LinuxHelmCmd,
        LinuxHelmChartInfo,
        LinuxHelmRepoInfo
        ):
    def __init__(self):
        LinuxHelmCmd.__init__(self)
        LinuxHelmChartInfo.__init__(self)
        LinuxHelmRepoInfo.__init__(self)