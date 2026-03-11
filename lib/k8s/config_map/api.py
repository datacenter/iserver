import time
import traceback
from kubernetes import client


class K8sConfigMapApi():
    def __init__(self):
        self.config_map_mo = None
        self.config_map_namespace_mo = {}

    def get_config_map_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.config_map_mo,
            self.config_map_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.config_map_mo, self.config_map_namespace_mo = self.get_namespaced_resources(
            'ConfigMap', 
            'v1', 
            self.config_map_mo,
            self.config_map_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_config_map_mo(self, namespace, name):
        return self.delete_resource('ConfigMap', 'v1', name, namespace=namespace)
