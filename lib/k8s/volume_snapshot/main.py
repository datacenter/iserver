from lib.k8s.volume_snapshot.api import K8sVolumeSnapshotApi
from lib.k8s.volume_snapshot.info import K8sVolumeSnapshotInfo
from lib.k8s.volume_snapshot.create import K8sVolumeSnapshotCreate
from lib.k8s.volume_snapshot.wait import K8sVolumeSnapshotWait


class K8sVolumeSnapshot(
        K8sVolumeSnapshotApi,
        K8sVolumeSnapshotInfo,
        K8sVolumeSnapshotCreate,
        K8sVolumeSnapshotWait
        ):
    def __init__(self):
        K8sVolumeSnapshotApi.__init__(self)
        K8sVolumeSnapshotInfo.__init__(self)
        K8sVolumeSnapshotCreate.__init__(self)
        K8sVolumeSnapshotWait.__init__(self)
