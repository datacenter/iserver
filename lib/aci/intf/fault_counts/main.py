from lib.aci.intf.fault_counts.api import InterfaceFaultCountsApi
from lib.aci.intf.fault_counts.info import InterfaceFaultCountsInfo


class InterfaceFaultCounts(InterfaceFaultCountsApi, InterfaceFaultCountsInfo):
    def __init__(self):
        InterfaceFaultCountsApi.__init__(self)
        InterfaceFaultCountsInfo.__init__(self)
