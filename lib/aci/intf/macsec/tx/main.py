from lib.aci.intf.macsec.tx.api import InterfaceMacSecTxApi
from lib.aci.intf.macsec.tx.info import InterfaceMacSecTxInfo


class InterfaceMacSecTx(InterfaceMacSecTxApi, InterfaceMacSecTxInfo):
    def __init__(self):
        InterfaceMacSecTxApi.__init__(self)
        InterfaceMacSecTxInfo.__init__(self)
