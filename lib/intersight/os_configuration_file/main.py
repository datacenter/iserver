import traceback

from lib import filter_helper
from lib import output_helper

from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.organization import main as organization
from lib.intersight.os_image import main as os_image
from lib.intersight.hcl_operating_system import main as hcl_operating_system
from lib.intersight.hcl_operating_system_vendor import main as hcl_operating_system_vendor
from lib.intersight.os_catalog import main as os_catalog


class OsConfigurationFile(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'os configurationfile'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.my_output = None
        self.log_id = log_id

    def get_file_for_os(self, hcl_version_id):
        os_files = []
        items = self.get_all()
        if items is None:
            return os_files

        for item in items:
            match = False
            for distribution in item['Distributions']:
                if distribution['ObjectType'] == 'hcl.OperatingSystem' and distribution['Moid'] == hcl_version_id:
                    if item['Supported']:
                        match = True
                        break
            if match:
                os_files.append(item)

        return os_files

    def get_info(self, object_mo, vendors):
        info = {}
        info['__Output'] = {}

        keys = [
            'CreateTime',
            'Description',
            'Internal',
            'ModTime',
            'Moid',
            'FileContent',
            'Name',
            'Supported',
            'SharedScope'
        ]
        for key in keys:
            info[key] = object_mo[key]

        if info['Supported']:
            info['SupportedTick'] = '\u2713'
            info['__Output']['SupportedTick'] = 'Green'
        else:
            info['SupportedTick'] = '\u2717'
            info['__Output']['SupportedTick'] = 'Red'

        info['Placeholders'] = []
        for placeholder_mo in object_mo['Placeholders']:
            info['Placeholders'].append(
                placeholder_mo['Type']['Label']
            )

        info['Distributions'] = []
        for distribution_mo in object_mo['Distributions']:
            distribution_info = {}

            distribution_info['OsMoid'] = None
            distribution_info['VendorMoid'] = None
            if distribution_mo['ObjectType'] == 'hcl.OperatingSystem':
                distribution_info['OsMoid'] = distribution_mo['Moid']
                if 'Parent' in distribution_mo:
                    distribution_info['VendorMoid'] = distribution_mo['Parent']['Moid']

            distribution_info['Version'] = ''
            distribution_info['VersionId'] = None
            if 'Version' in distribution_mo:
                distribution_info['Version'] = distribution_mo['Version']
                distribution_info['VersionId'] = distribution_mo['Moid']

            distribution_info['Vendor'] = ''
            distribution_info['VendorId'] = None
            if 'Vendor' in distribution_mo:
                for vendor in vendors:
                    if vendor['Moid'] == distribution_mo['Vendor']['Moid']:
                        distribution_info['Vendor'] = vendor['Name']
                        distribution_info['VendorId'] = vendor['Moid']

            info['Distributions'].append(
                distribution_info
            )

        return info

    def get_infos(self, vendors, moid_filter=None, name_filter=None, vendor_filter=None, version_filter=None, expand=True):
        if expand:
            self.set_get_expand(
                'Distributions'
            )

        infos = []
        object_mos = self.get_all()
        if object_mos is None:
            return infos

        for object_mo in object_mos:
            info = self.get_info(
                object_mo,
                vendors
            )

            if moid_filter is not None:
                if not filter_helper.match_string(moid_filter, info['Moid']):
                    continue

            if name_filter is not None:
                if not filter_helper.match_string(name_filter, info['Name']):
                    continue

            if vendor_filter is not None:
                found = False
                for distribution_name in info['Distributions']:
                    if filter_helper.match_string(vendor_filter, distribution_name['Vendor']):
                        found = True

                if not found:
                    continue

            if version_filter is not None:
                found = False
                for distribution_name in info['Distributions']:
                    if filter_helper.match_string(version_filter, distribution_name['Version']):
                        found = True

                if not found:
                    continue

            infos.append(
                info
            )

        infos = sorted(
            infos,
            key=lambda i: i['Name']
        )

        return infos

    def validate_add(self, os_config, name_unique=True):
        try:
            if not isinstance(os_config, dict):
                return False, 'Dict os_config attributes required'

            for key in ['Name', 'FileContent', 'Organization', 'OsImageName']:
                if key not in os_config:
                    return False, 'Attribute %s required' % (key)

            image_handler = os_image.OsImage(self.iaccount)
            image_mo = image_handler.get_by_name(os_config['OsImageName'])
            if image_mo is None:
                return False, 'Invalid OS name: %s' % (os_config['OsImageName'])

            os_vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(self.iaccount)
            os_vendor_mo = os_vendor_handler.get_by_name(
                image_mo['Vendor']
            )
            if os_vendor_mo is None:
                return False, 'Invalid OS name vendor reference: %s' % (os_config['OsImageName'])

            os_handler = hcl_operating_system.HclOperatingSystem(self.iaccount)
            os_mo = os_handler.get_vendor_version(
                os_vendor_mo['Moid'],
                image_mo['Version']
            )
            if os_mo is None:
                return False, 'Invalid OS name version reference: %s' % (os_config['OsImageName'])

            organization_handler = organization.Organization(self.iaccount)
            if organization_handler.get_by_name(os_config['Organization']) is None:
                return False, 'Organization not found: %s' % (os_config['Organization'])

            if name_unique:
                if self.is_name(os_config['Name']):
                    return False, 'Name %s already defined' % (os_config['Name'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def add(self, attributes):
        create_attributes = ''
        for key in ['Name']:
            value = str(attributes[key])
            if len(value.split(' ')) > 1:
                create_attributes = '%s --%s=\'%s\'' % (create_attributes, key, value)
            else:
                create_attributes = '%s --%s=%s' % (create_attributes, key, value)

        file_content = '\\r\\n'.join(attributes['FileContent'].split('\n'))
        create_attributes = '%s --%s=\'%s\'' % (create_attributes, 'FileContent', file_content)

        if attributes['Internal']:
            create_attributes = '%s --Internal' % (create_attributes)

        image_handler = os_image.OsImage(self.iaccount)
        image_mo = image_handler.get_by_name(attributes['OsImageName'])
        if image_mo is None:
            return False

        os_vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(self.iaccount)
        os_vendor_mo = os_vendor_handler.get_by_name(
            image_mo['Vendor']
        )
        if os_vendor_mo is None:
            return False

        os_handler = hcl_operating_system.HclOperatingSystem(self.iaccount)
        os_mo = os_handler.get_vendor_version(
            os_vendor_mo['Moid'],
            image_mo['Version']
        )
        if os_mo is None:
            return False

        distributions = '["MoRef:hcl.OperatingSystem[Moid:%s]"]' % (os_mo['Moid'])
        create_attributes = '%s --%s=%s' % (create_attributes, 'Distributions', distributions)

        organization_handler = organization.Organization(self.iaccount)
        organization_id = organization_handler.get_by_name(attributes['Organization'])['Moid']

        src_handler = os_catalog.OsCatalog(self.iaccount)
        catalog_id = src_handler.get_organization_catalog_id(organization_id)
        if catalog_id is None:
            return False

        create_attributes = '%s --Catalog=MoRef[Moid:%s]' % (create_attributes, catalog_id)

        return IntersightCommon.create(self, create_attributes)

    def print(self, info, title=False, show_content=False):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(log_id=self.log_id)

        if title:
            self.my_output.default(
                'Intersight OS Configuration Files [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return
            return

        order = [
            'Moid',
            'Name',
            'Distributions.Vendor',
            'Distributions.Version',
            'Placeholders',
            'SupportedTick'
        ]

        headers = [
            'Moid',
            'Name',
            'Vendor',
            'Version',
            'Placeholders',
            'Supported'
        ]

        if show_content:
            for item in info:
                self.my_output.my_table(
                    self.my_output.expand_lists(
                        [item],
                        order,
                        ['Distributions', 'Placeholders']
                    ),
                    order=order,
                    headers=headers,
                    remove_empty_columns=False,
                    allow_order_subkeys=True,
                    row_separator=True,
                    underline=True,
                    table=True
                )

                self.my_output.default(
                    item['FileContent'],
                    before_newline=True,
                    after_newline=True
                )

        else:
            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['Distributions', 'Placeholders']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=False,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )
