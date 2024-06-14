from lib.k8s.volume_snapshot_class.api import K8sVolumeSnapshotClassApi
from lib.k8s.volume_snapshot_class.info import K8sVolumeSnapshotClassInfo


class K8sVolumeSnapshotClass(
        K8sVolumeSnapshotClassApi,
        K8sVolumeSnapshotClassInfo
        ):
    def __init__(self):
        K8sVolumeSnapshotClassApi.__init__(self)
        K8sVolumeSnapshotClassInfo.__init__(self)
