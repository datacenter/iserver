from lib.aci.ap.node.api import ApplicationProfileNodeApi
from lib.aci.ap.node.info import ApplicationProfileNodeInfo


class ApplicationProfileNode(ApplicationProfileNodeApi, ApplicationProfileNodeInfo):
    def __init__(self):
        ApplicationProfileNodeApi.__init__(self)
        ApplicationProfileNodeInfo.__init__(self)
