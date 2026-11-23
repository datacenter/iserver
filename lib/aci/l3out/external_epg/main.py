from lib.aci.l3out.external_epg.api import L3OutExternalEpgApi
from lib.aci.l3out.external_epg.info import L3OutExternalEpgInfo
from lib.aci.l3out.external_epg.delete import L3OutExternalEpgDelete
from lib.aci.l3out.external_epg.update import L3OutExternalEpgUpdate


class L3OutExternalEpg(
        L3OutExternalEpgApi,
        L3OutExternalEpgInfo,
        L3OutExternalEpgDelete,
        L3OutExternalEpgUpdate
    ):
    def __init__(self):
        L3OutExternalEpgApi.__init__(self)
        L3OutExternalEpgInfo.__init__(self)
        L3OutExternalEpgDelete.__init__(self)
        L3OutExternalEpgUpdate.__init__(self)
