from lib.aci.intf.phy.stats.epg.main import InterfacePhyEpgStats
from lib.aci.intf.phy.stats.ether.main import InterfacePhyEtherStats
from lib.aci.intf.phy.stats.fc.main import InterfacePhyFcStats
from lib.aci.intf.phy.stats.qos.main import InterfacePhyQosStats
from lib.aci.intf.phy.stats.rmon.main import InterfacePhyRmonStats


class InterfacePhyStats(
    InterfacePhyEpgStats,
    InterfacePhyEtherStats,
    InterfacePhyFcStats,
    InterfacePhyQosStats,
    InterfacePhyRmonStats
    ):
    def __init__(self):
        InterfacePhyEpgStats.__init__(self)
        InterfacePhyEtherStats.__init__(self)
        InterfacePhyFcStats.__init__(self)
        InterfacePhyQosStats.__init__(self)
        InterfacePhyRmonStats.__init__(self)
