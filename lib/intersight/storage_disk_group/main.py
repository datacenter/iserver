from lib.intersight.intersight_common import IntersightCommon


class StorageDiskGroup(IntersightCommon):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'storage diskgroup'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
