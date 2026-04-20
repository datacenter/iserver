class K8sBareMetalHostDetach():
    def __init__(self):
        pass

    def get_bare_metal_host_detached_body(self, namespace, name):
        body = {}
        body['apiVersion'] = 'metal3.io/v1alpha1'
        body['kind'] = 'BareMetalHost'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['metadata']['annotations'] = {}
        body['metadata']['annotations']['baremetalhost.metal3.io/detached'] = ''
        return body

    def set_bare_metal_host_detached(
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
        
        if info['provisioning_state'] not in ['available', 'externally provisioned', 'provisioned']:
            if my_output is not None:
                my_output.default(
                    'Bare metal host %s provisioning state %s must be one of available, externally provisioned, provisioned' % (
                        name, 
                        my_output.add_color(info['provisioning_state'], 'Red')
                    )
                )
            return False
        
        annotation = self.get(info, 'annotation:baremetalhost.metal3.io/detached')
        if annotation is not None:
            if my_output is not None:
                my_output.default('Bare metal host %s annotation %s already defined' % (name, my_output.add_color('baremetalhost.metal3.io/detached', 'Green')))
                if not info['detached']:
                    my_output.default('Operational status %s' % (my_output.add_color(self.get(info, 'status:operationalStatus'), 'Red')))
                    return False
                my_output.default('Operational status %s' % (my_output.add_color(self.get(info, 'status:operationalStatus'), 'Green')))
            return True
        
        body = self.get_bare_metal_host_detached_body(
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
            match_properties={'operational_state':'detached'},
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False
        
        return True    
