import os
import time
import uuid
import subprocess
import yaml

from lib import ssh


class OcpVmCreateDay0():
    def __init__(self):
        pass

    def create_day0(self):
        if self.user_input['deployment']['day0']['enabled']:
            day0_dv_filename = self.user_input['deployment']['day0']['dv']
            if day0_dv_filename is None:
                self.my_output.error(
                    'Define deployment.day.dv value'
                )
                return False

            yaml_content = self.user_input['files'][day0_dv_filename]
            dv_content = yaml.safe_load(yaml_content)
            if dv_content is None or len(dv_content) == 0:
                self.my_output.error(
                    'Day0 data volume yaml not found'
                )
                return False

            source_filename = self.user_input['deployment']['day0']['source']
            day0_content = self.user_input['files'][source_filename]
            if day0_content is None or len(day0_content) == 0:
                self.my_output.error(
                    'Day0 configuration not found'
                )
                return False

            if self.is_ocp_vm_day0_dv(dv_content):
                return True

            success = self.create_ocp_vm_day0(
                self.user_input['deployment']['day0']['filename'],
                day0_content,
                self.user_input['deployment']['day0']['destination'],
                dv_content,
                reuse=self.user_input['deployment']['day0']['reuse'],
                must_bound=self.user_input['deployment']['day0']['must_bound']
            )
            if not success:
                return False

        return True

    def create_ocp_vm_day0_iso(self, day0_filepath, iso_filepath):
        ssh_handler = ssh.Ssh(
            self.ocp_cluster_settings['tools']['ip'],
            self.ocp_cluster_settings['tools']['username'],
            password=self.ocp_cluster_settings['tools']['password'],
            key_filename=self.ocp_cluster_settings['tools']['key_filename'],
            log_id=self.log_id
        )
        self.my_output.default(
            'Day0 generation done via tools'
        )

        remote_directory = '/tmp/%s' % (str(uuid.uuid4()))
        if not ssh_handler.create_directory(remote_directory):
            self.my_output.error(
                'Upload directory create failed: %s' % (remote_directory)
            )
            return False

        remote_filename = '%s/%s' % (
            remote_directory,
            os.path.basename(day0_filepath)
        )

        success = ssh_handler.scp_file(
            day0_filepath,
            remote_filename,
            put=True
        )
        if not success:
            self.my_output.error(
                'Day0 configuration upload failed'
            )
            return False

        self.my_output.default(
            'Day0 configuration uploaded: %s => %s' % (
                day0_filepath,
                remote_filename
            )
        )

        remote_iso_filename = '%s/%s' % (
            remote_directory,
            os.path.basename(iso_filepath)
        )
        command = 'genisoimage -r -o %s %s' % (
            remote_iso_filename,
            remote_filename
        )
        self.my_output.default(
            'Generate iso: %s' % (command)
        )
        success, output, error = ssh_handler.run_cmd(
            command,
            live_output=False
        )
        if not success:
            self.my_output.error(
                'Day0 iso generation failed'
            )
            return False

        self.my_output.default(
            'Day0 iso generated: %s' % (
                remote_iso_filename
            )
        )

        success = ssh_handler.scp_file(
            remote_iso_filename,
            iso_filepath,
            put=False
        )
        if not success:
            self.my_output.error(
                'Day0 iso download failed: %s => %s' % (remote_iso_filename, iso_filepath)
            )
            return False

        self.my_output.default(
            'Day0 downloaded: %s => %s' % (
                remote_iso_filename,
                iso_filepath
            )
        )

        return True

    def is_ocp_vm_day0_dv(self, data_volume):
        data_volume_namespace = data_volume['metadata']['namespace']
        data_volume_name = data_volume['metadata']['name']
        if self.k8s_handler.is_data_volume(data_volume_namespace, data_volume_name):
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

        return False

    def create_ocp_vm_day0(self, day0_filename, day0_content, iso_filename, data_volume, reuse=False, must_bound=True):
        data_volume_namespace = data_volume['metadata']['namespace']
        data_volume_name = data_volume['metadata']['name']

        if self.k8s_handler.is_data_volume(data_volume_namespace, data_volume_name):
            if not reuse:
                self.my_output.error(
                    'Day0 data volume already exists: %s/%s' % (
                        data_volume_namespace,
                        data_volume_name
                    )
                )
                return False

            self.my_output.default(
                'Day0 data volume already exists with reuse enabled: %s/%s' % (
                    data_volume_namespace,
                    data_volume_name
                )
            )
            return True

        # Step 1: Prepare ISO in local_directory/iso_filename

        local_directory = '/tmp/%s' % (str(uuid.uuid4()))
        os.makedirs(local_directory, exist_ok=True)

        day0_filepath = '%s/%s' % (
            local_directory,
            day0_filename
        )
        with open(day0_filepath, 'w', encoding='utf-8') as file_handler:
            file_handler.write(day0_content)

        iso_filepath = '%s/%s' % (
            local_directory,
            iso_filename
        )

        success = self.create_ocp_vm_day0_iso(
            day0_filepath,
            iso_filepath
        )

        if not success:
            return False

        # Step 2: upload iso to virtctl-ready linux

        ssh_handler = ssh.Ssh(
            self.ocp_cluster_settings['virtctl']['ip'],
            self.ocp_cluster_settings['virtctl']['username'],
            password=self.ocp_cluster_settings['virtctl']['password'],
            key_filename=self.ocp_cluster_settings['virtctl']['key_filename'],
            log_id=self.log_id
        )

        remote_iso_filepath = '/tmp/%s' % (iso_filename)
        success = ssh_handler.scp_file(
            iso_filepath,
            remote_iso_filepath,
            put=True
        )
        if not success:
            self.my_output.error(
                'Day0 iso upload to installer failed'
            )
            return False

        self.my_output.debug(
            'Day0 uploaded for virctl upload: %s => %s' % (
                iso_filepath,
                remote_iso_filepath
            )
        )

        # Step 3: create data volume

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

        self.my_output.debug(
            'Data volume created: %s/%s' % (
                data_volume['metadata']['namespace'],
                data_volume['metadata']['name']
            )
        )

        self.my_output.debug(
            'Wait till dv %s/%s is upload ready' % (
                data_volume['metadata']['namespace'],
                data_volume['metadata']['name']
            )
        )
        if not self.k8s_handler.wait_data_volume_upload_ready(data_volume['metadata']['namespace'], data_volume['metadata']['name'], log_error_on_timeout=must_bound):
            if must_bound:
                self.my_output.error(
                    'Day0 dv did not reach upload ready state'
                )
                return False

            self.my_output.default(
                'Day0 dv did not reach upload ready state however must_bound set to False... continue'
            )

        # Step 4: upload iso to data volume'

        attempt = 1
        while True:
            time.sleep(5)

            command = 'virtctl image-upload dv %s -n %s --no-create --insecure --image-path %s' % (
                data_volume['metadata']['name'],
                data_volume['metadata']['namespace'],
                remote_iso_filepath
            )
            self.my_output.debug(
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
