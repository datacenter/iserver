import yaml
from menu.common import get_confirmation


class K8sServiceCreate():
    def __init__(self):
        pass
    
    def create_service(
            self, 
            namespace, 
            name, 
            body,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Service', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))            

        if self.is_service(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_service_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until service found [timeout:60s]...')

        success = self.wait_service(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        return True
