class K8sCephBlockPoolInfo():
    def __init__(self):
        self.ceph_block_pool = None

    def get_ceph_block_pool_info(self, managed_object):
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

        info['pool_id'] = self.get(managed_object, 'status:poolID')
        info['failure_domain'] = self.get(managed_object, 'status:info:failureDomain')
        info['type'] = self.get(managed_object, 'status:info:type')

        return info

    def get_ceph_block_pools(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_block_pool', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_block_pool(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_block_pool', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_block_pool(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_block_pool(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_block_pool(self, cache_enabled=True):
        infos = self.get_ceph_block_pools(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True