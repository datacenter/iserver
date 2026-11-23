class K8sProviderDelete():
    def __init__(self):
        pass
        
    def delete_provider(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Provider', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
                              
        provider_info = self.get_provider(namespace, name, cache_enabled=False)
        if provider_info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_provider_mo(namespace, name):
            if my_output is not None:
                my_output.error('Provider REST API failed')
            return False
        
        if provider_info['secret_namespace'] is not None:
            if not self.delete_secret_mo(provider_info['secret_namespace'], provider_info['secret_name']):
                if my_output is not None:
                    my_output.error('Secret REST API failed')
                return False

        if my_output is not None:
            my_output.default('Provider and secret deleted', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for no provider...')

        if not self.wait_no_provider(namespace, name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    