from lib.nexus.interface.brief.api import InterfaceBriefApi
from lib.nexus.interface.brief.info import InterfaceBriefInfo


class InterfaceBrief(
        InterfaceBriefApi,
        InterfaceBriefInfo
        ):
    def __init__(self):
        InterfaceBriefApi.__init__(self)
        InterfaceBriefInfo.__init__(self)
