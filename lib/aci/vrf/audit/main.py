from lib.aci.vrf.audit.api import VrfAuditApi
from lib.aci.vrf.audit.info import VrfAuditInfo


class VrfAudit(VrfAuditApi, VrfAuditInfo):
    def __init__(self):
        VrfAuditApi.__init__(self)
        VrfAuditInfo.__init__(self)
