class K8sConfigMapInfo():
    def __init__(self):
        self.config_map = None

    def get_config_map_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['data'] = self.get(managed_object, 'data', on_error={}, on_none={})
        info['dataCount'] = len(info['data'])

        return info

    def add_config_maps_pod(self, infos, cache_enabled=False):
        if not cache_enabled:
            self.get_pods(cache_enabled=False)

        for info in infos:
            info['info']['pod'] = []
            pods_info = self.get_pods(
                object_filter=[
                    'cm:%s:%s' % (
                        info['info']['namespace'],
                        info['info']['name']
                    )
                ],
                cache_enabled=True
            )
            if pods_info is not None:
                for pod in pods_info:
                    cm_pod_info = {}
                    cm_pod_info['namespace'] = pod['namespace']
                    cm_pod_info['name'] = pod['name']
                    cm_pod_info['namespace_name'] = '%s/%s' % (pod['namespace'], pod['name'])
                    info['info']['pod'].append(
                        cm_pod_info
                    )

        return infos
    
    def get_config_maps(self, object_filter=None, pod_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'config_map', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            add=dict(pod=pod_info)
        )
        return infos

    def get_config_map_optimized(self, namespace, name, return_mo=False, cache_enabled=True):
        managed_object = self.get_config_map_mo(
            namespace=namespace, 
            name=name, 
            cache_enabled=cache_enabled
        )
        if return_mo:
            return managed_object
        
        if managed_object is None:
            return None
        
        return self.get_config_map_info(managed_object)
    
    def get_config_map(self, namespace, name, return_mo=False, cache_enabled=True, optimize=False):
        if optimize:
            return self.get_config_map_optimized(namespace, name, return_mo=return_mo, cache_enabled=cache_enabled)

        return self.get_info(
            'config_map', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def is_config_map(self, namespace, name, cache_enabled=True, optimize=False):
        config_map = self.get_config_map(
            namespace,
            name,
            cache_enabled=cache_enabled,
            optimize=optimize
        )
        if config_map is None:
            return False
        return True
