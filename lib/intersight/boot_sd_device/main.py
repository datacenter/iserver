from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_sd_device.info import BootSdDeviceInfo


class BootSdDevice(IntersightCommon, BootSdDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot sddevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootSdDeviceInfo.__init__(self)
