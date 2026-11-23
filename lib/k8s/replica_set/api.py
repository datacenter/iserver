class K8sReplicaSetApi():
    def __init__(self):
        self.replica_set_mo = None
        self.replica_set_namespace_mo = {}

    def get_replica_set_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.replica_set_mo,
            self.replica_set_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.replica_set_mo, self.replica_set_namespace_mo = self.get_namespaced_resources(
            'ReplicaSet', 
            'apps/v1', 
            self.replica_set_mo,
            self.replica_set_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response