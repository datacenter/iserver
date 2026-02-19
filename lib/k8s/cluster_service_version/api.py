import time
import traceback


class K8sClusterServiceVersionApi():
    def __init__(self):
        self.cluster_service_version_mo = None
        self.cluster_service_version_namespace_mo = {}

    def get_cluster_service_version_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.cluster_service_version_mo,
            self.cluster_service_version_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.cluster_service_version_mo, self.cluster_service_version_namespace_mo = self.get_namespaced_resources(
            'ClusterServiceVersion', 
            'operators.coreos.com/v1alpha1', 
            self.cluster_service_version_mo,
            self.cluster_service_version_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_cluster_service_version_mo(self, namespace, name):
        return self.delete_resource('ClusterServiceVersion', 'operators.coreos.com/v1alpha1', name, namespace=namespace)
