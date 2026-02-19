class K8sConfigMapDelete():
    def __init__(self):
        pass

    def delete_config_map(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Config Map', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_config_map(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_config_map_mo(namespace, name):
            if my_output is not None:
                my_output.error('Failed to delete config map')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no config map')

            if not self.wait_no_config_map(namespace, name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True