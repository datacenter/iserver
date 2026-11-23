from lib.openshift.assistedinstall.infra.api import AssistedInstallInfraApi
from lib.openshift.assistedinstall.infra.info import AssistedInstallInfraInfo


class AssistedInstallInfra(
        AssistedInstallInfraApi,
        AssistedInstallInfraInfo
        ):
    def __init__(self):
        AssistedInstallInfraApi.__init__(self)
        AssistedInstallInfraInfo.__init__(self)
