from lib.aci.intf.macsec.rx.api import InterfaceMacSecRxApi
from lib.aci.intf.macsec.rx.info import InterfaceMacSecRxInfo


class InterfaceMacSecRx(InterfaceMacSecRxApi, InterfaceMacSecRxInfo):
    def __init__(self):
        InterfaceMacSecRxApi.__init__(self)
        InterfaceMacSecRxInfo.__init__(self)
