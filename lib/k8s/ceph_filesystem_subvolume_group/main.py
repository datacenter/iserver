from lib.k8s.ceph_filesystem_subvolume_group.api import K8sCephFilesystemSubVolumeGroupApi
from lib.k8s.ceph_filesystem_subvolume_group.info import K8sCephFilesystemSubVolumeGroupInfo


class K8sCephFilesystemSubVolumeGroup(
        K8sCephFilesystemSubVolumeGroupApi,
        K8sCephFilesystemSubVolumeGroupInfo
        ):
    def __init__(self):
        K8sCephFilesystemSubVolumeGroupApi.__init__(self)
        K8sCephFilesystemSubVolumeGroupInfo.__init__(self)
