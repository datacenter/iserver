from lib.aci.endpoint.vmm.vnic.api import EndpointVmmVnicApi
from lib.aci.endpoint.vmm.vnic.info import EndpointVmmVnicInfo


class EndpointVmmVnic(EndpointVmmVnicApi, EndpointVmmVnicInfo):
    def __init__(self):
        EndpointVmmVnicApi.__init__(self)
        EndpointVmmVnicInfo.__init__(self)
