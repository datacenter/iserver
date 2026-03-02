class K8sVastStorageCreate():
    def __init__(self):
        pass

    def get_vast_storage_body(
            self, 
            namespace,
            name,
            driver_type,
            provisioner,
            secret_namespace,
            secret_name, 
            extras={}
        ):
        body = {}
        body['apiVersion'] = 'storage.vastdata.com/v1'
        body['kind'] = 'VastStorage'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['driverType'] = driver_type
        body['spec']['provisioner'] = provisioner
        body['spec']['secretName'] = secret_name
        body['spec']['secretNamespace'] = secret_namespace

        for key in extras:
            body['spec'][key] = extras[key]

        return body

    def create_vast_storage(
            self, 
            namespace,
            name,
            driver_type,
            provisioner,
            secret_namespace,
            secret_name, 
            extras={},
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_vast_storage_body(
            namespace,
            name,
            driver_type,
            provisioner,
            secret_namespace,
            secret_name, 
            extras=extras
        )
        if not self.create_resource(body, object_name='vast_storage', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_vast_storage(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_vast_storage(
            namespace,
            name,
            match_properties={'initialized_status':'True'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_vast_storage(
            namespace,
            name,
            match_properties={'deployed_status':'True'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False

        return True
