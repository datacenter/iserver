from lib.openshift.assistedinstall.cluster.api import AssistedInstallClusterApi
from lib.openshift.assistedinstall.cluster.info import AssistedInstallClusterInfo


class AssistedInstallCluster(
        AssistedInstallClusterApi,
        AssistedInstallClusterInfo
        ):
    def __init__(self):
        AssistedInstallClusterApi.__init__(self)
        AssistedInstallClusterInfo.__init__(self)
