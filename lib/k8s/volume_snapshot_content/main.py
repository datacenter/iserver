from lib.k8s.volume_snapshot_content.api import K8sVolumeSnapshotContentApi
from lib.k8s.volume_snapshot_content.info import K8sVolumeSnapshotContentInfo


class K8sVolumeSnapshotContent(
        K8sVolumeSnapshotContentApi,
        K8sVolumeSnapshotContentInfo
        ):
    def __init__(self):
        K8sVolumeSnapshotContentApi.__init__(self)
        K8sVolumeSnapshotContentInfo.__init__(self)
