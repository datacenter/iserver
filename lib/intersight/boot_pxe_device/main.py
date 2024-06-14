from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_pxe_device.info import BootPxeDeviceInfo


class BootPxeDevice(IntersightCommon, BootPxeDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot pxedevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootPxeDeviceInfo.__init__(self)
