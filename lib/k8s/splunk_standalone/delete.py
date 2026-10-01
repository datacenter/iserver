class K8sSplunkStandaloneDelete():
    def __init__(self):
        pass

    def remove_splunk_standalone_finalizers(self, namespace, name):
        standalone_mo = self.get_splunk_standalone(namespace, name, return_mo=True, cache_enabled=False)
        if standalone_mo is None:
            return False
        
        modified = False
        if 'finalizers' in standalone_mo['spec']:
            del standalone_mo['spec']['finalizers']
            modified = True

        if 'finalizers' in standalone_mo['metadata']:
            del standalone_mo['metadata']['finalizers']
            modified = True

        if not modified:
            return True
        
        return self.replace_resource(standalone_mo)
    
    def delete_splunk_standalone(
            self, 
            namespace, 
            name,
            my_output=None, 
            wait=True,
            finalizers=True
        ):
        success, deleted = self.delete_resource(
            'Standalone', 
            'enterprise.splunk.com/v4',
            name, 
            namespace=namespace, 
            object_name='splunk_standalone',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True
        
        success = self.wait_no_pod(
            namespace, 
            'splunk-%s-standalone-0' % (name), 
            max_time=300, 
            my_output=my_output
        )
        if not success:
            return False
        
        if not self.wait_no_splunk_standalone(namespace, name, my_output=my_output):
            if not finalizers:
                return False

            if my_output is not None:
                my_output.default('Remove finalizers')

            if not self.remove_splunk_standalone_finalizers(namespace, name):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
            
            if not self.wait_no_splunk_standalone(namespace, name, my_output=my_output):
                if my_output is not None:
                    my_output.error('Giving up')
                return False
            
        return True    