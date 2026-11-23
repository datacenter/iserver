from lib.k8s.volume_upload_source.api import K8sVolumeUploadSourceApi
from lib.k8s.volume_upload_source.info import K8sVolumeUploadSourceInfo


class K8sVolumeUploadSource(
        K8sVolumeUploadSourceApi,
        K8sVolumeUploadSourceInfo
        ):
    def __init__(self):
        K8sVolumeUploadSourceApi.__init__(self)
        K8sVolumeUploadSourceInfo.__init__(self)
