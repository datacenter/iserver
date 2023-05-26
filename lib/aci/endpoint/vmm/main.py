from lib.aci.endpoint.vmm.hv.main import EndpointVmmHv
from lib.aci.endpoint.vmm.vm.main import EndpointVmmVm
from lib.aci.endpoint.vmm.vnic.main import EndpointVmmVnic


class EndpointVmm(EndpointVmmHv, EndpointVmmVm, EndpointVmmVnic):
    def __init__(self, log_id=None):
        EndpointVmmHv.__init__(self)
        EndpointVmmVm.__init__(self)
        EndpointVmmVnic.__init__(self)
