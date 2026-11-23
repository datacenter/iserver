from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.management_interface.info import ManagementInterfaceInfo


class ManagementInterface(IntersightCommon, ManagementInterfaceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'management interface'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        ManagementInterfaceInfo.__init__(self)
