from lib.nso.cnfm.release.api import NsoCnfmReleaseApi
from lib.nso.cnfm.release.info import NsoCnfmReleaseInfo


class NsoCnfmRelease(
        NsoCnfmReleaseApi,
        NsoCnfmReleaseInfo
        ):
    def __init__(self):
        NsoCnfmReleaseApi.__init__(self)
        NsoCnfmReleaseInfo.__init__(self)
