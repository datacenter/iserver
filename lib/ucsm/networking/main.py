from lib.ucsm.networking.adaptor import Adaptor
from lib.ucsm.networking.ether_server_int_fi import EtherServerIntFi
from lib.ucsm.networking.ether_server_int_fi_pc import EtherServerIntFiPc
from lib.ucsm.networking.ether_server_int_fi_pc_ep import EtherServerIntFiPcEp
from lib.ucsm.networking.ether_switch_int_fi import EtherSwitchIntFi
from lib.ucsm.networking.ether_switch_int_fi_pc import EtherSwitchIntFiPc
from lib.ucsm.networking.ether_switch_int_fi_pc_ep import EtherSwitchIntFiPcEp
from lib.ucsm.networking.eth_port import EthPort
from lib.ucsm.networking.ext_eth import ExtEth
from lib.ucsm.networking.fabric_eth_lan_pc import FabricEthLanPc
from lib.ucsm.networking.fabric_eth_lan_pc_ep import FabricEthLanPcEp
from lib.ucsm.networking.fabric_eth_vlan_pc import FabricEthVlanPc
from lib.ucsm.networking.fabric_net_group import FabricNetGroup
from lib.ucsm.networking.fabric_pooled_vlan import FabricPooledVlan
from lib.ucsm.networking.fabric_vlan import FabricVlan
from lib.ucsm.networking.host_eth import HostEth
from lib.ucsm.networking.io_card import IoCard
from lib.ucsm.networking.switch_card import SwitchCard
from lib.ucsm.networking.switch_port_group import SwitchPortGroup
from lib.ucsm.networking.vif import Vif
from lib.ucsm.networking.vlan import Vlan


class Networking(
        Adaptor,
        EtherServerIntFi,
        EtherServerIntFiPc,
        EtherServerIntFiPcEp,
        EtherSwitchIntFi,
        EtherSwitchIntFiPc,
        EtherSwitchIntFiPcEp,
        EthPort,
        ExtEth,
        FabricEthLanPc,
        FabricEthLanPcEp,
        FabricEthVlanPc,
        FabricNetGroup,
        FabricPooledVlan,
        FabricVlan,
        HostEth,
        IoCard,
        SwitchCard,
        SwitchPortGroup,
        Vif,
        Vlan
    ):
    def __init__(self):
        Adaptor.__init__(self)
        EtherServerIntFi.__init__(self)
        EtherServerIntFiPc.__init__(self)
        EtherServerIntFiPcEp.__init__(self)
        EtherSwitchIntFi.__init__(self)
        EtherSwitchIntFiPc.__init__(self)
        EtherSwitchIntFiPcEp.__init__(self)
        EthPort.__init__(self)
        ExtEth.__init__(self)
        FabricEthLanPc.__init__(self)
        FabricEthLanPcEp.__init__(self)
        FabricEthVlanPc.__init__(self)
        FabricNetGroup.__init__(self)
        FabricPooledVlan.__init__(self)
        FabricVlan.__init__(self)
        HostEth.__init__(self)
        IoCard.__init__(self)
        SwitchCard.__init__(self)
        SwitchPortGroup.__init__(self)
        Vif.__init__(self)
        Vlan.__init__(self)
