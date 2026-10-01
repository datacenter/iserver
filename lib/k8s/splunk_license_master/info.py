class K8sSplunkLicenseMasterInfo():
    def __init__(self):
        self.splunk_license_master = None

    def get_splunk_license_master_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_splunk_license_masters(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_license_master', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_splunk_license_master(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_license_master', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_splunk_license_master(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_license_master(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_splunk_license_master(self, cache_enabled=True):
        infos = self.get_splunk_license_masters(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True