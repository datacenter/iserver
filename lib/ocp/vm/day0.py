import os
import time
import uuid
import subprocess

from lib import ssh


class OcpVmDay0():
    def __init__(self):
        pass

    def is_ocp_dv_vm_day0(self, namespace, name, cache=True):
        dvs_mo = self.get_ocp_dv_vm_day0(
            namespace,
            name,
            cache=cache
        )
        if dvs_mo is None:
            return False
        return True

    def get_ocp_dv_vm_day0(self, namespace, name, cache=True):
        if not self.get_ocp_dvs(cache=cache):
            return None

        for dv_mo in self.dvs:
            if dv_mo['metadata']['namespace'] == namespace and dv_mo['metadata']['name'] == name:
                return dv_mo

        return None

    def create_ocp_vm_day0(self, source_filename, source_content, destination, data_volume, tools=None):
        data_volume_namespace = data_volume['metadata']['namespace']
        data_volume_name = data_volume['metadata']['name']
        if self.is_ocp_dv(data_volume_namespace, data_volume_name):
            self.my_output.default(
                'Day0 data volume already exists: %s/%s' % (
                    data_volume_namespace,
                    data_volume_name
                )
            )
            return True

        if self.k8s_handler.is_pvc(data_volume_namespace, data_volume_name):
            self.my_output.default(
                'Day0 pvc already exists: %s/%s' % (
                    data_volume_namespace,
                    data_volume_name
                )
            )
            return True

        self.my_output.default(
            'Day0 data volume will be created: %s/%s' % (
                data_volume_namespace,
                data_volume_name
            )
        )

        directory = '/tmp/%s' % (str(uuid.uuid4()))
        os.makedirs(directory, exist_ok=True)

        day0_filename = '%s/%s' % (
            directory,
            source_filename
        )
        with open(day0_filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(source_content)

        if tools is not None and tools['enabled']:
            ssh_handler = ssh.Ssh(
                tools['ip'],
                tools['username'],
                password=tools['password'],
                key_filename=tools['key_filename']
            )
            self.my_output.default(
                'Day0 generation done via: %s@%s' % (
                    tools['username'],
                    tools['ip']
                )
            )

            if not ssh_handler.create_directory(directory):
                self.my_output.error(
                    'Upload directory create failed: %s' % (directory)
                )
                return False

            success = ssh_handler.scp_file(
                day0_filename,
                day0_filename,
                put=True
            )
            if not success:
                self.my_output.error(
                    'Day0 configuration upload failed'
                )
                return False

            self.my_output.default(
                'Day0 configuration uploaded: %s' % (
                    day0_filename
                )
            )

            iso_destination = '%s/%s' % (
                directory,
                destination
            )
            command = 'genisoimage -r -o %s %s' % (
                iso_destination,
                day0_filename
            )
            self.my_output.default(
                'Generate iso: %s' % (command)
            )
            success, output, error = ssh_handler.run_cmd(
                command,
                live_output=True
            )
            if not success:
                self.my_output.error(
                    'Day0 iso generation failed'
                )
                return False

            self.my_output.default(
                'Day0 iso generated: %s' % (
                    iso_destination
                )
            )

            success = ssh_handler.scp_file(
                iso_destination,
                iso_destination,
                put=False
            )
            if not success:
                self.my_output.error(
                    'Day0 iso download failed: %s' % (iso_destination)
                )
                return False

            self.my_output.default(
                'Day0 downloaded: %s' % (
                    iso_destination
                )
            )

        else:
            iso_destination = '%s/%s' % (
                directory,
                destination
            )
            command = 'genisoimage -r -o %s %s' % (
                iso_destination,
                day0_filename
            )
            self.my_output.default(
                'Generate iso: %s' % (command)
            )

            exit_code = subprocess.call(command.split())
            if exit_code > 0:
                self.my_output.default('ISO generation failed')
                return False

        ssh_handler = ssh.Ssh(
            self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            key_filename=self.ocp_cluster_settings['parameters']['installer']['vm']['key_filename']
        )

        success = ssh_handler.scp_file(
            iso_destination,
            '/tmp/%s' % (destination),
            put=True
        )
        if not success:
            self.my_output.error(
                'Day0 iso upload to installer failed'
            )
            return False

        self.my_output.default(
            'Day0 uploaded to installer: %s' % (
                '/tmp/%s' % (destination)
            )
        )

        success = self.create_ocp_dv(
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

        attempt = 1
        while True:
            time.sleep(5)

            command = 'virtctl image-upload dv %s --no-create --insecure --image-path %s' % (
                data_volume['metadata']['name'],
                '/tmp/%s' % (destination)
            )
            self.my_output.default(
                'Upload iso to data volume: %s' % (command)
            )

            success, output, error = ssh_handler.run_cmd(
                command,
                live_output=True
            )
            if not success:
                self.my_output.error(
                    'Upload iso to data volume failed'
                )
                attempt = attempt + 1
                if attempt > 5:
                    return False

            if success:
                break

        self.my_output.default(
            'Upload iso to data volume completed: %s/%s' % (
                data_volume['metadata']['namespace'],
                data_volume['metadata']['name']
            )
        )

        return True
