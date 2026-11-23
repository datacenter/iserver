from lib.k8s.volume_import_source.api import K8sVolumeImportSourceApi
from lib.k8s.volume_import_source.info import K8sVolumeImportSourceInfo


class K8sVolumeImportSource(
        K8sVolumeImportSourceApi,
        K8sVolumeImportSourceInfo
        ):
    def __init__(self):
        K8sVolumeImportSourceApi.__init__(self)
        K8sVolumeImportSourceInfo.__init__(self)
