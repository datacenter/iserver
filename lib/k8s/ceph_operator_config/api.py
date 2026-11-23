class K8sCephOperatorConfigApi():
    def __init__(self):
        self.ceph_operator_config_mo = None
        self.ceph_operator_config_namespace_mo = {}

    def get_ceph_operator_config_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ceph_operator_config_mo,
            self.ceph_operator_config_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ceph_operator_config_mo, self.ceph_operator_config_namespace_mo = self.get_namespaced_resources(
            'OperatorConfig', 
            'csi.ceph.io/v1alpha1', 
            self.ceph_operator_config_mo,
            self.ceph_operator_config_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response