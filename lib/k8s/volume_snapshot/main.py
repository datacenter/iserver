from lib.k8s.volume_snapshot.api import K8sVolumeSnapshotApi
from lib.k8s.volume_snapshot.info import K8sVolumeSnapshotInfo


class K8sVolumeSnapshot(
        K8sVolumeSnapshotApi,
        K8sVolumeSnapshotInfo
        ):
    def __init__(self):
        K8sVolumeSnapshotApi.__init__(self)
        K8sVolumeSnapshotInfo.__init__(self)
