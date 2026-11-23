from lib.aci.policy.general.output import PolicyGeneralOutput
from lib.aci.policy.interface.output import PolicyInterfaceOutput
from lib.aci.policy.snoop.output import PolicySnoopOutput


class PolicyOutput(PolicyGeneralOutput, PolicyInterfaceOutput, PolicySnoopOutput):
    def __init__(self):
        PolicyGeneralOutput.__init__(self)
        PolicyInterfaceOutput.__init__(self)
        PolicySnoopOutput.__init__(self)
