from lib.osp.floating_ip.api import OspFloatingIpApi
from lib.osp.floating_ip.info import OspFloatingIpInfo


class OspFloatingIp(
        OspFloatingIpApi,
        OspFloatingIpInfo
        ):
    def __init__(self):
        OspFloatingIpApi.__init__(self)
        OspFloatingIpInfo.__init__(self)
