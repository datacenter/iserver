from lib.intersight.intersight_common import IntersightCommon
from lib.intersight import hcl_operating_system_vendor


class HclOperatingSystem(IntersightCommon):
    """Class for intersight hcl operating system objects

    {
        "AccountMoid": "",
        "Ancestors": [],
        "ClassId": "hcl.OperatingSystem",
        "CreateTime": "2019-02-08T01:20:11.049Z",
        "DomainGroupMoid": "SystemDomainGroup",
        "ModTime": "2019-02-08T01:20:11.053Z",
        "Moid": "5c5cd94b3535383637d7b0b4",
        "ObjectType": "hcl.OperatingSystem",
        "Owners": [
            "system"
        ],
        "SharedScope": "",
        "Tags": [],
        "Vendor": {
            "ClassId": "mo.MoRef",
            "Moid": "5b7370f16836726e35cc7025",
            "ObjectType": "hcl.OperatingSystemVendor",
            "link": "https://www.intersight.com/api/v1/hcl/OperatingSystemVendors/5b7370f16836726e35cc7025"
        },
        "Version": "CentOS 7.6"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'hcl operatingsystem'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.log_id = log_id

    def get_vendor_versions(self, vendor_id):
        all_versions = IntersightCommon.get_all(self)
        if all_versions is None:
            return None

        vendor_versions = []
        for version in all_versions:
            if version['Vendor']['Moid'] == vendor_id:
                vendor_versions.append(version)

        return vendor_versions

    def get_vendor_version_id(self, vendor_id, version_name):
        version = self.get_vendor_version(vendor_id, version_name)
        if version is not None:
            return version['Moid']
        return None

    def get_vendor_version(self, vendor_id, version_name):
        all_versions = IntersightCommon.get_all(self)
        if all_versions is None:
            return None

        for version in all_versions:
            if version['Vendor']['Moid'] == vendor_id:
                if version['Version'] == version_name:
                    return version

        return None

    def is_vendor_version(self, vendor_id, version_name):
        if self.get_vendor_version(vendor_id, version_name) is None:
            return False
        return True
