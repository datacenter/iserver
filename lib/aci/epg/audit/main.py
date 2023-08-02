from lib.aci.epg.audit.api import EpgAuditApi
from lib.aci.epg.audit.info import EpgAuditInfo


class EpgAudit(EpgAuditApi, EpgAuditInfo):
    def __init__(self):
        EpgAuditApi.__init__(self)
        EpgAuditInfo.__init__(self)
