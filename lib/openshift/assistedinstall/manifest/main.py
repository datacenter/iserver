from lib.openshift.assistedinstall.manifest.api import AssistedInstallManifestApi
from lib.openshift.assistedinstall.manifest.info import AssistedInstallManifestInfo


class AssistedInstallManifest(
        AssistedInstallManifestApi,
        AssistedInstallManifestInfo
        ):
    def __init__(self):
        AssistedInstallManifestApi.__init__(self)
        AssistedInstallManifestInfo.__init__(self)
