class K8sPvcDelete():
    def __init__(self):
        pass
    
    def delete_pvc(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Persistent Volume Claim', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_pvc(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        success = self.delete_pvc_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no pvc')

        success = self.wait_no_pvc(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
