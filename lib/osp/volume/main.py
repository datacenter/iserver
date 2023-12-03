from lib.osp.volume.api import OspVolumeApi
from lib.osp.volume.info import OspVolumeInfo


class OspVolume(
        OspVolumeApi,
        OspVolumeInfo
        ):
    def __init__(self):
        OspVolumeApi.__init__(self)
        OspVolumeInfo.__init__(self)
