from lib.nso.cnfm.cluster.api import NsoCnfmClusterApi
from lib.nso.cnfm.cluster.info import NsoCnfmClusterInfo


class NsoCnfmCluster(
        NsoCnfmClusterApi,
        NsoCnfmClusterInfo
        ):
    def __init__(self):
        NsoCnfmClusterApi.__init__(self)
        NsoCnfmClusterInfo.__init__(self)
