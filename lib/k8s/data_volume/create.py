import yaml
from menu.common import get_confirmation


class K8sDataVolumeCreate():
    def __init__(self):
        pass

    def get_data_volume_body(self, namespace, name, storage_class, source, access_modes, storage, bind=False, secret=None):
        body = {}
        body['apiVersion'] = 'cdi.kubevirt.io/v1beta1'
        body['kind'] = 'DataVolume'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if bind:
            body['metadata']['annotations'] = {}
            body['metadata']['annotations']['cdi.kubevirt.io/storage.bind.immediate.requested'] = 'true'

        body['spec'] = {}

        if source is None:
            body['spec']['source'] = {}
            body['spec']['source']['upload'] = {}
        else:
            body['spec']['source'] = {}
            body['spec']['source']['http'] = {}
            body['spec']['source']['http']['url'] = source
            if secret is not None:
                body['spec']['source']['http']['secretRef'] = secret

        body['spec']['pvc'] = {}
        body['spec']['pvc']['accessModes'] = access_modes

        body['spec']['pvc']['resources'] = {}
        body['spec']['pvc']['resources']['requests'] = {}
        body['spec']['pvc']['resources']['requests']['storage'] = storage
        body['spec']['pvc']['storageClassName'] = storage_class

        return body

    def create_data_volume(
            self, 
            namespace, 
            name, 
            storage_class,
            source,
            size,
            secret=None,
            access_modes=['ReadWriteOnce'], 
            bind=True,
            confirmation=False, 
            my_output=None, 
            my_k8s_output=None,
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Data Volume ready for upload', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- access mode: %s' % (','.join(access_modes)))
            my_output.default('- storage class: %s' % (storage_class))
            my_output.default('- size [%s]' % (size))
            if source is None:
                my_output.default('- ready for upload')
            else:
                my_output.default('- source: %s' % (source))

        if not self.is_storage_class(storage_class):
            if my_output is not None:
                my_output.error('Storage class not found: %s' % (storage_class))
            return False

        if self.is_data_volume(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        body = self.get_data_volume_body(
            namespace, 
            name, 
            storage_class, 
            source,
            access_modes, 
            size, 
            bind=bind,
            secret=secret
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_data_volume_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Data volume created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for data volume...')
    
        if not self.wait_data_volume(namespace, name):
            if my_output is not None:
                my_output.error('Timed out')
            return False
                
        if my_output is not None:
            my_output.default('Wait for data volume upload ready state...')
    
        if not self.wait_data_volume_upload_ready(namespace, name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        if source is None:
            return True
        
        if my_k8s_output is not None:
            info = self.get_data_volume(namespace, name, cache_enabled=False)
            my_k8s_output.print_data_volumes([info])

        if my_output is not None:
            my_output.default('Wait for data uploaded...')

        if not self.wait_data_volume_uploaded(namespace, name, my_output=my_output):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
