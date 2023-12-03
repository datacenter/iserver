from lib.nso.cnfm.cluster.main import NsoCnfmCluster
from lib.nso.cnfm.cnfd.main import NsoCnfmCnfd
from lib.nso.cnfm.cnfi.main import NsoCnfmCnfi
from lib.nso.cnfm.device.main import NsoCnfmDevice
from lib.nso.cnfm.plan.main import NsoCnfmPlan
from lib.nso.cnfm.release.main import NsoCnfmRelease
from lib.nso.cnfm.result.main import NsoCnfmResult


class NsoCnfm(
        NsoCnfmCluster,
        NsoCnfmCnfd,
        NsoCnfmCnfi,
        NsoCnfmDevice,
        NsoCnfmPlan,
        NsoCnfmRelease,
        NsoCnfmResult
        ):
    def __init__(self):
        NsoCnfmCluster.__init__(self)
        NsoCnfmCnfd.__init__(self)
        NsoCnfmCnfi.__init__(self)
        NsoCnfmDevice.__init__(self)
        NsoCnfmPlan.__init__(self)
        NsoCnfmRelease.__init__(self)
        NsoCnfmResult.__init__(self)
