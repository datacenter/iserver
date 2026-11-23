import base64


class K8sBareMetalHostBmc():
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

    def set_bare_metal_host_bmc(
            self, 
            namespace, 
            name,
            server_type,
            secret,
            address,
            cert, 
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        managed_object = self.get_bare_metal_host(
            namespace,
            name,
            return_mo=True,
            cache_enabled=False
        )
        if managed_object is None:
            if my_output is not None:
                my_output.default('Bare metal host %s %s' % (name, my_output.add_color('not found', 'Red')))
            return False
        
        status = self.get(managed_object, 'status')
        managed_object = self.cleanup_managed_object(managed_object, exclude=['resourceVersion'])
        managed_object['spec'] = {}
        managed_object['spec']['bmc'] = {}
        if server_type == 'ucsc':
            serial = self.get(status, 'hardware:systemVendor:serialNumber')
            if serial is None:
                if my_output is not None:
                    my_output.default('Bare metal host %s serial number %s' % (name, my_output.add_color('not found', 'Red')))
                return False

            managed_object['spec']['bmc']['address'] = 'redfish-virtualmedia://%s/redfish/v1/Systems/%s' % (
                address,
                serial
            )

        managed_object['spec']['bmc']['credentialsName'] = secret
        managed_object['spec']['bmc']['disableCertificateVerification'] = not cert

        if not self.patch_resource(managed_object, object_name='bare_metal_host', my_output=my_output, confirmation=confirmation):
            return False

        if not wait:
            return True

        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'operational_state':'OK'},
            max_time=600,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'provisioning_state':'externally provisioned'},
            max_time=600,
            my_output=my_output
        )
        if not success:
            return False
                
        return True    
