from lib.aci.path.api import FabricPathApi
from lib.aci.path.info import FabricPathInfo


class FabricPath(FabricPathApi, FabricPathInfo):
    def __init__(self):
        FabricPathApi.__init__(self)
        FabricPathInfo.__init__(self)
