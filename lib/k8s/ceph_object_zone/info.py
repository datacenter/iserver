class K8sCephObjectZoneInfo():
    def __init__(self):
        self.ceph_object_zone = None

    def get_ceph_object_zone_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_ceph_object_zones(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_object_zone', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_object_zone(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_object_zone', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_object_zone(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_object_zone(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_object_zone(self, cache_enabled=True):
        infos = self.get_ceph_object_zones(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True