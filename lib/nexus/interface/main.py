from lib.nexus.interface.brief.main import InterfaceBrief
from lib.nexus.interface.state.main import InterfaceState
from lib.nexus.interface.trans.main import InterfaceTrans


class Interface(
        InterfaceBrief,
        InterfaceState,
        InterfaceTrans
        ):
    def __init__(self):
        InterfaceBrief.__init__(self)
        InterfaceState.__init__(self)
        InterfaceTrans.__init__(self)
