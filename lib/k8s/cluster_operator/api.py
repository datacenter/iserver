class K8sClusterOperatorApi():
    def __init__(self):
        self.cluster_operator_mo = None

    def get_cluster_operator_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_operator_mo
        )
        if cache_hit:
            return response

        response, self.cluster_operator_mo = self.get_resources(
            'ClusterOperator', 
            'config.openshift.io/v1', 
            self.cluster_operator_mo,
            name=name
        )

        return response
    