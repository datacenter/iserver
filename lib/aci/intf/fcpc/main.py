from lib.aci.intf.fcpc.api import InterfaceFcPcApi
from lib.aci.intf.fcpc.info import InterfaceFcPcInfo
from lib.aci.intf.fcpc.audit.main import InterfaceFcPcAudit
from lib.aci.intf.fcpc.event.main import InterfaceFcPcEvent
from lib.aci.intf.fcpc.fault.main import InterfaceFcPcFault


class InterfaceFcPc(
        InterfaceFcPcApi,
        InterfaceFcPcInfo,
        InterfaceFcPcAudit,
        InterfaceFcPcEvent,
        InterfaceFcPcFault
        ):
    def __init__(self):
        InterfaceFcPcApi.__init__(self)
        InterfaceFcPcInfo.__init__(self)
        InterfaceFcPcAudit.__init__(self)
        InterfaceFcPcEvent.__init__(self)
        InterfaceFcPcFault.__init__(self)
