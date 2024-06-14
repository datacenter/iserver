from lib.osp.image.api import OspImageApi
from lib.osp.image.info import OspImageInfo
from lib.osp.image.task import OspImageTask


class OspImage(
        OspImageApi,
        OspImageInfo,
        OspImageTask
        ):
    def __init__(self):
        OspImageApi.__init__(self)
        OspImageInfo.__init__(self)
        OspImageTask.__init__(self)
