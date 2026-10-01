class K8sVastDriverCreate():
    def __init__(self):
        pass

    def get_vast_driver_body(
            self, 
            namespace,
            name,
            driver_type, 
            repository,
            extras={}
        ):
        body = {}
        body['apiVersion'] = 'storage.vastdata.com/v1'
        body['kind'] = 'VastCSIDriver'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['driverType'] = driver_type
        body['spec']['image'] = {}
        body['spec']['image']['csiVastPlugin'] = {}
        body['spec']['image']['csiVastPlugin']['repository'] = repository

        for key in extras:
            body['spec'][key] = extras[key]

        return body

    def create_vast_driver(
            self, 
            namespace,
            name,
            driver_type, 
            repository,
            extras={},
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_vast_driver_body(
            namespace,
            name,
            driver_type, 
            repository,
            extras=extras
        )
        return self.create_vast_driver_from_body(
            body,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )
    
    def create_vast_driver_from_body(
        self, 
        body,
        confirmation=False, 
        my_output=None, 
        wait=True
    ):
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')

        success = self.create_resource_and_wait(
            body, 
            'vast_driver', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_vast_driver(
            namespace,
            name,
            match_properties={'initialized_status':'True'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_vast_driver(
            namespace,
            name,
            match_properties={'deployed_status':'True'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False

        info = self.get_vast_driver(
            namespace,
            name,
            cache_enabled=False
        )
        if info is None:
            if my_output is not None:
                my_output.error('Exception: no object found')
            return False
        
        success = self.wait_vast_driver_resources(
            info['resource'],
            my_output=my_output
        )
        
        return success