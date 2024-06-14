from lib.intersight.intersight_common import IntersightCommon


class SoftwareRepositoryCatalog(IntersightCommon):
    """Class for intersight software repository catalog
    {
        "AccountMoid": "",
        "Ancestors": [],
        "ClassId": "softwarerepository.Catalog",
        "CreateTime": "2019-01-18T01:41:26.956Z",
        "DomainGroupMoid": "SystemDomainGroup",
        "IsImagePullFailure": false,
        "ModTime": "2019-01-18T01:41:27.145Z",
        "Moid": "5c412ec66e6c356c358c33bf",
        "Name": "system-catalog",
        "ObjectType": "softwarerepository.Catalog",
        "Organization": null,
        "Owners": [
        "system"
        ],
        "SharedScope": "",
        "System": {
        "ClassId": "mo.MoRef",
        "Moid": "5960901ca94eba000127e32c",
        "ObjectType": "iam.System",
        "link": "https://www.intersight.com/api/v1/iam/Systems/5960901ca94eba000127e32c"
        },
        "Tags": []
    }
    """
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
