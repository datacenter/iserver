from lib import filter_helper


class K8sIngressConfigInfo():
    def __init__(self):
        self.ingress_config = None

    def get_ingress_config_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)
        info['domain'] = filter_helper.get_attr(managed_object, 'spec:domain')

        return info

    def get_ingress_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ingress_config', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ingress_config(self, name='cluster', return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ingress_config', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )