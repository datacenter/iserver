from lib.aci.intf.fc.event.api import InterfaceFcEventApi
from lib.aci.intf.fc.event.info import InterfaceFcEventInfo


class InterfaceFcEvent(InterfaceFcEventApi, InterfaceFcEventInfo):
    def __init__(self):
        InterfaceFcEventApi.__init__(self)
        InterfaceFcEventInfo.__init__(self)
