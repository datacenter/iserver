class K8sPrometheusRuleApi():
    def __init__(self):
        self.prometheus_rule_mo = None
        self.prometheus_rule_namespace_mo = {}

    def get_prometheus_rule_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.prometheus_rule_mo,
            self.prometheus_rule_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.prometheus_rule_mo, self.prometheus_rule_namespace_mo = self.get_namespaced_resources(
            'PrometheusRule', 
            'monitoring.coreos.com/v1', 
            self.prometheus_rule_mo,
            self.prometheus_rule_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response