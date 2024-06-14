from lib.nso.cnfm.result.api import NsoCnfmResultApi
from lib.nso.cnfm.result.info import NsoCnfmResultInfo


class NsoCnfmResult(
        NsoCnfmResultApi,
        NsoCnfmResultInfo
        ):
    def __init__(self):
        NsoCnfmResultApi.__init__(self)
        NsoCnfmResultInfo.__init__(self)
