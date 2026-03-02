import yaml
from menu.common import get_confirmation


class K8sPodCreate():
    def __init__(self):
        pass
    
    def create_pod(
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
            my_output.default('Create Pod', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))            

        if self.is_pod(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_resource(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        my_output.default('Create pod rest api successful')
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until pod running [timeout:600s]...')

        success = self.wait_pod_phase(namespace, name, 'Running', max_time=600)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        return True
