from lib import filter_helper


class K8sNimBuildInfo():
    def __init__(self):
        self.nim_build = None

    def get_nim_build_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_nim_builds(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nim_build', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_nim_build(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'nim_build', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_nim_build(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nim_build(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_nim_build(self, cache_enabled=True):
        infos = self.get_nim_builds(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True