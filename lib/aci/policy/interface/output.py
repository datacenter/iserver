from lib.aci.policy.interface.auth.output import PolicyInterfaceAuthOutput
from lib.aci.policy.interface.cdp.output import PolicyInterfaceCdpOutput
from lib.aci.policy.interface.copp.output import PolicyInterfaceCoppOutput
from lib.aci.policy.interface.dpp.output import PolicyInterfaceDppOutput
from lib.aci.policy.interface.fc.output import PolicyInterfaceFcOutput
from lib.aci.policy.interface.l2.output import PolicyInterfaceL2Output
from lib.aci.policy.interface.link_flap.output import PolicyInterfaceLinkFlapOutput
from lib.aci.policy.interface.link_level.output import PolicyInterfaceLinkLevelOutput
from lib.aci.policy.interface.link_level_fc.output import PolicyInterfaceLinkLevelFcOutput
from lib.aci.policy.interface.lldp.output import PolicyInterfaceLldpOutput
from lib.aci.policy.interface.mcp.output import PolicyInterfaceMcpOutput
from lib.aci.policy.interface.pfc.output import PolicyInterfacePfcOutput
from lib.aci.policy.interface.port_channel.output import PolicyInterfacePortChannelOutput
from lib.aci.policy.interface.port_channel_member.output import PolicyInterfacePortChannelMemberOutput
from lib.aci.policy.interface.port_security.output import PolicyInterfacePortSecurityOutput
from lib.aci.policy.interface.slow_drain.output import PolicyInterfaceSlowDrainOutput
from lib.aci.policy.interface.storm_control.output import PolicyInterfaceStormControlOutput
from lib.aci.policy.interface.stp.output import PolicyInterfaceStpOutput
from lib.aci.policy.interface.synce.output import PolicyInterfaceSyncEOutput
from lib.aci.policy.interface.transceiver.output import PolicyInterfaceTransceiverOutput


class PolicyInterfaceOutput(
    PolicyInterfaceAuthOutput,
    PolicyInterfaceCdpOutput,
    PolicyInterfaceCoppOutput,
    PolicyInterfaceDppOutput,
    PolicyInterfaceFcOutput,
    PolicyInterfaceL2Output,
    PolicyInterfaceLinkFlapOutput,
    PolicyInterfaceLinkLevelOutput,
    PolicyInterfaceLinkLevelFcOutput,
    PolicyInterfaceLldpOutput,
    PolicyInterfaceMcpOutput,
    PolicyInterfacePfcOutput,
    PolicyInterfacePortChannelOutput,
    PolicyInterfacePortChannelMemberOutput,
    PolicyInterfacePortSecurityOutput,
    PolicyInterfaceSlowDrainOutput,
    PolicyInterfaceStormControlOutput,
    PolicyInterfaceStpOutput,
    PolicyInterfaceSyncEOutput,
    PolicyInterfaceTransceiverOutput
    ):
    def __init__(self):
        PolicyInterfaceAuthOutput.__init__(self)
        PolicyInterfaceCdpOutput.__init__(self)
        PolicyInterfaceCoppOutput.__init__(self)
        PolicyInterfaceDppOutput.__init__(self)
        PolicyInterfaceFcOutput.__init__(self)
        PolicyInterfaceL2Output.__init__(self)
        PolicyInterfaceLinkFlapOutput.__init__(self)
        PolicyInterfaceLinkLevelOutput.__init__(self)
        PolicyInterfaceLinkLevelFcOutput.__init__(self)
        PolicyInterfaceLldpOutput.__init__(self)
        PolicyInterfaceMcpOutput.__init__(self)
        PolicyInterfacePfcOutput.__init__(self)
        PolicyInterfacePortChannelOutput.__init__(self)
        PolicyInterfacePortChannelMemberOutput.__init__(self)
        PolicyInterfacePortSecurityOutput.__init__(self)
        PolicyInterfaceSlowDrainOutput.__init__(self)
        PolicyInterfaceStormControlOutput.__init__(self)
        PolicyInterfaceStpOutput.__init__(self)
        PolicyInterfaceSyncEOutput.__init__(self)
        PolicyInterfaceTransceiverOutput.__init__(self)