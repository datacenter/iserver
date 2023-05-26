import json
import uuid

from lib.intersight import asset_device_registration
from lib import ssh


class IwoOcpDeleteLcm():
    def __init__(self):
        pass

    def delete_iwo_install_finished(self, cluster_parameters):
        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        filename = '/root/.iwo_installed'
        if ssh_handler.is_file(filename):
            if not ssh_handler.delete_file(filename):
                self.my_output.error('Post installation flag delete failed')
                return False
        self.my_output.default('IWO installation complete flag deleted')
        return True

    def uninstall_iwo(self, cluster_parameters, variables):
        filename = self.get_template_filename('uninstall.sh')
        if filename is None:
            self.log.error(
                'uninstall_iwo',
                'Uninstallation template not found'
            )
            return False

        content = self.get_template_content(filename, variables)
        if content is None:
            self.log.error(
                'uninstall_iwo',
                'Uninstallation template preparation failed'
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
            '/root/iwo_uninstall.sh',
            744
        )
        if not success:
            self.log.error(
                'uninstall_iwo',
                'Uninstallation script upload failed'
            )

        success, output, error = ssh_handler.run_cmd(
            'dos2unix /root/iwo_uninstall.sh',
            live_output=False
        )
        if not success:
            self.log.error(
                'uninstall_iwo',
                'Unnstallation script preparation failed'
            )

        success, output, error = ssh_handler.run_cmd(
            './iwo_uninstall.sh',
            live_output=True
        )
        if not success:
            self.log.error(
                'uninstall_iwo',
                'Uninstallation script failed'
            )

        return True

    def generate_delete_variables(self, cluster_parameters):
        variables = {}
        variables['NAMESPACE'] = 'iwo-collector'
        variables['POD'] = 'my-iwo-k8s-collector'

        self.log.debug(
            'generate_delete_variables',
            json.dumps(variables, indent=4)
        )

        return variables

    def delete_intersight_target(self, iaccount, cluster_parameters):
        device_identifier = self.get_install_device_identifier(cluster_parameters)
        if device_identifier is None:
            self.my_output.info('Target serial number not found - target is unlikely to exist')
            return True

        target_moid = self.get_intersight_target_claim(iaccount, device_identifier)
        if target_moid is None:
            self.my_output.default('No target found with serial: %s' % (device_identifier))
            return True

        asset_handler = asset_device_registration.AssetDeviceRegistration(iaccount, log_id=self.log_id)
        success = asset_handler.delete_target(target_moid)
        if not success:
            self.my_output.error('Target delete failed: %s' % (target_moid))
            return False

        self.my_output.default('Target deleted: %s' % (target_moid))
        return True

    def delete(self, cluster_name, iaccount):
        self.my_output.default('Check OCP cluster')
        cluster_parameters = self.ocp_settings_handler.get_ocp_cluster_parameters(cluster_name)
        if cluster_parameters is None:
            return False

        variables = self.generate_delete_variables(cluster_parameters)

        self.my_output.default('Uninstall')
        if not self.uninstall_iwo(cluster_parameters, variables):
            return False

        self.my_output.default('Delete Intersight Target')
        if not self.delete_intersight_target(iaccount, cluster_parameters):
            return False

        if not self.delete_iwo_install_finished(cluster_parameters):
            return False

        if not self.ocp_settings_handler.set_ocp_cluster_parameter(cluster_name, 'iwo', None):
            self.my_output.error('OCP cluster iwo settings failed')
            return False
        self.my_output.default('OCP cluster iwo settings cleared')

        return True
