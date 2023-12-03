from lib.osp.hypervisor.api import OspHypervisorApi
from lib.osp.hypervisor.info import OspHypervisorInfo


class OspHypervisor(
        OspHypervisorApi,
        OspHypervisorInfo
        ):
    def __init__(self):
        OspHypervisorApi.__init__(self)
        OspHypervisorInfo.__init__(self)
