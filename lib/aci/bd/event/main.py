from lib.aci.bd.event.api import BridgeDomainEventApi
from lib.aci.bd.event.info import BridgeDomainEventInfo


class BridgeDomainEvent(BridgeDomainEventApi, BridgeDomainEventInfo):
    def __init__(self):
        BridgeDomainEventApi.__init__(self)
        BridgeDomainEventInfo.__init__(self)
