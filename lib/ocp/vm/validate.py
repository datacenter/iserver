import os
import yaml

from lib import file_helper
from lib import template

from lib import log_helper
from lib import output_helper


class OcpDeploymentValidate():
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.template_handler = template.Template(
            log_id=log_id
        )
        self.template_subdirectory = 'ocp/kubevirt'
        self.variables = None

    def get_deployment_yaml(self, filename):
        content = file_helper.get_file_yaml(filename)
        if content is None:
            self.log.error(
                'get_deployment_yaml',
                'File read failed: %s' % (filename)
            )
            return None

        self.variables = None
        if 'variables' in content:
            self.variables = content['variables']

        content = self.template_handler.get_template(
            filename,
            self.variables,
            replace_variables_enabled=True,
            check_remaining_variables=True,
            yaml_conversion=True
        )
        if content is None:
            self.log.error(
                'get_deployment_yaml',
                'File parse failed: %s' % (filename)
            )

        return content

    def validate(self, deployment_filename, chdir=None):
        data = self.get_deployment_yaml(deployment_filename)
        if data is None:
            return None

        validated_data = self.template_handler.validate_input(
            self.template_subdirectory,
            'deployment',
            data
        )

        if validated_data is None:
            return None

        if chdir is None:
            base_directory = os.path.dirname(deployment_filename)
        else:
            base_directory = chdir

        validated_data['files'] = {}

        filename = validated_data['deployment']['vm']
        validated_data['files'][filename] = self.template_handler.get_template(
            os.path.join(
                base_directory,
                filename
            ),
            self.variables,
            replace_variables_enabled=True,
            check_remaining_variables=True,
            yaml_check=True,
            yaml_conversion=False
        )

        vm_yaml = yaml.safe_load(
            validated_data['files'][filename]
        )
        if vm_yaml is None:
            self.log.error(
                'validate',
                'Yaml load failed: %s' % (validated_data['files'][filename])
            )
            return None

        for key in ['namespace', 'name']:
            if key not in vm_yaml['metadata']:
                self.my_output.error(
                    'Attribute metadata.%s is mandatory in %s' % (
                        key,
                        filename
                    )
                )
                return None

            if validated_data['deployment'][key] != vm_yaml['metadata'][key]:
                self.my_output.error(
                    'Attribute metadata.%s must be the same in %s and %s' % (
                        key,
                        deployment_filename,
                        filename
                    )
                )
                return None

        if validated_data['deployment']['image']['dv'] is not None:
            filename = validated_data['deployment']['image']['dv']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        if validated_data['deployment']['day0']['filename'] is not None:
            filename = validated_data['deployment']['day0']['filename']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        if validated_data['deployment']['day0']['dv'] is not None:
            filename = validated_data['deployment']['day0']['dv']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        if validated_data['deployment']['sriov']['policy'] is not None:
            for filename in validated_data['deployment']['sriov']['policy']:
                validated_data['files'][filename] = self.template_handler.get_template(
                    os.path.join(
                        base_directory,
                        filename
                    ),
                    self.variables,
                    replace_variables_enabled=True,
                    check_remaining_variables=True,
                    yaml_check=True,
                    yaml_conversion=False
                )
                if validated_data['files'][filename] is None:
                    return None

        if validated_data['deployment']['sriov']['network'] is not None:
            for filename in validated_data['deployment']['sriov']['network']:
                validated_data['files'][filename] = self.template_handler.get_template(
                    os.path.join(
                        base_directory,
                        filename
                    ),
                    self.variables,
                    replace_variables_enabled=True,
                    check_remaining_variables=True,
                    yaml_check=True,
                    yaml_conversion=False
                )
                if validated_data['files'][filename] is None:
                    return None

        if validated_data['deployment']['multus']['network'] is not None:
            for filename in validated_data['deployment']['multus']['network']:
                validated_data['files'][filename] = self.template_handler.get_template(
                    os.path.join(
                        base_directory,
                        filename
                    ),
                    self.variables,
                    replace_variables_enabled=True,
                    check_remaining_variables=True,
                    yaml_check=True,
                    yaml_conversion=False
                )
                if validated_data['files'][filename] is None:
                    return None

        if validated_data['deployment']['service']['ssh'] is not None:
            filename = validated_data['deployment']['service']['ssh']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        if validated_data['deployment']['service']['snmp'] is not None:
            filename = validated_data['deployment']['service']['snmp']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        if validated_data['deployment']['service']['netconf'] is not None:
            filename = validated_data['deployment']['service']['netconf']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        if validated_data['deployment']['service']['ui'] is not None:
            filename = validated_data['deployment']['service']['ui']
            validated_data['files'][filename] = self.template_handler.get_template(
                os.path.join(
                    base_directory,
                    filename
                ),
                self.variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_check=True,
                yaml_conversion=False
            )
            if validated_data['files'][filename] is None:
                return None

        return validated_data
