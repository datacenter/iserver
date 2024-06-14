from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_hdd_device.info import BootHddDeviceInfo


class BootHddDevice(IntersightCommon, BootHddDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot hdddevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootHddDeviceInfo.__init__(self)
