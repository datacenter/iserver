class K8sPodDelete():
    def __init__(self):
        pass
    
    def delete_pod(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Pod', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_pod(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        success = self.delete_pod_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no pod')

        success = self.wait_no_pod(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
