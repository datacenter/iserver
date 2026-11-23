from lib.nexus.interface.trans.api import InterfaceTransApi
from lib.nexus.interface.trans.info import InterfaceTransInfo


class InterfaceTrans(
        InterfaceTransApi,
        InterfaceTransInfo
        ):
    def __init__(self):
        InterfaceTransApi.__init__(self)
        InterfaceTransInfo.__init__(self)
