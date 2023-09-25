from lib.intersight.intersight_common import IntersightCommon


class BootIscsiDevice(IntersightCommon):
    """Class for intersight boot iscsi device objects
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot iscsidevice'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, managed_object):
        info = {}

        info['Moid'] = managed_object['Moid']
        info['Name'] = managed_object['Name']
        info['Order'] = managed_object['Order']
        info['State'] = managed_object['State']
        info['Type'] = managed_object['Type']

        return info
