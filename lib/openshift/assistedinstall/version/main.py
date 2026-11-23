from lib.openshift.assistedinstall.version.api import AssistedInstallVersionApi
from lib.openshift.assistedinstall.version.info import AssistedInstallVersionInfo


class AssistedInstallVersion(
        AssistedInstallVersionApi,
        AssistedInstallVersionInfo
        ):
    def __init__(self):
        AssistedInstallVersionApi.__init__(self)
        AssistedInstallVersionInfo.__init__(self)
