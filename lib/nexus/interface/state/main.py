from lib.nexus.interface.state.api import InterfaceStateApi
from lib.nexus.interface.state.info import InterfaceStateInfo


class InterfaceState(
        InterfaceStateApi,
        InterfaceStateInfo
        ):
    def __init__(self):
        InterfaceStateApi.__init__(self)
        InterfaceStateInfo.__init__(self)
