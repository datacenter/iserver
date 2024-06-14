from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_usb_device.info import BootUsbDeviceInfo


class BootUsbDevice(IntersightCommon, BootUsbDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot usbdevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootUsbDeviceInfo.__init__(self)
