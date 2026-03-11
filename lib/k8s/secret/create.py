class K8sSecretCreate():
    def __init__(self):
        pass

    def get_create_secret_kv_body(
            self,
            namespace, 
            name,
            data, 
            labels={},
            secret_type='Opaque'
    ):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Secret'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if len(labels) > 0:
            body['metadata']['labels'] = {}
            for key in labels:
                body['metadata']['labels'][key] = labels[key]

        body['type'] = secret_type
        body['data'] = data
        return body

    def create_secret_kv(
            self, 
            namespace, 
            name,
            data, 
            labels={},
            secret_type='Opaque',
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_create_secret_kv_body(
            namespace,
            name,
            data, 
            labels=labels,
            secret_type=secret_type
        )
        if not self.create_resource(body, object_name='secret', my_output=my_output, confirmation=confirmation):
            return False

        if not wait:
            return True

        success = self.wait_secret(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True    

    def create_or_update_secret_kv(
            self, 
            namespace, 
            name,
            data, 
            labels={},
            secret_type='Opaque',
            replace=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_secret(namespace, name, cache_enabled=False):
            return self.update_secret_kv(
                namespace, 
                name,
                data, 
                secret_type=secret_type,
                replace=replace,
                confirmation=confirmation, 
                my_output=my_output
            )
        
        return self.create_secret_kv(
            namespace, 
            name,
            data, 
            labels=labels,
            secret_type=secret_type,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )
