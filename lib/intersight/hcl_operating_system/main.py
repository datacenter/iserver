from lib import output_helper
from lib.intersight.intersight_common import IntersightCommon


class HclOperatingSystem(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'hcl operatingsystem'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.set_get_expand('Vendor')
        self.my_output = None
        self.log_id = log_id

    def get_vendor_versions(self, vendor_id):
        all_versions = IntersightCommon.get_all(self)
        if all_versions is None:
            return None

        vendor_versions = []
        for version in all_versions:
            if version['Vendor']['Moid'] == vendor_id:
                vendor_versions.append(version)

        vendor_versions = sorted(
            vendor_versions,
            key=lambda i: i['Version']
        )

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

    def print(self, info, title=False):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(log_id=self.log_id)

        if title:
            self.my_output.default(
                'Intersight OS Version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Moid',
            'Version',
            'Vendor.Moid',
            'Vendor.Name',
        ]

        headers = [
            'Moid',
            'Version',
            'Vendor Moid',
            'Vendor'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
