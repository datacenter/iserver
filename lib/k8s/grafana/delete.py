class K8sGrafanaDelete():
    def __init__(self):
        pass

    def delete_grafana(
            self, 
            namespace, 
            name,
            my_output=None, 
            wait=True
        ):
        if my_output is not None:
            my_output.default('Delete Grafana Instance', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (namespace))

        if not self.is_grafana(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_grafana_mo(namespace, name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until grafana gone [timeout:60s]...')

        success = self.wait_no_grafana(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if my_output is not None:
            my_output.default('Wait until grafana resources are gone [timeout:60s]...')

        success = self.wait_no_grafana_resources(namespace, name, my_output=my_output)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if my_output is not None:
            my_output.default('Wait for no service account...')

        success = self.wait_no_service_account(namespace, '%s-sa' % (name))
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
    
        return True
