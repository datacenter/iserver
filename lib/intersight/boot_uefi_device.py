from lib.intersight.intersight_common import IntersightCommon


class BootUefiDevice(IntersightCommon):
    """Class for intersight boot uefi device objects
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot uefishelldevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        info = {}

        info['Moid'] = item['Moid']
        info['Name'] = item['Name']
        info['Order'] = item['Order']
        info['State'] = item['State']
        info['Type'] = item['Type']

        return info
