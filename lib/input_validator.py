import os

from lib import file_helper
from lib import ip_helper
from lib import log_helper


class InputValidator():
    def __init__(self, log_id=None):
        self.log_handler = log_helper.Log(log_id=log_id)
        self.base_directory = None

    def get_template_dir(self, template_name, template_category=None):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        templates_dir = os.path.join(main_dir, 'templates')
        if template_category is not None:
            templates_dir = os.path.join(templates_dir, template_category)

        template_dir = os.path.join(
            templates_dir,
            template_name
        )
        if not os.path.isdir(template_dir):
            self.log_handler.error(
                'get_template_dir',
                'Template definition not found: %s' % (template_dir)
            )
            return None

        return template_dir

    def get_template_files_dir(self, template_name, template_category=None):
        template_dir = self.get_template_dir(template_name, template_category=template_category)
        if template_dir is None:
            return None

        files_dir = os.path.join(
            template_dir,
            'files'
        )
        if not os.path.isdir(files_dir):
            self.log_handler.error(
                'get_template_files_dir',
                'Template files not found: %s' % (files_dir)
            )
            return None

        return files_dir

    def get_template_rules_dir(self, template_name, template_category=None):
        template_dir = self.get_template_dir(template_name, template_category=template_category)
        if template_dir is None:
            return None

        rules_dir = os.path.join(
            template_dir,
            'rules'
        )
        if not os.path.isdir(rules_dir):
            self.log_handler.error(
                'get_template_rules_dir',
                'Template rules not found: %s' % (rules_dir)
            )
            return None

        return rules_dir

    def get_section_rules(self, template_name, section_name, template_category=None):
        rules_dir = self.get_template_rules_dir(template_name, template_category=template_category)
        if rules_dir is None:
            return None

        filename = os.path.join(rules_dir, '%s.yaml' % (section_name))
        content = file_helper.get_file_yaml(
            filename
        )
        if content is None:
            self.log_handler.error(
                'get_section_rules',
                'Section %s rules read failed: %s' % (section_name, filename)
            )
            return None

        return content

    def get_template_name(self, user_input, template_reference=None, template_name=None):
        if template_reference is None and template_name is None:
            self.log_handler.error(
                'get_template_name',
                'Define template reference or name'
            )
            return None

        if template_name is not None:
            return template_name

        # Keep it stupid simple. Template reference has syntax section.key. No need to make it more complicated
        try:
            (section, key) = template_reference.split('.')
            template_name = user_input[section][key]
        except BaseException:
            self.log_handler.error(
                'get_template_name',
                'Template name expected at %s' % (template_reference)
            )
            return None

        return template_name

    def get_template_definition_key_value(self, template_name, key, template_category=None):
        template_definition = self.get_template_definition(template_name, template_category=template_category)
        if template_definition is None:
            return None

        if key not in template_definition['main']:
            self.log_handler.error(
                'get_template_definition_key_value',
                'No key %s found in template definition %s' % (key, template_name)
            )
            return None

        return template_definition['main'][key]

    def get_template_definition(self, template_name, template_category=None):
        rules_dir = self.get_template_rules_dir(template_name, template_category=template_category)
        if rules_dir is None:
            return None

        filename = os.path.join(rules_dir, 'main.yaml')
        content = file_helper.get_file_yaml(
            filename
        )
        if content is None:
            self.log_handler.error(
                'get_template_definition',
                'Template definition read failed: %s' % (filename)
            )

        return content

    def get_template_filename(self, template_name, filename, template_category=None):
        files_dir = self.get_template_files_dir(template_name, template_category=template_category)
        if files_dir is None:
            return None

        template_filename = os.path.join(files_dir, filename)
        if not os.path.isfile(template_filename):
            self.log_handler.error(
                'get_template_filename',
                'Template file not found: %s' % (template_filename)
            )
            return None

        return template_filename

    def get_input(self, location):
        if not os.path.isfile(location) and not os.path.isdir(location):
            self.log_handler.error(
                'get_input',
                'Specify valid location user input'
            )
            return None

        if os.path.isfile(location):
            content = file_helper.get_file_yaml(
                location
            )
            if content is None:
                return None

            return content

        content = {}
        for filename in os.listdir(location):
            if filename in ['.gitignore']:
                continue

            fullname = os.path.join(location, filename)
            if os.path.isdir(fullname):
                continue

            part = file_helper.get_file_yaml(
                fullname
            )
            if part is None:
                continue

            for key in part:
                if key in content:
                    self.log_handler.error(
                        'get_input',
                        'Sections have to be defined in single file: %s' % (key)
                    )
                    return None

                content[key] = part[key]

        return content

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

        if rules['type'] not in ['str', 'int', 'bool']:
            self.log_handler.error(
                'validate_key_value',
                'Unsupported attribute type: %s' % (rules['type'])
            )
            return False, None

        if rules['type'] == 'str':
            if value is None and rules['check'] == 'local-file-null-accepted':
                pass
            else:
                if not isinstance(value, str):
                    self.log_handler.error(
                        'validate_key_value',
                        'Expected attribute %s type is %s' % (attribute_name, rules['type'])
                    )
                    return False, None

        if rules['type'] == 'int':
            if not isinstance(value, int):
                self.log_handler.error(
                    'validate_key_value',
                    'Expected attribute %s type is %s' % (attribute_name, rules['type'])
                )
                return False, None

        if rules['type'] == 'bool':
            if not isinstance(value, bool):
                self.log_handler.error(
                    'validate_key_value',
                    'Expected attribute %s type is %s' % (attribute_name, rules['type'])
                )
                return False, None

        if rules['check'] is not None:
            if rules['type'] == 'bool':
                if rules['check'] == 'must-be-true':
                    if not value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is True: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'must-be-false':
                    if value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is False: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

            if rules['type'] == 'str':
                if rules['check'] == 'ipv4':
                    if not ip_helper.is_valid_ipv4_address(value):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid IPv4 address: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'ipv4s':
                    for item in value.split(','):
                        if not ip_helper.is_valid_ipv4_address(item):
                            self.log_handler.error(
                                'validate_key_value',
                                'Expected attribute %s value is list of valid IPv4 addresses: %s' % (attribute_name, value)
                            )
                            return False, None
                    return True, value

                if rules['check'] == 'ipv6':
                    if not ip_helper.is_valid_ipv6_address(value):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid IPv6 address: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'cidrv4':
                    if not ip_helper.is_valid_ipv4_cidr(value):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid IPv4 CIDR: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'cidrv6':
                    if not ip_helper.is_valid_ipv6_cidr(value):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid IPv6 CIDR: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'url':
                    if not ip_helper.is_url_valid(value):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid URL: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'dhcp-v4-range':
                    if len(value.split('-')) != 2:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid IPv4 address ranges: %s' % (attribute_name, value)
                        )
                        return False, None

                    (start_ip, end_ip) = value.split('-')
                    if not ip_helper.is_valid_ipv4_address(start_ip) or not ip_helper.is_valid_ipv4_address(end_ip):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is valid IPv4 address ranges: %s' % (attribute_name, value)
                        )
                        return False, None

                    return True, value

                if rules['check'] == 'not-empty-no-spaces':
                    if value is None:
                        value = ''
                    value = value.strip()

                    if len(value) == 0:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is non-empty string without spaces: %s' % (attribute_name, value)
                        )
                        return False, None

                    if ' ' in value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is non-empty string without spaces: %s' % (attribute_name, value)
                        )
                        return False, None

                    return True, value

                if rules['check'] == 'not-empty':
                    if value is None:
                        value = ''
                    value = value.strip()

                    if len(value) == 0:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is non-empty string: %s' % (attribute_name, value)
                        )
                        return False, None

                    return True, value

                if rules['check'].startswith('values:'):
                    reference_values = rules['check'].lstrip('values').lstrip(':')
                    if value not in reference_values.split(','):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is one of %s: %s' % (attribute_name, reference_values, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'local-file':
                    if os.path.isabs(value):
                        filename = value
                    else:
                        filename = os.path.join(
                            self.base_directory,
                            value
                        )
                    if not os.path.isfile(filename):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is existing local file: %s' % (attribute_name, filename)
                        )
                        return False, None

                    return True, value

                if rules['check'] == 'local-file-null-accepted':
                    if value is None:
                        return True, None

                    if len(value) == 0:
                        return True, None

                    if not os.path.isfile(value):
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is existing local file: %s' % (attribute_name, value)
                        )
                        return False, None

                    return True, value

                if rules['check'] == 'must-be-null':
                    if value is None:
                        return True, None

                    self.log_handler.error(
                        'validate_key_value',
                        'Expected attribute %s value is null' % (attribute_name)
                    )
                    return False, None

            if rules['type'] == 'int':
                if rules['check'] == 'port':
                    if value < 1 or value > 65535:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is within TCP/UDP port range: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'host-prefix-v4':
                    if value < 1 or value > 30:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is within <1,30> range: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'] == 'host-prefix-v6':
                    if value > 127 or value < 64:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is within <64,127> range: %s' % (attribute_name, value)
                        )
                        return False, None
                    return True, value

                if rules['check'].startswith('ge'):
                    reference_value = int(rules['check'].lstrip('ge'))
                    if value < reference_value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is greater or equal %s: %s' % (attribute_name, reference_value, value)
                        )
                        return False, None
                    return True, value

                if rules['check'].startswith('gt'):
                    reference_value = int(rules['check'].lstrip('gt'))
                    if value <= reference_value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is greater than %s: %s' % (attribute_name, reference_value, value)
                        )
                        return False, None
                    return True, value

                if rules['check'].startswith('le'):
                    reference_value = int(rules['check'].lstrip('le'))
                    if value > reference_value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is lower or equal %s: %s' % (attribute_name, reference_value, value)
                        )
                        return False, None
                    return True, value

                if rules['check'].startswith('lt'):
                    reference_value = int(rules['check'].lstrip('lt'))
                    if value >= reference_value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is lower than %s: %s' % (attribute_name, reference_value, value)
                        )
                        return False, None
                    return True, value

                if rules['check'].startswith('eq'):
                    reference_value = int(rules['check'].lstrip('eq'))
                    if value != reference_value:
                        self.log_handler.error(
                            'validate_key_value',
                            'Expected attribute %s value is %s: %s' % (attribute_name, reference_value, value)
                        )
                        return False, None
                    return True, value

            self.log_handler.error(
                'validate_key_value',
                'Unsupported check: %s' % (rules['check'])
            )
            return False, None

        return True, value

    def validate_section(self, section_name, section_rules, user_input):
        if section_rules['value'] == 'dict':
            if not isinstance(user_input, dict):
                self.log_handler.error(
                    'validate_section',
                    'Section %s is expected to be dictionary' % (section_name)
                )
                return None

            if not section_rules['validate']:
                validated_input = {}
                for key in user_input:
                    validated_input[key] = user_input[key]

            if section_rules['validate']:
                validated_input = {}
                for key in section_rules['properties']:
                    if section_rules['properties'][key]['mandatory']:
                        if not self.is_key_in_section(key, user_input):
                            self.log_handler.error(
                                'validate_section',
                                'Required property %s.%s' % (section_name, key)
                            )
                            return None

                        success, value = self.validate_key_value(
                            section_name,
                            key,
                            section_rules['properties'][key],
                            self.get_key_value(key, user_input)
                        )
                        if not success:
                            return None

                        validated_input = self.add_key_value(
                            validated_input,
                            key,
                            value
                        )

                    if not section_rules['properties'][key]['mandatory']:
                        if self.is_key_in_section(key, user_input):
                            success, value = self.validate_key_value(
                                section_name,
                                key,
                                section_rules['properties'][key],
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
                                section_rules['properties'][key]['default']
                            )

        if section_rules['value'] == 'list_of_dict':
            if not isinstance(user_input, list):
                self.log_handler.error(
                    'validate_section',
                    'Section %s is expected to be list' % (section_name)
                )
                return None

            if 'min_length' in section_rules:
                if len(user_input) < section_rules['min_length']:
                    self.log_handler.error(
                        'validate_section',
                        'Section %s is expected to be list with minimum %s elements: %s' % (section_name, section_rules['min_length'], len(user_input))
                    )
                    return None

            if 'max_length' in section_rules:
                if len(user_input) > section_rules['max_length']:
                    self.log_handler.error(
                        'validate_section',
                        'Section %s is expected to be list with maximum %s elements: %s' % (section_name, section_rules['max_length'], len(user_input))
                    )
                    return None

            if not section_rules['validate']:
                validated_input = []
                for item in user_input:
                    validated_input.append(item)

            if section_rules['validate']:
                validated_input = []
                for item in user_input:
                    if not isinstance(item, dict):
                        self.log_handler.error(
                            'validate_section',
                            'Section %s is expected to be list of dict' % (section_name)
                        )
                        return None

                    validated_item = {}
                    for key in section_rules['properties']:
                        if section_rules['properties'][key]['mandatory']:
                            if not self.is_key_in_section(key, item):
                                self.log_handler.error(
                                    'validate_section',
                                    'Required property %s.%s' % (section_name, key)
                                )
                                return None

                            success, value = self.validate_key_value(
                                section_name,
                                key,
                                section_rules['properties'][key],
                                self.get_key_value(key, item)
                            )
                            if not success:
                                return None

                            validated_item = self.add_key_value(
                                validated_item,
                                key,
                                value
                            )

                        if not section_rules['properties'][key]['mandatory']:
                            if self.is_key_in_section(key, user_input):
                                success, value = self.validate_key_value(
                                    section_name,
                                    key,
                                    section_rules['properties'][key],
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
                                    section_rules['properties'][key]['default']
                                )

                    validated_input.append(validated_item)

        if section_rules['value'] == 'list_of_str':
            if not isinstance(user_input, list):
                self.log_handler.error(
                    'validate_section',
                    'Section %s is expected to be list' % (section_name)
                )
                return None

            if not section_rules['validate']:
                validated_input = []
                for item in user_input:
                    validated_input.append(item)

            if section_rules['validate']:
                validated_input = []
                for value in user_input:
                    if not isinstance(value, str):
                        self.log_handler.error(
                            'validate_section',
                            'Section %s is expected to be list of strings' % (section_name)
                        )
                        return None

                    if section_rules['check'] is None:
                        validated_input.append(value)
                        continue

                    if section_rules['check'] is not None:
                        if section_rules['check'] == 'ssh-public-key':
                            if not ip_helper.is_public_key_valid(value):
                                self.log_handler.error(
                                    'validate_section',
                                    'Section %s is expected to be list of ssh public keys' % (section_name)
                                )
                                return None
                            validated_input.append(value)
                            continue

                        if section_rules['check'] == 'tasks-yaml':
                            filename = os.path.join(self.base_directory, value)
                            if not os.path.isfile(filename):
                                self.log_handler.error(
                                    'validate_section',
                                    'Expected attribute %s value is existing local file: %s' % (section_name, value)
                                )
                                return None

                            content = file_helper.get_file_yaml(filename)
                            if content is None:
                                self.log_handler.error(
                                    'validate_section',
                                    'Expected attribute %s value is existing local file with yaml formatted content: %s' % (section_name, value)
                                )
                                return None

                            validated_input.append(filename)
                            continue

                        self.log_handler.error(
                            'validate_section',
                            'Unsupported check: %s' % (section_rules['check'])
                        )
                        return None

        return validated_input

    def validate(self, user_input_location, operation, template_reference=None, template_category=None, template_name=None):
        user_input = self.get_input(user_input_location)
        if user_input is None:
            return None

        template_name = self.get_template_name(
            user_input,
            template_reference=template_reference,
            template_name=template_name
        )
        if template_name is None:
            return None

        template_definition = self.get_template_definition(template_name, template_category=template_category)
        if template_definition is None:
            return None

        mandatory_sections = template_definition['main']['operation'][operation]['mandatory']
        if mandatory_sections is None:
            mandatory_sections = []

        optional_sections = template_definition['main']['operation'][operation]['optional']
        if optional_sections is None:
            optional_sections = []

        for key in mandatory_sections:
            if key not in user_input:
                user_input[key] = {}

        validated_input = {}
        validated_input['template_name'] = template_name

        if os.path.isfile(user_input_location):
            self.base_directory = os.path.dirname(user_input_location)
        else:
            self.base_directory = user_input_location
        validated_input['base_directory'] = self.base_directory

        for section_name in user_input:
            if section_name in mandatory_sections or section_name in optional_sections:
                section_rules = self.get_section_rules(template_name, section_name, template_category=template_category)
                if section_rules is None:
                    return None

                validated_input[section_name] = self.validate_section(
                    section_name,
                    section_rules,
                    user_input[section_name]
                )
                if validated_input[section_name] is None:
                    return None

        return validated_input
