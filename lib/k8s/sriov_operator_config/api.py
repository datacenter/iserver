class K8sSriovOperatorConfigApi():
    def __init__(self):
        self.sriov_operator_config_mo = None
        self.sriov_operator_config_namespace_mo = {}

    def get_sriov_operator_config_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.sriov_operator_config_mo,
            self.sriov_operator_config_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.sriov_operator_config_mo, self.sriov_operator_config_namespace_mo = self.get_namespaced_resources(
            'SriovOperatorConfig', 
            'sriovnetwork.openshift.io/v1', 
            self.sriov_operator_config_mo,
            self.sriov_operator_config_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_sriov_operator_config_mo(self, namespace, name):
        success, _ = self.delete_resource('SriovOperatorConfig', 'sriovnetwork.openshift.io/v1', name, namespace=namespace)
        return success