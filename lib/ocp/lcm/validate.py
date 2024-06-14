import os
import json

from lib import file_helper
from lib import ip_helper


class OcpValidate():
    def __init__(self):
        self.ocp_type = None
        self.ocp_user_input_location = None
        self.ocp_user_input = None
        self.ocp_token_filename = None
        self.vcenter_credentials = None

    def set_ocp_type(self):
        try:
            installation_method = str(self.ocp_user_input['ocp']['installation'])
        except BaseException:
            self.my_output.error('ocp.installation property required')
            self.my_output.debug(json.dumps(self.ocp_user_input, indent=4))
            return False

        supported_methods = ['vsphere-ipi', 'bm-ipi']
        if installation_method not in supported_methods:
            self.my_output.error('Unsupported ocp.installation value: %s' % (installation_method))
            self.my_output.default('Supported values')
            for supported_method in supported_methods:
                self.my_output.default('- %s' % (supported_method))
            return False

        self.ocp_type = installation_method
        return True

    def set_ocp_user_input(self, ocp_definition_location):
        self.ocp_user_input_location = ocp_definition_location
        if not os.path.isfile(ocp_definition_location) and not os.path.isdir(ocp_definition_location):
            self.my_output.error('Specify valid location of OCP configuration')
            return False

        token_filename = os.path.join(ocp_definition_location, 'secret')
        token_filename = os.path.join(token_filename, 'pull-secret.txt')
        if not os.path.isfile(token_filename):
            self.my_output.error('Specify valid OCP secret file: %s' % (token_filename))
            return False

        self.ocp_token_filename = token_filename

        vcenter_filename = os.path.join(ocp_definition_location, 'secret')
        vcenter_filename = os.path.join(vcenter_filename, 'vcenter.yaml')
        if not os.path.isfile(vcenter_filename):
            self.my_output.error('Specify valid vcenter credentials file: %s' % (vcenter_filename))
            return False

        self.vcenter_credentials = file_helper.get_file_yaml(vcenter_filename)
        if self.vcenter_credentials is None:
            self.my_output.error('Specify valid vcenter credentials file: %s' % (vcenter_filename))
            return False

        if 'username' not in self.vcenter_credentials or 'password' not in self.vcenter_credentials:
            self.my_output.error('Specify valid vcenter credentials file: %s' % (vcenter_filename))
            return False

        self.ocp_user_input = self.get_input(ocp_definition_location)
        if self.ocp_user_input is None:
            return False

        if not self.set_ocp_type():
            return False

        self.my_output.debug('User input: %s' % (json.dumps(self.ocp_user_input, indent=4)))
        return True

    def get_token(self, filename):
        if not os.path.isfile(filename):
            self.my_output.error('File %s not found' % (filename))
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = file_handler.readlines()

        except BaseException:
            self.my_output.error('File read exception: %s' % (filename))
            return None

        return content

    def get_input(self, location):
        if os.path.isfile(location):
            content = file_helper.get_file_yaml(location)
            if content is None:
                self.log.error(
                    'get_input',
                    'File read failed: %s' % (location)
                )
                return None

            return content

        content = {}
        for filename in os.listdir(location):
            content_filename = os.path.join(location, filename)
            if os.path.isdir(content_filename):
                continue

            part = file_helper.get_file_yaml(
                content_filename
            )
            if part is None:
                continue

            for key in part:
                if key in content:
                    self.my_output.error('Sections have to be defined in single file: %s' % (key))
                    return None

                content[key] = part[key]

        return content

    def get_section_rules(self, section_name):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            self.my_output.error('Failed to get module location')
            return None

        templates_dir = os.path.join(main_dir, 'templates')
        ocp_templates_dir = os.path.join(templates_dir, 'ocp')
        installation_method_dir = os.path.join(ocp_templates_dir, self.ocp_type)
        rules_dir = os.path.join(installation_method_dir, 'rules')
        rules_filename = os.path.join(rules_dir, '%s.yaml' % (section_name))
        return file_helper.get_file_yaml(rules_filename)

    def is_key_in_section(self, key, section):
        try:
            value = None
            for field in key.split('.'):
                if value is None:
                    value = section[field]
                    continue

                value = value[field]

        except BaseException:
            return False

        return True

    def get_key_value(self, key, section):
        try:
            value = None
            for field in key.split('.'):
                if value is None:
                    value = section[field]
                    continue

                value = value[field]

        except BaseException:
            return None

        return value

    def add_key_value(self, section, key, value):
        try:
            if len(key.split('.')) == 1:
                section[key] = value
                return section

            subsection = None
            for subdict in key.split('.')[:-1]:
                if subsection is None:
                    if subdict not in section:
                        section[subdict] = {}
                    subsection = section[subdict]
                    continue

                if subdict not in subsection:
                    subsection[subdict] = {}
                subsection = subsection[subdict]

            subsection[key.split('.')[-1]] = value

        except BaseException:
            return None

        return section

    def validate_key_value(self, section_name, key, rules, value):
        attribute_name = '%s.%s' % (section_name, key)

        if rules['type'] not in ['str', 'int', 'bool', 'list_of_ip', 'list_of_str']:
            self.my_output.error('Unsupported attribute type: %s' % (rules['type']))
            self.my_output.default('Section: %s' % (section_name))
            self.my_output.default('Key: %s' % (key))
            self.my_output.default('Rules: %s' % (rules))
            self.my_output.default('Value: %s' % (value))
            return False, None

        if rules['type'] == 'str':
            if value is None and rules['check'] == 'local-file-null-accepted':
                pass
            else:
                if not isinstance(value, str):
                    self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                    return False, None

        if rules['type'] == 'int':
            if not isinstance(value, int):
                self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                return False, None

        if rules['type'] == 'bool':
            if not isinstance(value, bool):
                self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                return False, None

        if rules['type'] == 'list_of_ip':
            if not isinstance(value, list):
                self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                return False, None

            for item in value:
                if not ip_helper.is_valid_ipv4_address(item):
                    self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                    return False, None

        if rules['type'] == 'list_of_ip':
            if not isinstance(value, list):
                self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                return False, None

            for item in value:
                if not isinstance(item, str):
                    self.my_output.error('Expected attribute %s type is %s' % (attribute_name, rules['type']))
                    return False, None

        if rules['check'] is not None:
            if rules['type'] == 'bool':
                if rules['check'] == 'must-be-true':
                    if not value:
                        self.my_output.error('Expected attribute %s value is True: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'must-be-false':
                    if value:
                        self.my_output.error('Expected attribute %s value is False: %s' % (attribute_name, value))
                        return False, None
                    return True, value

            if rules['type'] == 'str':
                if rules['check'] == 'ipv4':
                    if not ip_helper.is_valid_ipv4_address(value):
                        self.my_output.error('Expected attribute %s value is valid IPv4 address: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'ipv4s':
                    for item in value.split(','):
                        if not ip_helper.is_valid_ipv4_address(item):
                            self.my_output.error('Expected attribute %s value is list of valid IPv4 addresses: %s' % (attribute_name, value))
                            return False, None
                    return True, value

                if rules['check'] == 'ipv6':
                    if not ip_helper.is_valid_ipv6_address(value):
                        self.my_output.error('Expected attribute %s value is valid IPv6 address: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'cidrv4':
                    if not ip_helper.is_valid_ipv4_cidr(value):
                        self.my_output.error('Expected attribute %s value is valid IPv4 CIDR: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'cidrv6':
                    if not ip_helper.is_valid_ipv6_cidr(value):
                        self.my_output.error('Expected attribute %s value is valid IPv6 CIDR: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'url':
                    if not ip_helper.is_url_valid(value):
                        self.my_output.error('Expected attribute %s value is valid URL: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'dhcp-v4-range':
                    if len(value.split('-')) != 2:
                        self.my_output.error('Expected attribute %s value is valid IPv4 address ranges: %s' % (attribute_name, value))
                        return False, None

                    (start_ip, end_ip) = value.split('-')
                    if not ip_helper.is_valid_ipv4_address(start_ip) or not ip_helper.is_valid_ipv4_address(end_ip):
                        self.my_output.error('Expected attribute %s value is valid IPv4 address ranges: %s' % (attribute_name, value))
                        return False, None

                    return True, value

                if rules['check'] == 'not-empty-no-spaces':
                    if value is None:
                        value = ''
                    value = value.strip()

                    if len(value) == 0:
                        self.my_output.error('Expected attribute %s value is non-empty string without spaces: %s' % (attribute_name, value))
                        return False, None

                    if ' ' in value:
                        self.my_output.error('Expected attribute %s value is non-empty string without spaces: %s' % (attribute_name, value))
                        return False, None

                    return True, value

                if rules['check'] == 'not-empty':
                    if value is None:
                        value = ''
                    value = value.strip()

                    if len(value) == 0:
                        self.my_output.error('Expected attribute %s value is non-empty string: %s' % (attribute_name, value))
                        return False, None

                    return True, value

                if rules['check'].startswith('values:'):
                    reference_values = rules['check'].lstrip('values').lstrip(':')
                    if value not in reference_values.split(','):
                        self.my_output.error('Expected attribute %s value is one of %s: %s' % (attribute_name, reference_values, value))
                        return False, None
                    return True, value

                if rules['check'] == 'local-file':
                    if not os.path.isfile(value):
                        self.my_output.error('Expected attribute %s value is existing local file: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'local-file-null-accepted':
                    if value is None:
                        return True, None

                    if len(value) == 0:
                        return True, None

                    if not os.path.isfile(value):
                        self.my_output.error('Expected attribute %s value is existing local file: %s' % (attribute_name, value))
                        return False, None

                    return True, value

            if rules['type'] == 'int':
                if rules['check'] == 'port':
                    if value < 1 or value > 65535:
                        self.my_output.error('Expected attribute %s value is within TCP/UDP port range: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'host-prefix-v4':
                    if value < 1 or value > 30:
                        self.my_output.error('Expected attribute %s value is within <1,30> range: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'] == 'host-prefix-v6':
                    if value > 127 or value < 64:
                        self.my_output.error('Expected attribute %s value is within <64,127> range: %s' % (attribute_name, value))
                        return False, None
                    return True, value

                if rules['check'].startswith('ge'):
                    reference_value = int(rules['check'].lstrip('ge'))
                    if value < reference_value:
                        self.my_output.error('Expected attribute %s value is greater or equal %s: %s' % (attribute_name, reference_value, value))
                        return False, None
                    return True, value

                if rules['check'].startswith('gt'):
                    reference_value = int(rules['check'].lstrip('gt'))
                    if value <= reference_value:
                        self.my_output.error('Expected attribute %s value is greater than %s: %s' % (attribute_name, reference_value, value))
                        return False, None
                    return True, value

                if rules['check'].startswith('le'):
                    reference_value = int(rules['check'].lstrip('le'))
                    if value > reference_value:
                        self.my_output.error('Expected attribute %s value is lower or equal %s: %s' % (attribute_name, reference_value, value))
                        return False, None
                    return True, value

                if rules['check'].startswith('lt'):
                    reference_value = int(rules['check'].lstrip('lt'))
                    if value >= reference_value:
                        self.my_output.error('Expected attribute %s value is lower than %s: %s' % (attribute_name, reference_value, value))
                        return False, None
                    return True, value

                if rules['check'].startswith('eq'):
                    reference_value = int(rules['check'].lstrip('eq'))
                    if value != reference_value:
                        self.my_output.error('Expected attribute %s value is %s: %s' % (attribute_name, reference_value, value))
                        return False, None
                    return True, value

            self.my_output.error('Unsupported check: %s' % (rules['check']))
            self.my_output.default('Section: %s' % (section_name))
            self.my_output.default('Key: %s' % (key))
            self.my_output.default('Rules: %s' % (rules))
            self.my_output.default('Value: %s' % (value))
            return False, None

        return True, value

    def validate_section(self, section_name, user_input):
        rules = self.get_section_rules(section_name)
        if rules is None:
            self.my_output.error('Section %s rules not defined for installation method %s' % (section_name, self.ocp_type))
            return None

        if rules['value'] == 'dict':
            if not isinstance(user_input, dict):
                self.my_output.error('Section %s is expected to be dictionary' % (section_name))
                return None

            validated_input = {}
            for key in rules['properties']:
                if rules['properties'][key]['mandatory']:
                    if not self.is_key_in_section(key, user_input):
                        self.my_output.error('Required property %s.%s' % (section_name, key))
                        return None

                    success, value = self.validate_key_value(
                        section_name,
                        key,
                        rules['properties'][key],
                        self.get_key_value(key, user_input)
                    )
                    if not success:
                        return None

                    validated_input = self.add_key_value(
                        validated_input,
                        key,
                        value
                    )

                if not rules['properties'][key]['mandatory']:
                    if self.is_key_in_section(key, user_input):
                        success, value = self.validate_key_value(
                            section_name,
                            key,
                            rules['properties'][key],
                            self.get_key_value(key, user_input)
                        )
                        if not success:
                            return None

                        validated_input = self.add_key_value(
                            validated_input,
                            key,
                            value
                        )
                    else:
                        validated_input = self.add_key_value(
                            validated_input,
                            key,
                            rules['properties'][key]['default']
                        )

        if rules['value'] == 'list_of_dict':
            if not isinstance(user_input, list):
                self.my_output.error('Section %s is expected to be list' % (section_name))
                return None

            if 'min_length' in rules:
                if len(user_input) < rules['min_length']:
                    self.my_output.error('Section %s is expected to be list with minimum %s elements: %s' % (section_name, rules['min_length'], len(user_input)))
                    return None

            if 'max_length' in rules:
                if len(user_input) > rules['max_length']:
                    self.my_output.error('Section %s is expected to be list with maximum %s elements: %s' % (section_name, rules['max_length'], len(user_input)))
                    return None

            validated_input = []
            for item in user_input:
                if not isinstance(item, dict):
                    self.my_output.error('Section %s is expected to be list of dict' % (section_name))
                    return None

                validated_item = {}
                for key in rules['properties']:
                    if rules['properties'][key]['mandatory']:
                        if not self.is_key_in_section(key, item):
                            self.my_output.error('Required property %s.%s' % (section_name, key))
                            return None

                        success, value = self.validate_key_value(
                            section_name,
                            key,
                            rules['properties'][key],
                            self.get_key_value(key, item)
                        )
                        if not success:
                            return None

                        validated_item = self.add_key_value(
                            validated_item,
                            key,
                            value
                        )

                    if not rules['properties'][key]['mandatory']:
                        if self.is_key_in_section(key, item):
                            success, value = self.validate_key_value(
                                section_name,
                                key,
                                rules['properties'][key],
                                self.get_key_value(key, item)
                            )
                            if not success:
                                return None

                            validated_item = self.add_key_value(
                                validated_item,
                                key,
                                value
                            )
                        else:
                            validated_item = self.add_key_value(
                                validated_item,
                                key,
                                rules['properties'][key]['default']
                            )

                validated_input.append(validated_item)

        if rules['value'] == 'list_of_str':
            if not isinstance(user_input, list):
                self.my_output.error('Section %s is expected to be list' % (section_name))
                return None

            validated_input = []
            for value in user_input:
                if not isinstance(value, str):
                    self.my_output.error('Section %s is expected to be list of strings' % (section_name))
                    return None

                if rules['check'] is None:
                    validated_input.append(value)
                    continue

                if rules['check'] is not None:
                    if rules['check'] == 'ssh-public-key':
                        if not ip_helper.is_public_key_valid(value):
                            self.my_output.error('Section %s is expected to be list of ssh public keys' % (section_name))
                            return None
                        validated_input.append(value)
                        continue

                    self.my_output.error('Unsupported check: %s' % (rules['check']))
                    return None

        return validated_input

    def validate_sections(self, mandatory, optional):
        for key in mandatory:
            if key not in self.ocp_user_input:
                self.ocp_user_input[key] = {}

        validated_input = {}
        for key in self.ocp_user_input:
            if key in mandatory or key in optional:
                validated_input[key] = self.validate_section(key, self.ocp_user_input[key])
                if validated_input[key] is None:
                    return None

        return validated_input
