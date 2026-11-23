class K8sSecretUpdate():
    def __init__(self):
        pass

    def get_update_secret_kv_body(
            self,
            namespace, 
            name,
            data, 
            secret_type='Opaque'
    ):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Secret'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['type'] = secret_type
        body['data'] = data
        return body
        
    def update_secret_kv(
            self, 
            namespace, 
            name,
            data, 
            secret_type='Opaque',
            replace=True,
            confirmation=False, 
            my_output=None
        ):
        body = self.get_update_secret_kv_body(
            namespace,
            name,
            data, 
            secret_type=secret_type
        )
        if replace:
            if not self.replace_resource(body, object_name='secret', my_output=my_output, confirmation=confirmation):
                return False
        else:
            if not self.patch_resource(body, object_name='secret', my_output=my_output, confirmation=confirmation):
                return False

        return True    
