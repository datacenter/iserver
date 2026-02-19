from lib.md.nexus.interface.eth import MdNexusInterfaceEthOutput
from lib.md.nexus.interface.pc import MdNexusInterfacePcOutput
from lib.md.nexus.interface.vlan import MdNexusInterfaceVlanOutput


class MdNexusInterfaceOutput(
        MdNexusInterfaceEthOutput,
        MdNexusInterfacePcOutput,
        MdNexusInterfaceVlanOutput
    ):
    def __init__(self):
        MdNexusInterfaceEthOutput.__init__(self)
        MdNexusInterfacePcOutput.__init__(self)
        MdNexusInterfaceVlanOutput.__init__(self)
