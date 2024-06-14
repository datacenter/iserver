from lib.aci.proto.isis.route.api import ProtocolIsisRouteApi
from lib.aci.proto.isis.route.info import ProtocolIsisRouteInfo


class ProtocolIsisRoute(ProtocolIsisRouteApi, ProtocolIsisRouteInfo):
    def __init__(self):
        ProtocolIsisRouteApi.__init__(self)
        ProtocolIsisRouteInfo.__init__(self)
