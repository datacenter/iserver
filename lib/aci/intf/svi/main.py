from lib.aci.intf.svi.api import InterfaceSviApi
from lib.aci.intf.svi.info import InterfaceSviInfo


class InterfaceSvi(InterfaceSviApi, InterfaceSviInfo):
    def __init__(self):
        InterfaceSviApi.__init__(self)
        InterfaceSviInfo.__init__(self)
