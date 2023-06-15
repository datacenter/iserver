from lib.aci.epg.stats.api import EpgStatsApi
from lib.aci.epg.stats.info import EpgStatsInfo


class EpgStats(EpgStatsApi, EpgStatsInfo):
    def __init__(self):
        EpgStatsApi.__init__(self)
        EpgStatsInfo.__init__(self)
