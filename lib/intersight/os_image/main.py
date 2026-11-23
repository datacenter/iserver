import json
import traceback
import yaml

from lib.intersight.intersight_common import IntersightCommon
from lib import ip_helper
from lib import output_helper
from lib.intersight.organization import main as organization
from lib.intersight.hcl_operating_system_vendor import main as hcl_operating_system_vendor
from lib.intersight.hcl_operating_system import main as hcl_operating_system
from lib.intersight.software_repository_catalog import main as software_repository_catalog


class OsImage(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'softwarerepository operatingsystemfile'
        self.hcl_os_vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=log_id)
        self.hcl_os_version_handler = hcl_operating_system.HclOperatingSystem(iaccount, log_id=log_id)

        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.log_id = log_id
        self.my_output = None

    def get_all(self, max_errors=3, error_timeout=1):
        """Get all OS image objects

        Args:
            max_errors (int, optional): if API call fails retry until max_errors. Defaults to 3.
            error_timeout (int, optional): if API response takes longer than error_timeout, then consider API as failed. Defaults to 1.

        Extend the raw get API call with custom attributes
        - Organization: organization name
        - Type: url, nfs
        - Link: normalized location
        - Verified: check if url is reachable. not supported for nfs type

        Note: cfs type not supported

        Returns:
            list of dict: list of Intersight OS image objects
        """
        images = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if images is None:
            return images

        organization_handler = organization.Organization(self.iaccount)
        organizations = organization_handler.get_moids_dict()

        verified = []

        keys = [
            'Moid',
            'Name',
            'Source',
            'Tags',
            'Vendor',
            'Version'
        ]

        for image in images:
            info = {}
            info['__Output'] = {}

            for key in keys:
                info[key] = image[key]

            organization_id = None
            for permission in image['PermissionResources']:
                if permission['ObjectType'] == 'organization.Organization':
                    organization_id = permission['Moid']

            if organization_id is None or organization_id not in organizations:
                # Organization ID must exist
                continue

            info['Organization'] = organizations[organization_id]
            info['Verified'] = False
            info['Type'] = None
            info['Link'] = None

            if info['Source']['ClassId'] not in ['softwarerepository.HttpServer', 'softwarerepository.NfsServer']:
                continue

            if info['Source']['ClassId'] == 'softwarerepository.HttpServer':
                info['Type'] = 'url'
                info['Link'] = image['Source']['LocationLink']
                info['Verified'] = ip_helper.is_url_accessible(info['Link'])

                if info['Verified']:
                    info['__Output']['Link'] = 'Green'
                else:
                    info['__Output']['Link'] = 'Red'

            if info['Source']['ClassId'] == 'softwarerepository.NfsServer':
                info['Type'] = 'nfs'
                info['Link'] = image['Source']['FileLocation']
                info['Verified'] = False

            verified.append(info)

        return verified

    def validate_add(self, image, name_unique=True):
        """Validate os image create attributes

        Args:
            image (dict): image attributes
            name_unique (bool, optional): check if Name already exists. Defaults to True.

        Expected attributes: Name, Vendor, Version, Link and Organization
        Vendor and Version must be defined in HCL catalog
        Organization (name) must exist
        If name_unique, then Name cannot already exist

        Returns:
            bool: validation success
            string: if validation fails, contains information on the reason
        """
        try:
            if not isinstance(image, dict):
                return False, 'Dict image attributes required'

            for key in ['Name', 'Vendor', 'Version', 'Link', 'Organization']:
                if key not in image:
                    return False, 'Attribute %s required' % (key)

            if image['Vendor'] == '':
                return False, 'Define vendor'

            vendor_attributes = self.hcl_os_vendor_handler.get_by_name(image['Vendor'])
            if vendor_attributes is None:
                return False, 'Vendor not found: %s' % (image['Vendor'])
            vendor_id = vendor_attributes['Moid']

            if image['Version'] == '':
                return False, 'Define version'

            if not self.hcl_os_version_handler.is_vendor_version(vendor_id, image['Version']):
                return False, 'Invalid version for vendor: %s' % (image['Version'])

            organization_handler = organization.Organization(self.iaccount)
            if organization_handler.get_by_name(image['Organization']) is None:
                return False, 'Organization not found: %s' % (image['Organization'])

            if name_unique:
                if self.is_name(image['Name']):
                    return False, 'Name %s already defined' % (image['Name'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def add(self, attributes):
        """Create os image object in Intersight

        Args:
            attributes (dict): Expected keys Name, Vendor, Version, Type, Link and Organization

        The bulk of code takes attributes and formats that with the Intersight specific parameters
        Catalog is found based on Organization value

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        for key in ['Name', 'Vendor', 'Version']:
            value = str(attributes[key])
            if len(value.split(' ')) > 1:
                create_attributes = '%s --%s=\'%s\'' % (create_attributes, key, value)
            else:
                create_attributes = '%s --%s=%s' % (create_attributes, key, value)

        if attributes['Type'] not in ['url', 'nfs']:
            return False

        if attributes['Type'] == 'url':
            source = {}
            source['ClassId'] = 'softwarerepository.HttpServer'
            source['LocationLink'] = attributes['Link']
            source['ObjectType'] = 'softwarerepository.HttpServer'
            create_attributes = '%s --%s=\'%s\'' % (create_attributes, 'Source', json.dumps(source))

        if attributes['Type'] == 'nfs':
            source = {}
            source['ClassId'] = 'softwarerepository.NfsServer'
            source['FileLocation'] = attributes['Link']
            source['ObjectType'] = 'softwarerepository.NfsServer'
            create_attributes = '%s --%s=\'%s\'' % (create_attributes, 'Source', json.dumps(source))

        organization_handler = organization.Organization(self.iaccount)
        organization_id = organization_handler.get_by_name(attributes['Organization'])['Moid']

        src_handler = software_repository_catalog.SoftwareRepositoryCatalog(self.iaccount)
        catalog_id = src_handler.get_user_catalog_id(organization_id)
        if catalog_id is None:
            return False

        create_attributes = '%s --Catalog=MoRef[Moid:%s]' % (create_attributes, catalog_id)

        return IntersightCommon.create(self, create_attributes)

    def get_set_output(self, images):
        """Prepare YAML-based format from list of os image attributes

        Args:
            images (list of dict): Os image objects likely returned by get_all method

        Select subset of image object attributes that are supported by set operation
        - Moid, Name, Vendor, Version, Type, Link

        Returns:
            string: YAML-formatted output
        """
        if images is None:
            return None

        set_output = []
        for image in images:
            item = {}
            for key in ['Moid', 'Name', 'Vendor', 'Version', 'Type', 'Link']:
                item[key] = image[key]

            set_output.append(item)

        try:
            output = yaml.dump(
                set_output,
                default_flow_style=False
            )
        except BaseException:
            output = None

        return output

    def validate_set(self, images):
        """Check os image user input for set/update operation

        Args:
            images (list of dict): User defined os image attributes

        Each entry in the list must have keys: ...

        Returns:
            boolean: validation successful
            string: failed validation description
        """
        try:
            ids = self.get_moids_list()
            if ids is None:
                return False, 'Exception in intersight os image check'

            if not isinstance(images, list):
                return False, 'List required'

            for image in images:
                if not isinstance(image, dict):
                    return False, 'List of dict required'

                if image['Moid'] not in ids:
                    return False, 'SCU Moid not found: %s' % (image['Moid'])

                if 'Name' in image and len(image['Name']) > 0:
                    if self.is_name(image['Name']):
                        return False, 'Name %s already defined' % (image['Name'])

                is_link = False
                if 'Link' in image and len(image['Link']) > 0:
                    is_link = True

                is_type = False
                if 'Type' in image and len(image['Type']) > 0:
                    is_type = True

                if is_link and is_type:
                    if image['Type'] not in ['url', 'nfs']:
                        return False, 'Unsupported type: %s' % (image['Type'])

                    if image['Link'].startswith('http'):
                        if not ip_helper.is_url_valid(image['Link']):
                            return False, 'Invalid link: %s' % (image['Link'])

                is_vendor = False
                if 'Vendor' in image and len(image['Vendor']) > 0:
                    is_vendor = True

                is_version = False
                if 'Version' in image and len(image['Version']) > 0:
                    is_version = True

                if is_vendor and is_version:
                    vendor_attributes = self.hcl_os_vendor_handler.get_by_name(image['Vendor'])
                    if vendor_attributes is None:
                        return False, 'Vendor not found: %s' % (image['Vendor'])
                    vendor_id = vendor_attributes['Moid']

                    if image['Version'] == '':
                        return False, 'Define version'

                    if not self.hcl_os_version_handler.is_vendor_version(vendor_id, image['Version']):
                        return False, 'Invalid version for vendor: %s' % (image['Version'])
                else:
                    if not is_vendor and not is_version:
                        pass
                    else:
                        return False, 'Define both vendor and version'

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def update(self, moid, attributes):
        """Update OS image object in Intersight

        Args:
            moid (string): Moid of os image object to be updated
            attributes (dict): Expected keys Name, Vendor, Version, Type, Link

        Format image attributes with the Intersight specific parameters
        Supported Type: url and nfs

        Returns:
            bool: success or failure
        """
        update_attributes = ''
        for key in ['Name', 'Vendor', 'Version']:
            if key in attributes and len(attributes[key]) > 0:
                value = str(attributes[key])
                if len(value.split(' ')) > 1:
                    update_attributes = '%s --%s=\"%s\"' % (update_attributes, key, value)
                else:
                    update_attributes = '%s --%s=%s' % (update_attributes, key, value)

        is_link = False
        if 'Link' in attributes and len(attributes['Link']) > 0:
            is_link = True

        is_type = False
        if 'Type' in attributes and len(attributes['Type']) > 0:
            is_type = True

        if is_link and is_type:
            if attributes['Type'] == 'url':
                source = {}
                source['ClassId'] = 'softwarerepository.HttpServer'
                source['LocationLink'] = attributes['Link']
                source['ObjectType'] = 'softwarerepository.HttpServer'
                update_attributes = '%s --%s=\'%s\'' % (update_attributes, 'Source', json.dumps(source))

            if attributes['Type'] == 'nfs':
                source = {}
                source['ClassId'] = 'softwarerepository.NfsServer'
                source['FileLocation'] = attributes['Link']
                source['ObjectType'] = 'softwarerepository.NfsServer'
                update_attributes = '%s --%s=\'%s\'' % (update_attributes, 'Source', json.dumps(source))

        return IntersightCommon.update(self, moid, update_attributes)

    def print(self, info, title=False):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(log_id=self.log_id)

        if title:
            self.my_output.default(
                'Intersight OS Images [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name',
            'Vendor',
            'Version',
            'Link'
        ]

        headers = [
            'Name',
            'Vendor',
            'Version',
            'Link'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
