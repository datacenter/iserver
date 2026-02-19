class K8sSecretDelete():
    def __init__(self):
        pass

    def delete_secret(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Secret', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_secret(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_secret_mo(namespace, name):
            if my_output is not None:
                my_output.error('Failed to delete secret')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no secret')

            if not self.wait_no_secret(namespace, name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    