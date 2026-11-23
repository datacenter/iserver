from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_uefi_device.info import BootUefiDeviceInfo


class BootUefiDevice(IntersightCommon, BootUefiDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot uefishelldevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootUefiDeviceInfo.__init__(self)
