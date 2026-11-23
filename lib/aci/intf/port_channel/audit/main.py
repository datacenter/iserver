from lib.aci.intf.port_channel.audit.api import InterfacePortChannelAuditApi
from lib.aci.intf.port_channel.audit.info import InterfacePortChannelAuditInfo


class InterfacePortChannelAudit(InterfacePortChannelAuditApi, InterfacePortChannelAuditInfo):
    def __init__(self):
        InterfacePortChannelAuditApi.__init__(self)
        InterfacePortChannelAuditInfo.__init__(self)
