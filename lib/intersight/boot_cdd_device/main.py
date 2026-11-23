from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_cdd_device.info import BootCddDeviceInfo


class BootCddDevice(IntersightCommon, BootCddDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot cdddevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootCddDeviceInfo.__init__(self)
