from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_device_boot_mode.info import BootDeviceBootModeInfo


class BootDeviceBootMode(IntersightCommon, BootDeviceBootModeInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot devicebootmode'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootDeviceBootModeInfo.__init__(self)
