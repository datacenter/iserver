from lib.nso.cnfm.cnfd.api import NsoCnfmCnfdApi
from lib.nso.cnfm.cnfd.info import NsoCnfmCnfdInfo


class NsoCnfmCnfd(
        NsoCnfmCnfdApi,
        NsoCnfmCnfdInfo
        ):
    def __init__(self):
        NsoCnfmCnfdApi.__init__(self)
        NsoCnfmCnfdInfo.__init__(self)
