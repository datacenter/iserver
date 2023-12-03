from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.running_firmware.info import RunningFirmwareInfo


class RunningFirmware(IntersightCommon, RunningFirmwareInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'firmware runningfirmware'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        RunningFirmwareInfo.__init__(self)
