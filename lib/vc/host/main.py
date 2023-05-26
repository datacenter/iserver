from lib.vc.host.api import VcHostApi
from lib.vc.host.filtering import VcHostFiltering
from lib.vc.host.networking import VcHostNetworking
from lib.vc.host.summary import VcHostSummary


class VcHost(VcHostApi, VcHostFiltering, VcHostNetworking, VcHostSummary):
    def __init__(self):
        VcHostApi.__init__(self)
        VcHostFiltering.__init__(self)
        VcHostNetworking.__init__(self)
        VcHostSummary.__init__(self)
