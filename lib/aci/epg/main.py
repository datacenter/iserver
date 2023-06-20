from lib.aci.epg.api import EpgApi
from lib.aci.epg.info import EpgInfo
from lib.aci.epg.ifconn.main import EpgIfConn
from lib.aci.epg.locale.main import EpgLocale


class Epg(
        EpgApi,
        EpgInfo,
        EpgIfConn,
        EpgLocale
        ):
    def __init__(self):
        EpgApi.__init__(self)
        EpgInfo.__init__(self)
        EpgIfConn.__init__(self)
        EpgLocale.__init__(self)
