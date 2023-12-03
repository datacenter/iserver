import traceback
import json
import yaml

from lib.intersight.intersight_common import IntersightCommon
from lib import ip_helper
from lib.intersight import software_repository_catalog
from lib.intersight import organization


class SoftwareConfigurationUtility(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'firmware serverconfigurationutilitydistributable'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.log_id = log_id
        self.my_output = None

    def get_all(self, max_errors=3, error_timeout=1):
        """Get all SCU objects

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
            list of dict: list of Intersight SCU objects
        """
        scus = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if scus is None:
            return scus

        organization_handler = organization.Organization(self.iaccount)
        organizations = organization_handler.get_moids_dict()

        verified = []
        keys = [
            'Moid',
            'Name',
            'Source',
            'SupportedModels',
            'Tags',
            'Vendor',
            'Version'
        ]

        for scu in scus:
            info = {}
            info['__Output'] = {}

            for key in keys:
                info[key] = scu[key]

            organization_id = None
            for permission in scu['PermissionResources']:
                if permission['ObjectType'] == 'organization.Organization':
                    organization_id = permission['Moid']

            if organization_id is None or organization_id not in organizations:
                # Organization ID must exist
                continue

            info['Organization'] = organizations[organization_id]

            info['Verified'] = False
            info['Link'] = None
            info['Type'] = None

            if info['Source']['ClassId'] not in ['softwarerepository.HttpServer', 'softwarerepository.NfsServer']:
                continue

            if info['Source']['ClassId'] == 'softwarerepository.HttpServer':
                info['Type'] = 'url'
                info['Link'] = scu['Source']['LocationLink']
                info['Verified'] = ip_helper.is_url_accessible(info['Link'])

                if info['Verified']:
                    info['__Output']['Link'] = 'Green'
                else:
                    info['__Output']['Link'] = 'Red'

            if info['Source']['ClassId'] == 'softwarerepository.NfsServer':
                info['Type'] = 'nfs'
                info['Link'] = scu['Source']['FileLocation']
                info['Verified'] = False

            verified.append(info)

        return verified

    def validate_add(self, scu, name_unique=True):
        """Validate SCU create attributes

        Args:
            scus (dict): scu attributes
            name_unique (bool, optional): check if Name already exists. Defaults to True.

        Expected attributes: Name, Version, Link and Organization
        Organization (name) must exist
        If name_unique, then Name cannot already exist

        Returns:
            bool: validation success
            string: if validation fails, contains information on the reason
        """
        try:
            if not isinstance(scu, dict):
                return False, 'Dict scu attributes required'

            for key in ['Name', 'Version', 'Link', 'Organization']:
                if key not in scu:
                    return False, 'Attribute %s required' % (key)

            for key in ['Name', 'Version', 'Link']:
                if len(scu[key]) == 0:
                    return False, 'Attribute value %s required' % (key)

            if name_unique:
                if self.is_name(scu['Name']):
                    return False, 'Name %s already defined' % (scu['Name'])

            if not ip_helper.is_url_valid(scu['Link']):
                return False, 'Invalid link: %s' % (scu['Link'])

            organization_handler = organization.Organization(self.iaccount)
            if organization_handler.get_by_name(scu['Organization']) is None:
                return False, 'Organization not found: %s' % (scu['Organization'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def add(self, attributes):
        """Create SCU object in Intersight

        Args:
            attributes (dict): Expected keys Name, Version, Type, Link and Organization

        The bulk of code takes attributes and formats that with the Intersight specific parameters
        SupportedModels is hard-coded
        Catalog is found based on Organization value

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        for key in ['Name', 'Version']:
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

        create_attributes = '%s --SupportedModels=ucs' % (create_attributes)

        organization_handler = organization.Organization(self.iaccount)
        organization_id = organization_handler.get_by_name(attributes['Organization'])['Moid']

        src_handler = software_repository_catalog.SoftwareRepositoryCatalog(self.iaccount)
        catalog_id = src_handler.get_user_catalog_id(organization_id)
        if catalog_id is None:
            return False

        create_attributes = '%s --Catalog=MoRef[Moid:%s]' % (create_attributes, catalog_id)

        return IntersightCommon.create(self, create_attributes)

    def get_set_output(self, scus):
        """Prepare YAML-based format from list of SCUs attributes

        Args:
            scus (list of dict): SCU objects likely returned by get_all method

        Select subset of scu object attributes that are supported by scu set operation
        - Moid, Name, Version, Type, Link

        Returns:
            string: YAML-formatted output
        """
        if scus is None:
            return None

        set_output = []
        for scu in scus:
            item = {}
            for key in ['Moid', 'Name', 'Version', 'Type', 'Link']:
                item[key] = scu[key]

            set_output.append(item)

        try:
            output = yaml.dump(
                set_output,
                default_flow_style=False
            )
        except BaseException:
            output = None

        return output

    def validate_set(self, scus):
        """Check SCU user input for set/update operation

        Args:
            scus (list of dict): User defined SCUs attributes

        Each entry in the list must have Moid key
        The rest of the fields is optional: Name, Version, Type, Link
        Organizaiton is not allowed to be updated
        Moid must exist
        Supported type: url and nfs

        Returns:
            boolean: validation successful
            string: failed validation description
        """
        try:
            ids = self.get_moids_list()
            if ids is None:
                return False, 'Exception in intersight scu check'

            if not isinstance(scus, list):
                return False, 'List of dict required'

            for scu in scus:
                if not isinstance(scu, dict):
                    return False, 'List of dict required'

                if scu['Moid'] not in ids:
                    return False, 'SCU Moid not found: %s' % (scu['Moid'])

                if 'Name' in scu and len(scu['Name']) > 0:
                    if self.is_name(scu['Name']):
                        return False, 'Name %s already defined' % (scu['Name'])

                is_link = False
                if 'Link' in scu and len(scu['Link']) > 0:
                    is_link = True

                is_type = False
                if 'Type' in scu and len(scu['Type']) > 0:
                    is_type = True

                if is_link and is_type:
                    if scu['Type'] not in ['url', 'nfs']:
                        return False, 'Unsupported type: %s' % (scu['Type'])

                    if scu['Link'].startswith('http'):
                        if not ip_helper.is_url_valid(scu['Link']):
                            return False, 'Invalid link: %s' % (scu['Link'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def update(self, moid, attributes):
        """Update SCU object in Intersight

        Args:
            moid (string): Moid of SCU object to be updated
            attributes (dict): Optional keys Name, Version, Type, Link

        Format SCU attributes with the Intersight specific parameters
        Supported Type: url and nfs

        Returns:
            bool: success or failure
        """
        update_attributes = ''
        for key in ['Name', 'Version']:
            if key in attributes and len(attributes[key]) > 0:
                value = str(attributes[key])
                if len(value.split(' ')) > 1:
                    update_attributes = '%s --%s=\'%s\'' % (update_attributes, key, value)
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
