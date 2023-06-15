from lib.aci.epg.api import EpgApi
from lib.aci.epg.info import EpgInfo
from lib.aci.epg.stats.main import EpgStats


class Epg(EpgApi, EpgInfo, EpgStats):
    def __init__(self):
        EpgApi.__init__(self)
        EpgInfo.__init__(self)
        EpgStats.__init__(self)
