from lib.osp.subnet.api import OspSubnetApi
from lib.osp.subnet.info import OspSubnetInfo


class OspSubnet(
        OspSubnetApi,
        OspSubnetInfo
        ):
    def __init__(self):
        OspSubnetApi.__init__(self)
        OspSubnetInfo.__init__(self)
