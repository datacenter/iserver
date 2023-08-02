from lib.aci.epg.api import EpgApi
from lib.aci.epg.info import EpgInfo
from lib.aci.epg.ifconn.main import EpgIfConn
from lib.aci.epg.locale.main import EpgLocale
from lib.aci.epg.audit.main import EpgAudit
from lib.aci.epg.event.main import EpgEvent
from lib.aci.epg.fault.main import EpgFault
from lib.aci.epg.node.main import EpgNode


class Epg(
        EpgApi,
        EpgInfo,
        EpgIfConn,
        EpgLocale,
        EpgAudit,
        EpgEvent,
        EpgFault,
        EpgNode
        ):
    def __init__(self):
        EpgApi.__init__(self)
        EpgInfo.__init__(self)
        EpgIfConn.__init__(self)
        EpgLocale.__init__(self)
        EpgAudit.__init__(self)
        EpgEvent.__init__(self)
        EpgFault.__init__(self)
        EpgNode.__init__(self)
