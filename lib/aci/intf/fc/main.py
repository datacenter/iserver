from lib.aci.intf.fc.api import InterfaceFcApi
from lib.aci.intf.fc.info import InterfaceFcInfo


class InterfaceFc(InterfaceFcApi, InterfaceFcInfo):
    def __init__(self):
        InterfaceFcApi.__init__(self)
        InterfaceFcInfo.__init__(self)
