class K8sEgressIpApi():
    def __init__(self):
        self.egress_ip_mo = None

    def get_egress_ip_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.egress_ip_mo
        )
        if cache_hit:
            return response

        response, self.egress_ip_mo = self.get_resources(
            'EgressIP', 
            'k8s.ovn.org/v1', 
            self.egress_ip_mo,
            name=name
        )

        return response