class K8sBfdProfileInfo():
    def __init__(self):
        self.bfd_profile = None

    def get_bfd_profile_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_bfd_profiles(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'bfd_profile', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_bfd_profile(self, namespace, name, cache_enabled=True):
        if self.get_bfd_profile(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_bfd_profile(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'bfd_profile', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
