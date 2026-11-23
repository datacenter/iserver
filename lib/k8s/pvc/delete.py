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

    def delete_namespaced_pvcs(self, namespace, my_output=None, wait=True):
        pvcs = self.get_pvcs(object_filter=['namespace:%s' % (namespace)], cache_enabled=False)
        if pvcs is None:
            if my_output is not None:
                my_output.error('Failed to get pvcs')
            return False

        for pvc in pvcs:
            success = self.delete_pvc(
                pvc['namespace'],
                pvc['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True