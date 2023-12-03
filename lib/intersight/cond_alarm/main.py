from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.cond_alarm.info import CondAlarmInfo


class CondAlarm(IntersightCommon, CondAlarmInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'cond alarm'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        CondAlarmInfo.__init__(self)
