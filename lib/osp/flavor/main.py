from lib.osp.flavor.api import OspFlavorApi
from lib.osp.flavor.info import OspFlavorInfo


class OspFlavor(
        OspFlavorApi,
        OspFlavorInfo
        ):
    def __init__(self):
        OspFlavorApi.__init__(self)
        OspFlavorInfo.__init__(self)
