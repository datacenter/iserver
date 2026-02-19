import yaml
from menu.common import get_confirmation


class K8sPlanCreate():
    def __init__(self):
        pass

    def get_plan_body(self, namespace, name, source, destination, nmap, smap, vms, target_namespace, migration_type):
        body = {}
        body['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        body['kind'] = 'Plan'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}

        body['spec']['provider'] = {}

        provider = {}
        provider['namespace'] = namespace
        provider['name'] = source
        body['spec']['provider']['source'] = provider

        provider = {}
        provider['namespace'] = namespace
        provider['name'] = destination
        body['spec']['provider']['destination'] = provider

        body['spec']['map'] = {}

        map_ref = {}
        map_ref['namespace'] = namespace
        map_ref['name'] = nmap
        body['spec']['map']['network'] = map_ref

        map_ref = {}
        map_ref['namespace'] = namespace
        map_ref['name'] = smap
        body['spec']['map']['storage'] = map_ref

        body['spec']['vms'] = []
        for vm_name in vms:
            body['spec']['vms'].append(dict(name=vm_name))

        body['spec']['type'] = migration_type
        body['spec']['targetNamespace'] = target_namespace
        return body
    
    def create_plan(self, namespace, name, source, destination, nmap, smap, vms, target_namespace, migration_type, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Migration Plan', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
                              
        if self.is_plan(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        body = self.get_plan_body(
            namespace, 
            name, 
            source, 
            destination, 
            nmap,
            smap, 
            vms, 
            target_namespace, 
            migration_type
        )

        if my_output is not None:
            my_output.default(
                yaml.dump(body),
                before_newline=True, 
                wrap='~~~'
            )

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_plan_mo(body):
            if my_output is not None:
                my_output.error('Plan REST API failed')
            return False
                
        if my_output is not None:
            my_output.default('Plan created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for plan...')

        if not self.wait_plan(namespace, name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for plan ready state...')

        if not self.wait_plan_ready(namespace, name):
            info = self.get_plan(namespace, name)
            if not info['vms_found']:
                if my_output is not None:
                    my_output.error('invalid source vms')
                return False            
            
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    