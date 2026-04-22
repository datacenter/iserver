class K8sConfigMapCreate():
    def __init__(self):
        pass

    def get_create_config_map_body(
            self, 
            namespace, 
            name,
            content, 
            labels=None
        ):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'ConfigMap'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if labels is not None:
            body['metadata']['labels'] = {}
            for key in labels:
                body['metadata']['labels'][key] = labels[key]
        body['data'] = {}
        for key in content:
            body['data'][key] = content[key]

        return body
    
    def create_config_map(
            self, 
            namespace, 
            name,
            content, 
            labels=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_create_config_map_body(
            namespace, 
            name,
            content, 
            labels=labels
        )
        if not self.create_resource(body, object_name='config_map', my_output=my_output, confirmation=confirmation):
            return False

        if not wait:
            return True

        success = self.wait_config_map(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True

    def create_or_update_config_map(
            self, 
            namespace, 
            name,
            content, 
            labels=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_config_map(namespace, name, cache_enabled=False):
            return self.update_config_map(
                namespace, 
                name,
                content, 
                confirmation=confirmation, 
                my_output=my_output
            )
        
        return self.create_config_map(
            namespace, 
            name,
            content, 
            labels=labels,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
    