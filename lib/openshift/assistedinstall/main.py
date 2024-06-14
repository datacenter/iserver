from lib.openshift.assistedinstall.api import AssistedInstallApi
from lib.openshift.assistedinstall.cluster.main import AssistedInstallCluster
from lib.openshift.assistedinstall.event.main import AssistedInstallEvent
from lib.openshift.assistedinstall.infra.main import AssistedInstallInfra
from lib.openshift.assistedinstall.manifest.main import AssistedInstallManifest
from lib.openshift.assistedinstall.version.main import AssistedInstallVersion


class AssistedInstall(
        AssistedInstallApi,
        AssistedInstallCluster,
        AssistedInstallEvent,
        AssistedInstallInfra,
        AssistedInstallManifest,
        AssistedInstallVersion
        ):
    def __init__(self):
        AssistedInstallApi.__init__(self)
        AssistedInstallCluster.__init__(self)
        AssistedInstallEvent.__init__(self)
        AssistedInstallInfra.__init__(self)
        AssistedInstallManifest.__init__(self)
        AssistedInstallVersion.__init__(self)
