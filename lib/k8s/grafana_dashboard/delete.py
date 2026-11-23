class K8sGrafanaDashboardDelete():
    def __init__(self):
        pass

    def delete_grafana_dashboard(
            self, 
            namespace, 
            name,
            my_output=None, 
            wait=True
        ):
        if my_output is not None:
            my_output.default('Delete Grafana Dashboard', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_grafana_dashboard(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_grafana_dashboard_mo(namespace, name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until grafana dashboard gone [timeout:60s]...')

        success = self.wait_no_grafana_dashboard(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
    
        return True
