class K8sAuthInfo():
    def __init__(self):
        self.auth = None

    def get_auth_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)
        
        info['phase'] = self.get(managed_object, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['admin'] = self.get(managed_object, 'spec:adminGroups', on_error=[], on_none=[])
        info['allowed'] = self.get(managed_object, 'spec:allowedGroups', on_error=[], on_none=[])

        return info

    def get_auths(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'auth', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_auth(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'auth', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_auth(self, name, cache_enabled=True, optimized=True):
        if self.get_auth(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_auth(self, cache_enabled=True):
        infos = self.get_auths(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True