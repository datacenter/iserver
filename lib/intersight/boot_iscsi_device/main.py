from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_iscsi_device.info import BootIscsiDeviceInfo


class BootIscsiDevice(IntersightCommon, BootIscsiDeviceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot iscsidevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootIscsiDeviceInfo.__init__(self)
