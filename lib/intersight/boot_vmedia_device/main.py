from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_vmedia_device.info import BootVmediaDeviceInfo


class BootVmediaDevice(IntersightCommon, BootVmediaDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot vmediadevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootVmediaDeviceInfo.__init__(self)
