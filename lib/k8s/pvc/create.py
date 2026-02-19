import yaml
from menu.common import get_confirmation


class K8sPvcCreate():
    def __init__(self):
        pass

    def get_pvc_body(self, namespace, name, volume_mode, storage_class, requests, limits):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'PersistentVolumeClaim'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['accessModes'] = ['ReadWriteOnce']
        body['spec']['volumeMode'] = volume_mode
        body['spec']['resources'] = {}
        body['spec']['resources']['requests'] = dict(storage=requests)
        body['spec']['resources']['limits'] = dict(storage=limits)
        body['spec']['storageClassName'] = storage_class
        return body

    def create_pvc(
            self, 
            namespace, 
            name, 
            volume_mode,
            storage_class, 
            requests, 
            limits,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Persistent Volume Claim', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- volume mode: %s' % (volume_mode))
            my_output.default('- storage class: %s' % (storage_class))
            my_output.default('- requests [%s] limits [%s]' % (requests, limits))
        
        if not self.is_namespace(namespace):
            if my_output is not None:
                my_output.error('namespace not found')
            return False
        
        if self.is_pvc(namespace, name):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        body = self.get_pvc_body(
            namespace, 
            name, 
            volume_mode,
            storage_class, 
            requests, 
            limits
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_pvc_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Persistent volume claim created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for pvc...')
    
        if not self.wait_pvc(namespace, name):
            if my_output is not None:
                my_output.error('Timed out')
            return False
                
        if my_output is not None:
            my_output.default('Wait for pvc pending or bound...')
    
        if not self.wait_pvc_phase(namespace, name, ['Pending', 'Bound']):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
