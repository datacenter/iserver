from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.bios_boot_mode.info import BiosBootModeInfo


class BiosBootMode(IntersightCommon, BiosBootModeInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'bios bootmode'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BiosBootModeInfo.__init__(self)
