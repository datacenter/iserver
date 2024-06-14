from lib.intersight.intersight_common import IntersightCommon


class HclOperatingSystemVendor(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'hcl operatingsystemvendor'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
