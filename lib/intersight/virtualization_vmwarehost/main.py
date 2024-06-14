from lib.intersight.intersight_common import IntersightCommon


class VirtualizationVmwareHost(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'virtualization vmwarehost'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
