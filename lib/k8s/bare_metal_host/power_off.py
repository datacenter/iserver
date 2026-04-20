class K8sBareMetalHostPowerOff():
    def __init__(self):
        pass

    def get_bare_metal_host_power_off_body(self, namespace, name):
        body = {}
        body['apiVersion'] = 'metal3.io/v1alpha1'
        body['kind'] = 'BareMetalHost'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['online'] = False
        return body

    def set_bare_metal_host_power_off(
            self, 
            namespace, 
            name,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        info = self.get_bare_metal_host(
            namespace,
            name,
            cache_enabled=False
        )
        if info is None:
            if my_output is not None:
                my_output.default('Bare metal host %s %s' % (name, my_output.add_color('not found', 'Red')))
            return False

        if not info['online']:
            my_output.default('Bare metal host %s %s' % (name, my_output.add_color('already powered off', 'Green')))
            return True
                        
        body = self.get_bare_metal_host_power_off_body(
            namespace, 
            name
        )
        if not self.patch_resource(body, object_name='bare_metal_host', my_output=my_output, confirmation=confirmation):
            return False

        if not wait:
            return True

        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'online':False},
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False
              
        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'power':False},
            max_time=600,
            my_output=my_output
        )
        if not success:
            return False

        return True    
