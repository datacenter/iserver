from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_nvme_device.info import BootNvmeDeviceInfo


class BootNvmeDevice(IntersightCommon, BootNvmeDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot nvmedevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootNvmeDeviceInfo.__init__(self)
