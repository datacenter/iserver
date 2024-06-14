import os
import copy
import traceback
import yaml

from lib import ip_helper
from lib import file_helper
from lib import log_helper
from lib import output_helper


class Template():
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(verbose=verbose, debug=debug)

    def get_template_directory(self, subdirectory):
        template_dir = os.path.join(
            file_helper.get_main_dir(),
            'templates'
        )

        for item in subdirectory.split('/'):
            template_dir = os.path.join(
                template_dir,
                item
            )

        return template_dir

    def get_template_filename(self, subdirectory, template_type, filename):
        template_filename = os.path.join(
            os.path.join(
                self.get_template_directory(subdirectory),
                template_type
            ),
            filename
        )
        if not os.path.isfile(template_filename):
            self.my_output.error('File not found: %s' % (template_filename))
            return None

        return template_filename

    def is_template_attributes(self, template):
        attributes = self.get_template_attributes(template)
        if len(attributes) > 0:
            self.my_output.debug('Template attributes:')
            for attribute in attributes:
                self.my_output.debug('- %s' % (attribute))

            return True

        return False

    def get_word_attribute(self, word):
        if '${' in word:
            pattern = word.split('${')[1]
            if '}' in pattern:
                value = pattern.split('}')[0]
                return value
        return None

    def get_template_attributes(self, template):
        attributes = []
        for line in template.split('\n'):
            for word in line.split(' '):
                attribute = self.get_word_attribute(word)
                if attribute is not None:
                    attributes.append(attribute)
        return attributes

    def replace_attributes(self, content, variables):
        if content is None:
            return None

        if variables is None:
            return content

        my_variables = copy.deepcopy(variables)
        for key in my_variables:
            try:
                pattern = '${%s}' % (key)
                content = content.replace(pattern, str(my_variables[key]))

            except BaseException:
                self.my_output.error('Variable %s replacement failed' % (key))
                self.my_output.error(traceback.format_exc())
                return None

        return content

    def get_template(self, template_filename, variables, replace_variables_enabled=True, check_remaining_variables=True, yaml_conversion=False, yaml_check=False):
        content = file_helper.get_file(template_filename)
        if content is None:
            self.log.error(
                'get_template',
                'File read failed: %s' % (template_filename)
            )
            return None

        content = self.replace_attributes(content, variables)
        if content is None:
            self.log.error(
                'get_template',
                'Variable replace failed: %s' % (template_filename)
            )
            return None

        if check_remaining_variables:
            if self.is_template_attributes(content):
                self.my_output.error('Not all attributes replaced: %s' % (template_filename))
                self.my_output.default(content)
                return None

        if yaml_check:
            try:
                content_check = yaml.safe_load(content)

            except BaseException:
                self.my_output.error('YAML format required')
                self.my_output.traceback(traceback.format_exc())
                return None

        if yaml_conversion:
            try:
                content = yaml.safe_load(content)

            except BaseException:
                self.my_output.error('YAML format required')
                self.my_output.traceback(traceback.format_exc())
                return None

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

        if rules['type'] not in ['str', 'int', 'bool', 'list_of_ip', 'list_of_str', 'opaque']:
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

            if rules['type'] == 'opaque':
                return True, value

            self.my_output.error('Unsupported check: %s' % (rules['check']))
            self.my_output.default('Section: %s' % (section_name))
            self.my_output.default('Key: %s' % (key))
            self.my_output.default('Rules: %s' % (rules))
            self.my_output.default('Value: %s' % (value))
            return False, None

        return True, value

    def validate_input(self, rules_subdirectory, input_type, user_input):
        rules = file_helper.get_file_yaml(
            self.get_template_filename(
                rules_subdirectory,
                'rules',
                '%s.yaml' % (input_type)
            )
        )
        if rules is None:
            self.my_output.error('Rules %s not defined for %s' % (input_type, rules_subdirectory))
            return None

        if rules['value'] == 'dict':
            if not isinstance(user_input, dict):
                self.my_output.error('%s is expected to be dictionary' % (input_type))
                return None

            validated_input = {}
            for key in rules['properties']:
                if rules['properties'][key]['mandatory']:
                    if not self.is_key_in_section(key, user_input):
                        self.my_output.error('Required property %s.%s' % (input_type, key))
                        return None

                    success, value = self.validate_key_value(
                        input_type,
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
                            input_type,
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
                self.my_output.error('%s is expected to be list' % (input_type))
                return None

            if 'min_length' in rules:
                if len(user_input) < rules['min_length']:
                    self.my_output.error('%s is expected to be list with minimum %s elements: %s' % (input_type, rules['min_length'], len(user_input)))
                    return None

            if 'max_length' in rules:
                if len(user_input) > rules['max_length']:
                    self.my_output.error('%s is expected to be list with maximum %s elements: %s' % (input_type, rules['max_length'], len(user_input)))
                    return None

            validated_input = []
            for item in user_input:
                if not isinstance(item, dict):
                    self.my_output.error('%s is expected to be list of dict' % (input_type))
                    return None

                validated_item = {}
                for key in rules['properties']:
                    if rules['properties'][key]['mandatory']:
                        if not self.is_key_in_section(key, item):
                            self.my_output.error('Required property %s.%s' % (input_type, key))
                            return None

                        success, value = self.validate_key_value(
                            input_type,
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
                                input_type,
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
                self.my_output.error('%s is expected to be list' % (input_type))
                return None

            validated_input = []
            for value in user_input:
                if not isinstance(value, str):
                    self.my_output.error('%s is expected to be list of strings' % (input_type))
                    return None

                if rules['check'] is None:
                    validated_input.append(value)
                    continue

                if rules['check'] is not None:
                    if rules['check'] == 'ssh-public-key':
                        if not ip_helper.is_public_key_valid(value):
                            self.my_output.error('%s is expected to be list of ssh public keys' % (input_type))
                            return None
                        validated_input.append(value)
                        continue

                    self.my_output.error('Unsupported check: %s' % (rules['check']))
                    return None

        return validated_input
