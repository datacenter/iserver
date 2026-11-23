from lib.aci.epg.ifconn.api import EpgIfConnApi
from lib.aci.epg.ifconn.info import EpgIfConnInfo


class EpgIfConn(EpgIfConnApi, EpgIfConnInfo):
    def __init__(self):
        EpgIfConnApi.__init__(self)
        EpgIfConnInfo.__init__(self)
