class K8sHyperConvergedDelete():
    def __init__(self):
        pass
    
    def delete_hyperconverged(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete HyperConverged Instance', before_newline=True, underline=True)

        info = self.get_hyperconverged(cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if my_output is not None:
            my_output.default('- namespace: %s' % (info['namespace']))
            my_output.default('- name: %s' % (info['name']))
        
        success = self.delete_hyperconverged_mo(info['namespace'], info['name'])
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no hyperconverged instance and resources')

        success = self.wait_no_hyperconverged_resources()
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
