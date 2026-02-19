from lib.intersight.intersight_common import IntersightCommon


class OsCatalog(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'os catalog'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_organization_catalog_id(self, organization_id):
        items = IntersightCommon.get_all(self)
        if items is None:
            return None

        for item in items:
            if item['Organization']['Moid'] == organization_id:
                return item['Moid']

        return None
