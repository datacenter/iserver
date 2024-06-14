from lib.aci.system.fault.api import SystemFaultApi
from lib.aci.system.fault.info import SystemFaultInfo
from lib.aci.system.fault.code.main import SystemFaultCode


class SystemFault(SystemFaultApi, SystemFaultInfo, SystemFaultCode):
    def __init__(self):
        SystemFaultApi.__init__(self)
        SystemFaultInfo.__init__(self)
        SystemFaultCode.__init__(self)
