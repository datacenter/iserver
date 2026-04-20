import base64


class K8sBareMetalHostSecret():
    def __init__(self):
        pass

    def get_bare_metal_host_secret_body(
            self,
            namespace, 
            name,
            username,
            password, 
            labels={},
            secret_type='Opaque'
    ):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Secret'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['metadata']['labels'] = {}
        body['metadata']['labels']['environment.metal3.io'] = 'baremetal'
        for key in labels:
            body['metadata']['labels'][key] = labels[key]
        body['type'] = secret_type
        body['data'] = {}

        body['data']['username'] = base64.b64encode(
            username.encode('utf-8')
        ).decode('utf-8')
        body['data']['password'] = base64.b64encode(
            password.encode('utf-8')
        ).decode('utf-8')
        return body

    def set_bare_metal_host_secret(
            self, 
            namespace, 
            name,
            username,
            password, 
            labels={},
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_bare_metal_host_secret_body(
            namespace,
            name,
            username,
            password, 
            labels=labels
        )

        secret_mo = self.get_secret(namespace, name, return_mo=True, cache_enabled=False)
        if secret_mo is None:
            if not self.create_resource(body, object_name='secret', my_output=my_output, confirmation=confirmation):
                return False
        else:
            body['metadata']['resource_version'] = secret_mo['metadata']['resourceVersion']
            if not self.replace_resource(body, object_name='secret', my_output=my_output, confirmation=confirmation):
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
