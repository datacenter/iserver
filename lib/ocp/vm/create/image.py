import os
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

                success = self.create_ocp_vm_image(
                    self.user_input['deployment']['image']['ip'],
                    self.user_input['deployment']['image']['username'],
                    self.user_input['deployment']['image']['password'],
                    self.user_input['deployment']['image']['key_filename'],
                    self.user_input['deployment']['image']['path'],
                    content
                )
                if not success:
                    return False

        return True

    def create_ocp_vm_image(self, server_ip, server_username, server_password, server_key_filename, image_filename, data_volume):
        data_volume_namespace = data_volume['metadata']['namespace']
        data_volume_name = data_volume['metadata']['name']
        if self.k8s_handler.is_data_volume(data_volume_namespace, data_volume_name):
            self.my_output.default(
                'Image data volume already exists: %s/%s' % (
                    data_volume_namespace,
                    data_volume_name
                )
            )
            return True

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
            key_filename=server_key_filename
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
            'Image upload to installer...'
        )
        ssh_handler = ssh.Ssh(
            self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            key_filename=self.ocp_cluster_settings['parameters']['installer']['vm']['key_filename']
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
            return False

        self.my_output.default(
            'Upload image to data volume completed: %s/%s' % (
                data_volume['metadata']['namespace'],
                data_volume['metadata']['name']
            )
        )

        return True
