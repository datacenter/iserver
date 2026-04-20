class K8sBareMetalHostCreate():
    def __init__(self):
        pass

    def get_bare_metal_host_body(
            self,
            namespace, 
            name, 
            bmc,
            cert,
            mac,
            boot_mode,
            server_type=None,
            serial=None
        ):
        address = bmc
        if server_type == 'ucsc' and serial is not None:
            address = 'redfish-virtualmedia://%s/redfish/v1/Systems/%s' % (
                bmc,
                serial
            )

        body = {}
        body['apiVersion'] = 'metal3.io/v1alpha1'
        body['kind'] = 'BareMetalHost'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['online'] = True
        body['spec']['bmc'] = {}
        body['spec']['bmc']['address'] = address
        body['spec']['bmc']['credentialsName'] = '%s-bmc-secret' % (name)
        body['spec']['bmc']['disableCertificateVerification'] = not cert
        body['spec']['bootMACAddress'] = mac
        body['spec']['bootMode'] = 'Legacy'
        if boot_mode == 'uefi':
            body['spec']['bootMode'] = 'UEFI'
        if boot_mode == 'secure':
            body['spec']['bootMode'] = 'UEFISecureBoot'
        
        return body
    
    def create_bare_metal_host(
            self, 
            namespace, 
            name, 
            bmc,
            username,
            password,
            cert,
            mac,
            boot_mode,
            server_type=None,
            serial=None,
            my_output=None, 
            confirmation=False,
            wait=True
        ):
        success = self.set_bare_metal_host_secret(
            namespace,
            '%s-bmc-secret' % (name),
            username,
            password,
            my_output=my_output,
            confirmation=confirmation,
            wait=wait
        )
        if not success:
            return False
                
        body = self.get_bare_metal_host_body(
            namespace, 
            name, 
            bmc,
            cert,
            mac,
            boot_mode,
            server_type=server_type,
            serial=serial
        )

        if not self.create_resource(body, object_name='bare_metal_host', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_bare_metal_host(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'provisioning_state':'registering'},
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False
                                    
        success = self.wait_bare_metal_host(
            namespace,
            name,
            match_properties={'provisioning_state':'inspecting'},
            max_time=180,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
