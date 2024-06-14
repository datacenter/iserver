from lib.aci.endpoint.api import EndpointApi
from lib.aci.endpoint.info import EndpointInfo
from lib.aci.endpoint.ip.main import EndpointIp
from lib.aci.endpoint.hv.main import EndpointHv
from lib.aci.endpoint.vm.main import EndpointVm
from lib.aci.endpoint.vmm.main import EndpointVmm


class Endpoint(EndpointApi, EndpointInfo, EndpointIp, EndpointHv, EndpointVm, EndpointVmm):
    def __init__(self):
        EndpointApi.__init__(self)
        EndpointInfo.__init__(self)
        EndpointIp.__init__(self)
        EndpointHv.__init__(self)
        EndpointVm.__init__(self)
        EndpointVmm.__init__(self)
