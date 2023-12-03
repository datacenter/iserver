from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.chassis_profile.info import ChassisProfileInfo


class ChassisProfile(IntersightCommon, ChassisProfileInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'chassis profile'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        ChassisProfileInfo.__init__(self)
