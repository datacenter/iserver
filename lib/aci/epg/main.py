from lib.aci.epg.api import EpgApi
from lib.aci.epg.info import EpgInfo


class Epg(EpgApi, EpgInfo):
    def __init__(self):
        EpgApi.__init__(self)
        EpgInfo.__init__(self)
