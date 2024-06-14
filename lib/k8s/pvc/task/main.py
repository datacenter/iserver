import os
import uuid

from lib.linux import main as linux


class K8sPvcTask():
    def __init__(self):
        pass

    def get_pvc_data_volume_upload_definition(self, namespace, name, access_modes, storage, bind):
        dv_definition = {}
        dv_definition['apiVersion'] = 'cdi.kubevirt.io/v1beta1'
        dv_definition['kind'] = 'DataVolume'
        dv_definition['metadata'] = {}
        dv_definition['metadata']['namespace'] = namespace
        dv_definition['metadata']['name'] = name
        if bind:
            dv_definition['metadata']['annotations'] = {}
            dv_definition['metadata']['annotations']['cdi.kubevirt.io/storage.bind.immediate.requested'] = 'true'

        dv_definition['metadata']['labels'] = {}
        dv_definition['metadata']['labels']['createdy-by'] = 'iserver'

        dv_definition['spec'] = {}

        dv_definition['spec']['source'] = {}
        dv_definition['spec']['source']['upload'] = {}

        dv_definition['spec']['pvc'] = {}
        dv_definition['spec']['pvc']['accessModes'] = access_modes

        dv_definition['spec']['pvc']['resources'] = {}
        dv_definition['spec']['pvc']['resources']['requests'] = {}
        dv_definition['spec']['pvc']['resources']['requests']['storage'] = storage

        return dv_definition

    def create_pvc_via_data_volume_upload(
            self,
            namespace,
            name,
            tools,
            virtctl,
            source_filename=None,
            remote_filename=None,
            repository=None,
            file_type='file',
            access_modes=['ReadWriteOnce'],
            size='1Gi',
            bind=True,
            must_bound=True
            ):
        if file_type not in ['file', 'day0']:
            self.log.error(
                'create_pvc_via_data_volume_upload',
                'Unsupported file type: %s' % (file_type)
            )
            return False

        if self.is_data_volume(namespace, name):
            self.log.error(
                'create_pvc_via_data_volume_upload',
                'Data volume already exists: %s/%s' % (namespace, name)
            )
            return False

        if source_filename is not None:
            if not os.path.isfile(source_filename):
                self.log.error(
                    'create_pvc_via_data_volume_upload',
                    'File not found: %s' % (source_filename)
                )
                return False

        virtctl_handler = linux.Linux(
            virtctl['ip'],
            virtctl['username'],
            password=virtctl['password'],
            key_filename=virtctl['key_filename'],
            log_id=self.log_id
        )

        if remote_filename is not None:
            if not virtctl_handler.ssh_handler.is_file(remote_filename):
                self.log.error(
                    'create_pvc_via_data_volume_upload',
                    'Remote file not found at virtctl server: %s' % (source_filename)
                )
                return False

        data_volume = self.get_pvc_data_volume_upload_definition(
            namespace,
            name,
            access_modes,
            size,
            bind
        )

        if not self.create_data_volume(data_volume):
            return False

        self.log.debug(
            'create_pvc_via_data_volume_upload',
            'Create data volume: %s/%s' % (namespace, name)
        )
        self.log.debug(
            'create_pvc_via_data_volume_upload',
            data_volume
        )

        if not self.wait_data_volume_upload_ready(namespace, name, log_error_on_timeout=must_bound):
            if must_bound:
                return False

        self.log.debug(
            'create_pvc_via_data_volume_upload',
            'Data volume ready for upload'
        )

        if source_filename is not None:
            if file_type == 'day0':
                tools_handler = linux.Linux(
                    tools['ip'],
                    tools['username'],
                    password=tools['password'],
                    key_filename=tools['key_filename'],
                    log_id=self.log_id
                )

                local_day0_filename = '/tmp/%s.iso' % (str(uuid.uuid4()))
                if not tools_handler.genisoimage(source_filename, local_day0_filename):
                    return False

                source_filename = local_day0_filename

            remote_filename = '/tmp/%s' % (
                os.path.basename(source_filename)
            )

            success = virtctl_handler.ssh_handler.run_file_upload(
                source_filename,
                remote_filename
            )
            if not success:
                self.log.error(
                    'create_pvc_via_data_volume_upload',
                    'File upload failed: %s => %s' % (source_filename, remote_filename)
                )
                return False

        if not virtctl_handler.virtctl_image_upload(namespace, name, remote_filename):
            return False

        return True
