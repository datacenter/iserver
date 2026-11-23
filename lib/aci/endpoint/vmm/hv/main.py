from lib.aci.endpoint.vmm.hv.api import EndpointVmmHvApi
from lib.aci.endpoint.vmm.hv.info import EndpointVmmHvInfo


class EndpointVmmHv(EndpointVmmHvApi, EndpointVmmHvInfo):
    def __init__(self):
        EndpointVmmHvApi.__init__(self)
        EndpointVmmHvInfo.__init__(self)
