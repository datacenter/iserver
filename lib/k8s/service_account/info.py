class K8sServiceAccountInfo():
    def __init__(self):
        self.service_account = None

    def get_service_account_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['secret'] = self.get(managed_object, 'secrets', on_error=[], on_none=[])
        info['secretCount'] = len(info['secret'])
        return info

    def get_service_accounts(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'service_account', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_service_account(self, namespace, name, cache_enabled=True):
        if self.get_service_account(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_service_account(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'service_account', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
