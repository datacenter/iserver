class K8sSplunkLicenseMasterApi():
    def __init__(self):
        self.splunk_license_master_mo = None
        self.splunk_license_master_namespace_mo = {}

    def get_splunk_license_master_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.splunk_license_master_mo,
            self.splunk_license_master_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.splunk_license_master_mo, self.splunk_license_master_namespace_mo = self.get_namespaced_resources(
            'LicenseMaster', 
            'enterprise.splunk.com/v3', 
            self.splunk_license_master_mo,
            self.splunk_license_master_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response