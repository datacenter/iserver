from lib.intersight.intersight_common import IntersightCommon
from lib.intersight import hcl_operating_system_vendor


class HclOperatingSystem(IntersightCommon):
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
