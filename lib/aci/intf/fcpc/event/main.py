from lib.aci.intf.fcpc.event.api import InterfaceFcPcEventApi
from lib.aci.intf.fcpc.event.info import InterfaceFcPcEventInfo


class InterfaceFcPcEvent(InterfaceFcPcEventApi, InterfaceFcPcEventInfo):
    def __init__(self):
        InterfaceFcPcEventApi.__init__(self)
        InterfaceFcPcEventInfo.__init__(self)
