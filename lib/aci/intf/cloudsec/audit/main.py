from lib.aci.intf.cloudsec.audit.api import InterfaceCloudSecAuditApi
from lib.aci.intf.cloudsec.audit.info import InterfaceCloudSecAuditInfo


class InterfaceCloudSecAudit(InterfaceCloudSecAuditApi, InterfaceCloudSecAuditInfo):
    def __init__(self):
        InterfaceCloudSecAuditApi.__init__(self)
        InterfaceCloudSecAuditInfo.__init__(self)
