import os
import json
import uuid
import tarfile
import traceback

from lib import file_helper
from lib import ssh
from lib.intersight import asset_device_registration


class IwoOcpCreateLcm():
    def __init__(self):
        pass

    def get_chart_values(self, chart_filename):
        if not os.path.isfile(chart_filename):
            self.log.error(
                'get_chart_values',
                'Chart file not found: %s' % (chart_filename)
            )
            return None

        try:
            with tarfile.open(chart_filename) as file_handler:
                file_handler.extract('iwo-k8s-collector/values.yaml', '/tmp/')
            file_handler.close()
        except BaseException:
            self.log.error(
                'get_chart_values',
                'Failed to extract values.yaml: %s' % (chart_filename)
            )
            self.log.error(
                'get_chart_values',
                traceback.format_exc()
            )
            return None

        values_filename = '/tmp/iwo-k8s-collector/values.yaml'
        content = file_helper.get_file_yaml(
            values_filename
        )
        if content is None:
            self.log.error(
                'get_chart_values',
                'File read failed: %s' % (values_filename)
            )
            return None

        self.log.debug(
            'get_chart_values',
            json.dumps(content, indent=4)
        )
        return content

    def upload_chart(self, chart_filename, cluster_parameters):
        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        destination = '/root/iwo-chart.tgz'
        success = ssh_handler.scp_file(
            chart_filename,
            destination
        )

        if not success:
            self.log.error(
                'upload_chart',
                'IWO helm chart upload failed'
            )
            return None

        self.log.debug(
            'upload_chart',
            'IWO helm chart uploaded: %s' % (destination)
        )

        return destination

    def generate_create_variables(self, destination_chart_filename, cluster_parameters, chart_values):
        variables = {}
        variables['CHART'] = destination_chart_filename
        variables['NAMESPACE'] = 'iwo-collector'
        variables['POD'] = 'my-iwo-k8s-collector'
        variables['SERVER'] = chart_values['iwoServerVersion']
        variables['COLLECTOR'] = chart_values['collectorImage']['tag']
        variables['TARGET'] = 'my-k8s-cluster'
        if cluster_parameters['proxy']['enabled']:
            variables['HTTP_PROXY_ENABLED'] = 'True'
            variables['HTTP_PROXY_SERVER'] = cluster_parameters['proxy']['https'].split(':')[1][2:]
            variables['HTTP_PROXY_PORT'] = cluster_parameters['proxy']['https'].split(':')[2]
        else:
            variables['HTTP_PROXY_ENABLED'] = 'False'

        self.log.debug(
            'generate_create_variables',
            json.dumps(variables, indent=4)
        )

        return variables

    def install_iwo(self, cluster_parameters, variables):
        filename = self.get_template_filename('install.sh')
        if filename is None:
            self.log.error(
                'install_iwo',
                'Installation template not found'
            )
            return False

        content = self.get_template_content(filename, variables)
        if content is None:
            self.log.error(
                'install_iwo',
                'Installation template preparation failed'
            )
            return False

        script_source = '/tmp/%s' % (str(uuid.uuid4()))
        with open(script_source, 'w', encoding='utf-8') as file_handler:
            file_handler.write(content)

        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        success = ssh_handler.run_file_upload(
            script_source,
            '/root/iwo_install.sh',
            744
        )
        if not success:
            self.log.error(
                'install_iwo',
                'Installation script upload failed'
            )

        success, output, error = ssh_handler.run_cmd(
            'dos2unix /root/iwo_install.sh',
            live_output=False
        )
        if not success:
            self.log.error(
                'install_iwo',
                'Installation script preparation failed'
            )

        success, output, error = ssh_handler.run_cmd(
            './iwo_install.sh',
            live_output=True
        )
        if not success:
            self.log.error(
                'install_iwo',
                'Installation script failed'
            )
            self.log.error(
                'install_iwo',
                output
            )
            self.log.error(
                'install_iwo',
                error
            )

        return True

    def create_intersight_target(self, iaccount, device_identifier, security_token):
        asset_handler = asset_device_registration.AssetDeviceRegistration(iaccount, log_id=self.log_id)
        success = asset_handler.create_target(
            device_identifier,
            security_token
        )
        if not success:
            self.my_output.error('Intersight target create failed')
            return False

        self.my_output.default('Intersight target created')
        return True

    def create(self, cluster_name, iaccount, chart_filename):
        self.my_output.default('Check OCP cluster')
        cluster_parameters = self.ocp_settings_handler.get_ocp_cluster_parameters(cluster_name)
        if cluster_parameters is None:
            return False

        if self.is_iwo_installed(cluster_parameters):
            self.my_output.default('IWO is already installed')
        else:
            self.my_output.default('Check IWO chart')
            chart_values = self.get_chart_values(chart_filename)
            if chart_values is None:
                return False

            self.my_output.default('Upload IWO chart')
            destination_chart_filename = self.upload_chart(chart_filename, cluster_parameters)
            if destination_chart_filename is None:
                return False

            variables = self.generate_create_variables(destination_chart_filename, cluster_parameters, chart_values)

            self.my_output.default('Install IWO from chart')
            if not self.install_iwo(cluster_parameters, variables):
                return False

        self.my_output.default('Collect device identifier')
        device_identifier = self.get_install_device_identifier(cluster_parameters)
        if device_identifier is None:
            return False

        self.my_output.default('Collect security token')
        security_token = self.get_security_token(cluster_parameters)
        if security_token is None:
            return False

        self.my_output.default('Create Intersight Target')
        if self.is_intersight_target(iaccount, device_identifier):
            self.my_output.default('Intersight target already defined')
        else:
            if not self.create_intersight_target(iaccount, device_identifier, security_token):
                return False

        iwo_parameters = {}
        iwo_parameters['iaccount'] = iaccount
        iwo_parameters['device_identifier'] = device_identifier
        iwo_parameters['security_token'] = security_token
        iwo_parameters['registration_id'] = self.get_intersight_target_moid(iaccount, device_identifier)
        iwo_parameters['claim_id'] = self.get_intersight_target_claim(iaccount, device_identifier)
        if not self.set_iwo_installed(cluster_parameters, iwo_parameters):
            return False

        if not self.ocp_settings_handler.set_ocp_cluster_parameter(cluster_name, 'iwo', iwo_parameters):
            self.my_output.error('OCP cluster iwo settings failed')
            return False
        self.my_output.default('OCP cluster iwo settings set')

        return True
