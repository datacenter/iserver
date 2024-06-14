from lib.aci.intf.fc.api import InterfaceFcApi
from lib.aci.intf.fc.info import InterfaceFcInfo
from lib.aci.intf.fc.audit.main import InterfaceFcAudit
from lib.aci.intf.fc.event.main import InterfaceFcEvent
from lib.aci.intf.fc.fault.main import InterfaceFcFault


class InterfaceFc(
        InterfaceFcApi,
        InterfaceFcInfo,
        InterfaceFcAudit,
        InterfaceFcEvent,
        InterfaceFcFault
        ):
    def __init__(self):
        InterfaceFcApi.__init__(self)
        InterfaceFcInfo.__init__(self)
        InterfaceFcAudit.__init__(self)
        InterfaceFcEvent.__init__(self)
        InterfaceFcFault.__init__(self)
