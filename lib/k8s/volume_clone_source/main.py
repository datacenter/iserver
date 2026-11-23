from lib.k8s.volume_clone_source.api import K8sVolumeCloneSourceApi
from lib.k8s.volume_clone_source.info import K8sVolumeCloneSourceInfo


class K8sVolumeCloneSource(
        K8sVolumeCloneSourceApi,
        K8sVolumeCloneSourceInfo
        ):
    def __init__(self):
        K8sVolumeCloneSourceApi.__init__(self)
        K8sVolumeCloneSourceInfo.__init__(self)
