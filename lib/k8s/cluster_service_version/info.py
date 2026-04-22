class K8sClusterServiceVersionInfo():
    def __init__(self):
        self.cluster_service_version = None

    def get_cluster_service_version_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['phase'] = self.get(managed_object, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Succeeded':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        info['display_name'] = self.get(managed_object, 'spec:displayName')
        info['provider_name'] = self.get(managed_object, 'spec:provider:name')
        info['maturity'] = self.get(managed_object, 'spec:maturity')
        info['maturityT'] = info['maturity']
        if info['maturityT'] is None:
            info['maturityT'] = '--'
        info['replaces'] = self.get(managed_object, 'spec:replaces')
        info['version'] = self.get(managed_object, 'spec:version')

        return info

    def get_cluster_service_versions(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cluster_service_version', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
    
    def is_cluster_service_version(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_cluster_service_version(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_cluster_service_version(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        info = self.get_info(
            'cluster_service_version', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
        return info