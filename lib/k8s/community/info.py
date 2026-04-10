class K8sCommunityInfo():
    def __init__(self):
        self.community = None

    def get_community_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_communitys(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'community', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_community(self, namespace, name, cache_enabled=True):
        if self.get_community(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_community(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'community', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
