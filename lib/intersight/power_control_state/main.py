from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.power_control_state.info import PowerControlStateInfo


class PowerControlState(IntersightCommon, PowerControlStateInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'power controlstate'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        PowerControlStateInfo.__init__(self)
