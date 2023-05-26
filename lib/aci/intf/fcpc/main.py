from lib.aci.intf.fcpc.api import InterfaceFcPcApi
from lib.aci.intf.fcpc.info import InterfaceFcPcInfo


class InterfaceFcPc(InterfaceFcPcApi, InterfaceFcPcInfo):
    def __init__(self):
        InterfaceFcPcApi.__init__(self)
        InterfaceFcPcInfo.__init__(self)
