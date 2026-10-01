from lib import filter_helper


class K8sClusterQuotaInfo():
    def __init__(self):
        self.cluster_quota = None

    def get_cluster_quota_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_cluster_quotas(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cluster_quota', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_cluster_quota(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cluster_quota', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_cluster_quota(self, name, cache_enabled=True, optimized=True):
        if self.get_cluster_quota(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_cluster_quota(self, cache_enabled=True):
        infos = self.get_cluster_quotas(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True