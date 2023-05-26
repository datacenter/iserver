import os
import time
import traceback

from lib import ssh


class OcpVmImage():
    def __init__(self):
        pass

    def is_ocp_dv_vm_image(self, label_special, cache=True):
        dvs_mo = self.get_ocp_dv_vm_image(
            label_special,
            cache=cache
        )
        if dvs_mo is None or len(dvs_mo) == 0:
            return False
        return True

    def get_ocp_dv_vm_image(self, image_filename, cache=True):
        if not self.get_ocp_dvs(cache=cache):
            return []

        image_mo = []
        for dv_mo in self.dvs:
            if 'labels' not in dv_mo['metadata']:
                continue

            if 'type' not in dv_mo['metadata']['labels']:
                continue

            if dv_mo['metadata']['labels']['type'] != 'image':
                continue

            if 'filename' not in dv_mo['metadata']['labels']:
                continue

            if dv_mo['metadata']['labels']['filename'] != image_filename:
                continue

            image_mo.append(
                dv_mo
            )

        return image_mo

    def create_ocp_vm_image(self, server_ip, server_username, server_password, server_key_filename, image_filename, data_volume):
        data_volume_namespace = data_volume['metadata']['namespace']
        data_volume_name = data_volume['metadata']['name']
        if self.is_ocp_dv(data_volume_namespace, data_volume_name):
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

    def delete_ocp_dv_vm_image(self, label_special, cache=True):
        data_volumes = self.get_ocp_dv_vm_image(label_special, cache=cache)
        if len(data_volumes) == 0:
            return True

        delete_success = True

        for data_volume in data_volumes:
            try:
                start_time = int(time.time() * 1000)
                obj_list = self.api.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
                success = obj_list.delete(
                    namespace=data_volume['metadata']['namespace'],
                    name=data_volume['metadata']['name']
                )
            except BaseException:
                success = False
                self.log.error('ocp.delete_ocp_dv_vm_image', traceback.format_exc())

            self.log.ocp(
                'delete',
                'dv',
                success,
                int(time.time() * 1000) - start_time
            )

            if success:
                self.my_output.default(
                    'Delete data volume: %s/%s' % (
                        data_volume['metadata']['namespace'],
                        data_volume['metadata']['name']
                    )
                )
            else:
                self.my_output.error(
                    'Delete data volume failed: %s/%s' % (
                        data_volume['metadata']['namespace'],
                        data_volume['metadata']['name']
                    )
                )
                delete_success = False

        return delete_success
