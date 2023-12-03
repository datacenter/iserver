from lib.osp.snapshot.api import OspSnapshotApi
from lib.osp.snapshot.info import OspSnapshotInfo


class OspSnapshot(
        OspSnapshotApi,
        OspSnapshotInfo
        ):
    def __init__(self):
        OspSnapshotApi.__init__(self)
        OspSnapshotInfo.__init__(self)
