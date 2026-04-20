class K8sBareMetalHostInspect():
    def __init__(self):
        pass

    def get_bare_metal_host_inspect_body(self, namespace, name):
        body = {}
        body['apiVersion'] = 'metal3.io/v1alpha1'
        body['kind'] = 'BareMetalHost'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['metadata']['annotations'] = {}
        body['metadata']['annotations']['inspect.metal3.io'] = ''
        return body

    def set_bare_metal_host_inspect(
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
        
        annotation = self.get(info, 'inspect.metal3.io')
        if annotation is not None:
            if my_output is not None:
                my_output.default('Bare metal host %s annotation %s already defined' % (name, my_output.add_color('inspect.metal3.io', 'Green')))
                if not info['inspecting']:
                    my_output.default('Operational status %s' % (my_output.add_color(self.get(info, 'provisioning_state'), 'Red')))
                    return False
                my_output.default('Operational status %s' % (my_output.add_color(self.get(info, 'provisioning_state'), 'Green')))
            return True
        
        body = self.get_bare_metal_host_inspect_body(
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
            match_properties={'provisioning_state':'inspecting'},
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'operational_state':'OK'},
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False
                
        return True    
