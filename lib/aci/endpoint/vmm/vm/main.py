from lib.aci.endpoint.vmm.vm.api import EndpointVmmVmApi
from lib.aci.endpoint.vmm.vm.info import EndpointVmmVmInfo


class EndpointVmmVm(EndpointVmmVmApi, EndpointVmmVmInfo):
    def __init__(self):
        EndpointVmmVmApi.__init__(self)
        EndpointVmmVmInfo.__init__(self)
