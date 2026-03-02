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
        if not self.create_resource(body, object_name='vast_driver', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_vast_driver(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
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
