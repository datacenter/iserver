class K8sPvDelete():
    def __init__(self):
        pass

    def remove_pv_finalizers(self, name, my_output=None):
        pv_mo = self.get_pv(name, return_mo=True, cache_enabled=False)
        if pv_mo is None:
            return False
        
        if 'finalizers' not in pv_mo['metadata']:
            return True
        
        del pv_mo['metadata']['finalizers']
        return self.replace_resource(pv_mo, my_output=my_output)
        
    def delete_pv(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Persistent Volume', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        info = self.get_pv(name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if info['phase'] not in ['Released']:
            if my_output is not None:
                my_output.default('- unexpected phase: %s' % (my_output.add_color(info['phase'], 'Red')))
            return False
        
        success = self.delete_pv_mo(name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no pv')

        success = self.wait_no_pv(name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')

            success = self.remove_pv_finalizers(name, my_output=my_output)
            if not success:
                return False
            
            success = self.wait_no_pv(name, my_output=my_output)
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')

                return False
        
        return True
