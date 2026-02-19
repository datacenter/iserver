class K8sDataVolumeDelete():
    def __init__(self):
        pass
    
    def delete_data_volume(self, namespace, name, my_output=None, wait=True, force=False):
        if my_output is not None:
            my_output.default('Delete Data Volume', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_data_volume(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not info['used']:
            if my_output is not None:
                my_output.default('- used: %s' % (info['used']))

        if info['used']:
            if not force:
                if my_output is not None:
                    my_output.default('- used: %s (skip)' % (info['used']))
                return False

            if my_output is not None:
                my_output.default('- used: %s (force)' % (info['used']))

        success = self.delete_data_volume_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no data volume')

        success = self.wait_no_data_volume(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        if my_output is not None:
            my_output.default('- wait for no pvc')

        success = self.wait_no_pvc(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
