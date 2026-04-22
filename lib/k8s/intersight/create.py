class K8sIntersightCreate():
    def __init__(self):
        pass

    def get_intersight_body(self, namespace, name, ucs_tool=False, resource_version=None):
        body = {}
        body['apiVersion'] = 'intersight.cisco.com/v1'
        body['kind'] = 'CiscoIntersight'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if resource_version is not None:
            body['metadata']['resourceVersion'] = resource_version
        body['spec'] = {}
        body['spec']['OsDiscoveryToolInstall'] = ucs_tool
        return body

    def create_intersight(self, body, my_output=None, confirmation=False, wait=True):
        if not self.create_resource(body, object_name='intersight', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_intersight(
            body['metadata']['namespace'],
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_subscription_intersight_ready(my_output=my_output, with_instance=True, ucs_tool=self.get(body, 'spec:OsDiscoveryToolInstall'))
        if not success:
            return False
        
        return True
    
    def create_or_update_intersight(
            self, 
            body, 
            replace=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_intersight(body['metadata']['namespace'], body['metadata']['name'], cache_enabled=False):
            return self.update_intersight(
                body,
                replace=replace,
                confirmation=confirmation, 
                my_output=my_output
            )

        return self.create_intersight(
            body,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )