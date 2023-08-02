from lib.aci.epg.event.api import EpgEventApi
from lib.aci.epg.event.info import EpgEventInfo


class EpgEvent(EpgEventApi, EpgEventInfo):
    def __init__(self):
        EpgEventApi.__init__(self)
        EpgEventInfo.__init__(self)
