from lib.aci.intf.adjacency.output import InterfaceAdjecencyOutput
from lib.aci.intf.cloudsec.output import InterfaceCloudSecOutput
from lib.aci.intf.encapsulated_routed.output import InterfaceEncapsulatedRoutedOutput
from lib.aci.intf.fc.output import InterfaceFcOutput
from lib.aci.intf.fcpc.output import InterfaceFcPcOutput
from lib.aci.intf.lacp.output import InterfaceLacpOutput
from lib.aci.intf.loopback.output import InterfaceLoopbackOutput
from lib.aci.intf.macsec.output import InterfaceMacSecOutput
from lib.aci.intf.management.output import InterfaceMgmtOutput
from lib.aci.intf.phy.output import InterfacePhyOutput
from lib.aci.intf.port_channel.output import InterfacePortChannelOutput
from lib.aci.intf.summary.output import InterfaceSummaryOutput
from lib.aci.intf.svi.output import InterfaceSviOutput
from lib.aci.intf.tunnel.output import InterfaceTunnelOutput
from lib.aci.intf.vfc.output import InterfaceVfcOutput
from lib.aci.intf.virtual_port_channel.output import InterfaceVirtualPortChannelOutput
from lib.aci.intf.vlan.output import InterfaceVlanStatsOutput


class InterfaceOutput(
    InterfaceAdjecencyOutput,
    InterfaceCloudSecOutput,
    InterfaceEncapsulatedRoutedOutput,
    InterfaceFcOutput,
    InterfaceFcPcOutput,
    InterfaceLacpOutput,
    InterfaceLoopbackOutput,
    InterfaceMacSecOutput,
    InterfaceMgmtOutput,
    InterfacePhyOutput,
    InterfacePortChannelOutput,
    InterfaceSummaryOutput,
    InterfaceSviOutput,
    InterfaceTunnelOutput,
    InterfaceVfcOutput,
    InterfaceVirtualPortChannelOutput,
    InterfaceVlanStatsOutput
    ):
    def __init__(self):
        InterfaceAdjecencyOutput.__init__(self)
        InterfaceCloudSecOutput.__init__(self)
        InterfaceEncapsulatedRoutedOutput.__init__(self)
        InterfaceFcOutput.__init__(self)
        InterfaceFcPcOutput.__init__(self)
        InterfaceLacpOutput.__init__(self)
        InterfaceLoopbackOutput.__init__(self)
        InterfaceMacSecOutput.__init__(self)
        InterfaceMgmtOutput.__init__(self)
        InterfacePhyOutput.__init__(self)
        InterfacePortChannelOutput.__init__(self)
        InterfaceSummaryOutput.__init__(self)
        InterfaceSviOutput.__init__(self)
        InterfaceTunnelOutput.__init__(self)
        InterfaceVfcOutput.__init__(self)
        InterfaceVirtualPortChannelOutput.__init__(self)
        InterfaceVlanStatsOutput.__init__(self)
