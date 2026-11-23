from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.storage_item.info import StorageItemInfo


class StorageItem(IntersightCommon, StorageItemInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'storage item'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        StorageItemInfo.__init__(self)
