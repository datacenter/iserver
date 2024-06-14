from lib.aci.epg.locale.api import EpgLocaleApi
from lib.aci.epg.locale.info import EpgLocaleInfo


class EpgLocale(EpgLocaleApi, EpgLocaleInfo):
    def __init__(self):
        EpgLocaleApi.__init__(self)
        EpgLocaleInfo.__init__(self)
