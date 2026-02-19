from lib.intersight.intersight_common import IntersightCommon


class SoftwareRepositoryCatalog(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'softwarerepository catalog'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_user_catalog_id(self, organization_id):
        items = IntersightCommon.get_all(self)
        if items is None:
            return None

        for item in items:
            if item['Name'] == 'user-catalog' and item['Organization']['Moid'] == organization_id:
                return item['Moid']

        return None
