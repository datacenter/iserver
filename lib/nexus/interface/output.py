from lib.nexus.interface.brief.output import InterfaceBriefOutput
from lib.nexus.interface.state.output import InterfaceStateOutput
from lib.nexus.interface.trans.output import InterfaceTransOutput

class InterfaceOutput(
        InterfaceBriefOutput,
        InterfaceStateOutput,
        InterfaceTransOutput
    ):
    def __init__(self):
        InterfaceBriefOutput.__init__(self)
        InterfaceStateOutput.__init__(self)
        InterfaceTransOutput.__init__(self)
