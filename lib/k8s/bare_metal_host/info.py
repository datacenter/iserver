class K8sBareMetalHostInfo():
    def __init__(self):
        self.bare_metal_host = None

    def get_bare_metal_host_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        
        info['statusT'] = self.get(managed_object, 'status:operationalStatus')
        if info['statusT'] == 'error':
            info['statusT'] = self.get(managed_object, 'status:errorType')
        
        info['operational_state'] = self.get(managed_object, 'status:operationalStatus')
        info['provisioning_state'] = self.get(managed_object, 'status:provisioning:state')
        
        info = self.add_tick(
            info, 
            'status:operationalStatus', 
            'detached', 
            'detachedT', 
            bool_attribute='detached'
        )

        info = self.add_tick(
            info, 
            'status:provisioning:state', 
            'inspecting', 
            'inspectingT', 
            bool_attribute='inspecting'
        )        

        info = self.add_tick(
            info, 
            'status:poweredOn', 
            True, 
            'powerT', 
            bool_attribute='power'
        )

        info = self.add_tick(
            info, 
            'spec:online', 
            True, 
            'onlineT', 
            bool_attribute='online'
        )

        info['serverT'] = []
        info['serverT'].append(
            self.get(managed_object, 'spec:bmc:address', on_error='BMC Address: ---', on_none='BMC Address: ---', on_empty='BMC Address: ---')
        )
        info['serverT'].append(
            self.get(managed_object, 'spec:bmc:credentialsName', on_error='Credentials: ---', on_none='Credentials: ---', on_empty='Credentials: ---')
        )
        disable_cert = self.get(managed_object, 'spec:bmc:disableCertificateVerification', on_error=False, on_none=False)
        if disable_cert:
            info['serverT'].append('Cert verification: \u2717')
        else:
            info['serverT'].append('Cert verification: \u2713')
        info['serverT'].append(
            self.get(managed_object, 'status:hardware:systemVendor:productName', on_error='Product: ---', on_none='Product: ---')
        )
        info['serverT'].append(
            self.get(managed_object, 'status:hardware:systemVendor:serialNumber', on_error='Serial: ---', on_none='Serial: ---')
        )
        return info
    
    def get_bare_metal_hosts(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'bare_metal_host', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_bare_metal_host(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_bare_metal_host(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_bare_metal_host(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'bare_metal_host', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
