from lib.nso.cnfm.plan.api import NsoCnfmPlanApi
from lib.nso.cnfm.plan.info import NsoCnfmPlanInfo


class NsoCnfmPlan(
        NsoCnfmPlanApi,
        NsoCnfmPlanInfo
        ):
    def __init__(self):
        NsoCnfmPlanApi.__init__(self)
        NsoCnfmPlanInfo.__init__(self)
