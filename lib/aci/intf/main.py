from lib.aci.intf.adjacency.main import InterfaceAdjacency
from lib.aci.intf.cloudsec.main import InterfaceCloudSec
from lib.aci.intf.encapsulated_routed.main import InterfaceEncapsulatedRouted
from lib.aci.intf.fc.main import InterfaceFc
from lib.aci.intf.fcpc.main import InterfaceFcPc
from lib.aci.intf.ip.main import InterfaceIp
from lib.aci.intf.lacp.main import InterfaceLacp
from lib.aci.intf.loopback.main import InterfaceLoopback
from lib.aci.intf.macsec.main import InterfaceMacSec
from lib.aci.intf.management.main import InterfaceMgmt
from lib.aci.intf.phy.main import InterfacePhy
from lib.aci.intf.policy.main import InterfacePolicy
from lib.aci.intf.port_channel.main import InterfacePortChannel
from lib.aci.intf.summary.main import InterfaceSummary
from lib.aci.intf.svi.main import InterfaceSvi
from lib.aci.intf.tunnel.main import InterfaceTunnel
from lib.aci.intf.vfc.main import InterfaceVfc
from lib.aci.intf.virtual_port_channel.main import InterfaceVirtualPortChannel
from lib.aci.intf.vlan.main import InterfaceVlanStats


class Interface(
    InterfaceAdjacency,
    InterfaceCloudSec,
    InterfaceEncapsulatedRouted,
    InterfaceFc,
    InterfaceFcPc,
    InterfaceIp,
    InterfaceLacp,
    InterfaceLoopback,
    InterfaceMacSec,
    InterfaceMgmt,
    InterfacePhy,
    InterfacePolicy,
    InterfacePortChannel,
    InterfaceVirtualPortChannel,
    InterfaceSummary,
    InterfaceSvi,
    InterfaceTunnel,
    InterfaceVfc,
    InterfaceVlanStats
    ):
    def __init__(self):
        InterfaceAdjacency.__init__(self)
        InterfaceCloudSec.__init__(self)
        InterfaceEncapsulatedRouted.__init__(self)
        InterfaceFc.__init__(self)
        InterfaceFcPc.__init__(self)
        InterfaceIp.__init__(self)
        InterfaceLacp.__init__(self)
        InterfaceLoopback.__init__(self)
        InterfaceMacSec.__init__(self)
        InterfaceMgmt.__init__(self)
        InterfacePhy.__init__(self)
        InterfacePolicy.__init__(self)
        InterfacePortChannel.__init__(self)
        InterfaceVirtualPortChannel.__init__(self)
        InterfaceSummary.__init__(self)
        InterfaceSvi.__init__(self)
        InterfaceTunnel.__init__(self)
        InterfaceVfc.__init__(self)
        InterfaceVlanStats.__init__(self)
