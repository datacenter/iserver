import yaml
from menu.common import get_confirmation


class K8sStorageMapCreate():
    def __init__(self):
        pass

    def get_storage_map_body(self, namespace, name, source, destination, nmap):
        body = {}
        body['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        body['kind'] = 'StorageMap'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['provider'] = {}

        provider = {}
        provider['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        provider['kind'] = 'Provider'
        provider['namespace'] = namespace
        provider['name'] = source
        body['spec']['provider']['source'] = provider

        provider = {}
        provider['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        provider['kind'] = 'Provider'
        provider['namespace'] = namespace
        provider['name'] = destination
        body['spec']['provider']['destination'] = provider

        body['spec']['map'] = []

        for item in nmap:
            map_mo = {}
            map_mo['source'] = {}
            map_mo['source']['name'] = item['source']

            map_mo['destination'] = {}
            map_mo['destination']['storageClass'] = item['destination']

            body['spec']['map'].append(map_mo)

        return body
    
    def create_storage_map(self, namespace, name, source, destination, nmap, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Storage Map', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
                              
        if self.is_storage_map(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        map_body = self.get_storage_map_body(
            namespace, 
            name, 
            source, 
            destination,
            nmap
        )

        if my_output is not None:
            my_output.default(
                yaml.dump(map_body),
                before_newline=True, 
                wrap='~~~'
            )

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_storage_map_mo(map_body):
            if my_output is not None:
                my_output.error('Provider REST API failed')
            return False
                
        if my_output is not None:
            my_output.default('Storage map created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for storage map...')

        if not self.wait_storage_map(namespace, name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for storage map ready state...')

        if not self.wait_storage_map_ready(namespace, name):
            info = self.get_storage_map(namespace, name)
            if info['invalid']:
                if my_output is not None:
                    my_output.error('invalid source or destination storage definition')
                return False
            
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    