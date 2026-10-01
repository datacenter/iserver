class K8sReplicationControllerApi():
    def __init__(self):
        self.replication_controller_mo = None
        self.replication_controller_namespace_mo = {}

    def get_replication_controller_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.replication_controller_mo,
            self.replication_controller_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.replication_controller_mo, self.replication_controller_namespace_mo = self.get_namespaced_resources(
            'ReplicationController', 
            'v1', 
            self.replication_controller_mo,
            self.replication_controller_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response