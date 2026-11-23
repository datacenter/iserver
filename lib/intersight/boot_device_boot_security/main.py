from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.boot_device_boot_security.info import BootDeviceBootSecurityInfo


class BootDeviceBootSecurity(IntersightCommon, BootDeviceBootSecurityInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot devicebootsecurity'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        BootDeviceBootSecurityInfo.__init__(self)
