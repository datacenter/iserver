class K8sStorageMapDelete():
    def __init__(self):
        pass
        
    def delete_storage_map(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Storage Map', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
                              
        storage_map_info = self.get_storage_map(namespace, name, cache_enabled=False)
        if storage_map_info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_storage_map_mo(namespace, name):
            if my_output is not None:
                my_output.error('Provider REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Storage map deleted', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for no storage map...')

        if not self.wait_no_storage_map(namespace, name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    