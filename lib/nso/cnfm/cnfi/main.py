from lib.nso.cnfm.cnfi.api import NsoCnfmCnfiApi
from lib.nso.cnfm.cnfi.info import NsoCnfmCnfiInfo


class NsoCnfmCnfi(
        NsoCnfmCnfiApi,
        NsoCnfmCnfiInfo
        ):
    def __init__(self):
        NsoCnfmCnfiApi.__init__(self)
        NsoCnfmCnfiInfo.__init__(self)
