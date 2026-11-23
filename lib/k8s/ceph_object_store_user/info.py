class K8sCephObjectStoreUserInfo():
    def __init__(self):
        self.ceph_object_store_user = None

    def get_ceph_object_store_user_info(self, managed_object):
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

        info['secret'] = self.get(managed_object, 'status:info:secretName')
        return info

    def get_ceph_object_store_users(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_object_store_user', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_object_store_user(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_object_store_user', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_object_store_user(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_object_store_user(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_object_store_user(self, cache_enabled=True):
        infos = self.get_ceph_object_store_users(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True