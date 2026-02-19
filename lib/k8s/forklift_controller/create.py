import yaml
from menu.common import get_confirmation


class K8sForkliftControllerCreate():
    def __init__(self):
        pass
        
    def create_forklift_controller_from_body(self, body, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Forklift Controller', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (body['metadata']['namespace']))
            my_output.default('- name: %s' % (body['metadata']['name']))
                              
        if self.is_any_forklift_controller(cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_forklift_controller_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Forklift controller instance created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for forklift controller instance...')

        if not self.wait_forklift_controller(body['metadata']['namespace'], body['metadata']['name']):
            if my_output is not None:
                my_output.error('timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for forklift controller instance resources...')

        if not self.wait_instance_mtv_ready(my_output=my_output):
            return False

        if my_output is not None:
            my_output.default('Wait for forklift controller instance ready state...')

        if not self.wait_forklift_controller_ready(body['metadata']['namespace'], body['metadata']['name']):
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    