from lib.aci.intf.vfc.api import InterfaceVfcApi
from lib.aci.intf.vfc.info import InterfaceVfcInfo


class InterfaceVfc(InterfaceVfcApi, InterfaceVfcInfo):
    def __init__(self):
        InterfaceVfcApi.__init__(self)
        InterfaceVfcInfo.__init__(self)
