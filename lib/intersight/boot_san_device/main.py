from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_san_device.info import BootSanDeviceInfo


class BootSanDevice(IntersightCommon, BootSanDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot sandevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootSanDeviceInfo.__init__(self)
