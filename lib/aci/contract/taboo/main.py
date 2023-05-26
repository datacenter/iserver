from lib.aci.contract.taboo.api import TabooApi
from lib.aci.contract.taboo.info import TabooInfo


class Taboo(TabooApi, TabooInfo):
    def __init__(self):
        TabooApi.__init__(self)
        TabooInfo.__init__(self)
