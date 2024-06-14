import os
import time
import yaml

from lib import ssh


class OcpVmCreateImage():
    def __init__(self):
        pass

    def create_image(self):
        if self.user_input['deployment']['image']['enabled']:
            image_dv_filename = self.user_input['deployment']['image']['dv']
            if image_dv_filename is not None:
                yaml_content = self.user_input['files'][image_dv_filename]
                content = yaml.safe_load(yaml_content)

                if self.user_input['deployment']['image']['ip'] is None:
                    self.log.error(
                        'create_image',
                        'Image repository IP not defined in deployment file'
                    )
                    return False

                if self.user_input['deployment']['image']['username'] is None:
                    self.log.error(
                        'create_image',
                        'Image repository username not defined in deployment file'
                    )
                    return False

                success = self.create_ocp_vm_image(
                    self.user_input['deployment']['image']['source'],
                    self.user_input['deployment']['image']['ip'],
                    self.user_input['deployment']['image']['username'],
                    self.user_input['deployment']['image']['password'],
                    self.user_input['deployment']['image']['key_filename'],
                    self.user_input['deployment']['image']['path'],
                    content,
                    reuse=self.user_input['deployment']['image']['reuse'],
                    must_bound=self.user_input['deployment']['image']['must_bound']
                )
                if not success:
                    return False

        return True

    def create_ocp_vm_image(self, image_source, server_ip, server_username, server_password, server_key_filename, image_filename, data_volume, reuse=False, must_bound=True):
        data_volume_namespace = data_volume['metadata']['namespace']
        data_volume_name = data_volume['metadata']['name']

        if self.k8s_handler.is_data_volume(data_volume_namespace, data_volume_name):
            if not reuse:
                self.my_output.error(
                    'Image data volume already exists: %s/%s' % (
                        data_volume_namespace,
                        data_volume_name
                    )
                )
                return False

            self.my_output.default(
                'Image data volume already exists with reuse enabled: %s/%s' % (
                    data_volume_namespace,
                    data_volume_name
                )
            )
            return True

        if self.k8s_handler.is_pvc(data_volume_namespace, '%s-scratch' % (data_volume_name)):
            self.my_output.error(
                'Image scratch pvc exists: %s/%s' % (
                    data_volume_namespace,
                    '%s-scratch' % (data_volume_name)
                )
            )
            return False

        if self.k8s_handler.is_pvc(data_volume_namespace, data_volume_name):
            self.my_output.default(
                'Image pvc already exists: %s/%s' % (
                    data_volume_namespace,
                    data_volume_name
                )
            )
            return True

        self.my_output.default(
            'Image data volume will be created: %s/%s' % (
                data_volume_namespace,
                data_volume_name
            )
        )

        if image_source == 'file':
            self.my_output.default(
                'Download image from %s@%s:%s' % (
                    server_username,
                    server_ip,
                    image_filename
                )
            )

            ssh_handler = ssh.Ssh(
                server_ip,
                server_username,
                password=server_password,
                key_filename=server_key_filename,
                log_id=self.log_id
            )

            destination = '/tmp/%s' % (
                os.path.basename(
                    image_filename
                )
            )
            success = ssh_handler.scp_file(
                image_filename,
                destination,
                put=False
            )
            if not success:
                self.my_output.error(
                    'Image download failed'
                )
                return False
            self.my_output.default(
                'Image downloaded: %s' % (destination)
            )

            self.my_output.default(
                'Image upload to virtctl-ready host...'
            )
            ssh_handler = ssh.Ssh(
                self.ocp_cluster_settings['virtctl']['ip'],
                self.ocp_cluster_settings['virtctl']['username'],
                password=self.ocp_cluster_settings['virtctl']['password'],
                key_filename=self.ocp_cluster_settings['virtctl']['key_filename'],
                log_id=self.log_id
            )

            success = ssh_handler.scp_file(
                destination,
                destination,
                put=True
            )
            if not success:
                self.my_output.error(
                    'Image upload to installer failed'
                )
                return False

            self.my_output.default(
                'Image uploaded to installer: %s' % (
                    '/tmp/%s' % (destination)
                )
            )

        success = self.k8s_handler.create_data_volume(
            data_volume
        )
        if not success:
            self.my_output.error(
                'Data volume create failed: %s/%s' % (
                    data_volume['metadata']['namespace'],
                    data_volume['metadata']['name']
                )
            )
            return False

        self.my_output.default(
            'Data volume created: %s/%s' % (
                data_volume['metadata']['namespace'],
                data_volume['metadata']['name']
            )
        )

        self.my_output.default(
            'Wait till pvc %s/%s reaches bound state' % (
                data_volume['metadata']['namespace'],
                data_volume['metadata']['name']
            )
        )
        if not self.k8s_handler.wait_pvc_bound(data_volume['metadata']['namespace'], data_volume['metadata']['name'], log_error_on_timeout=must_bound):
            if must_bound:
                self.my_output.error(
                    'Image PVC did not reach bound state'
                )
                return False

            self.my_output.default(
                'Image PVC did not reach bound state however must_bound set to False'
            )

        if image_source == 'file':
            attempt = 1
            while True:
                time.sleep(5)

                command = 'virtctl image-upload dv %s --no-create --insecure --image-path %s' % (
                    data_volume['metadata']['name'],
                    destination,
                )
                self.my_output.default(
                    'Upload image to data volume: %s' % (command)
                )
                success, output, error = ssh_handler.run_cmd(
                    command,
                    live_output=True
                )
                if not success:
                    self.my_output.error(
                        'Upload image to data volume failed'
                    )
                    attempt = attempt + 1
                    if attempt > 5:
                        return False

                if success:
                    break

            self.my_output.default(
                'Upload image to data volume completed: %s/%s' % (
                    data_volume['metadata']['namespace'],
                    data_volume['metadata']['name']
                )
            )

        return True
