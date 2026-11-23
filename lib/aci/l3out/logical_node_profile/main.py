from lib.aci.l3out.logical_node_profile.api import L3OutLogicalNodeProfileApi
from lib.aci.l3out.logical_node_profile.info import L3OutLogicalNodeProfileInfo


class L3OutLogicalNodeProfile(L3OutLogicalNodeProfileApi, L3OutLogicalNodeProfileInfo):
    def __init__(self):
        L3OutLogicalNodeProfileApi.__init__(self)
        L3OutLogicalNodeProfileInfo.__init__(self)
