import yaml
from menu.common import get_confirmation


class K8sForkliftControllerDelete():
    def __init__(self):
        pass
        
    def delete_forklift_controller(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Forklift Controller', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
                              
        if not self.is_forklift_controller(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_forklift_controller_mo(namespace, name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Forklift controller instance deleted', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for no forklift controller instance...')

        if not self.wait_no_forklift_controller(namespace, name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for no forklift controller instance resources...')

        if not self.wait_no_instance_mtv(my_output=my_output):
            if my_output is not None:
                my_output.error('timed out')
            return False
        
        return True    
    