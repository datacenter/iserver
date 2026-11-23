class K8sCephFilesystemMirrorInfo():
    def __init__(self):
        self.ceph_filesystem_mirror = None

    def get_ceph_filesystem_mirror_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_ceph_filesystem_mirrors(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_filesystem_mirror', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_filesystem_mirror(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_filesystem_mirror', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_filesystem_mirror(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_filesystem_mirror(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_filesystem_mirror(self, cache_enabled=True):
        infos = self.get_ceph_filesystem_mirrors(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True