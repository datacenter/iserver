class K8sBgpSessionStateApi():
    def __init__(self):
        self.bgp_session_state_mo = None
        self.bgp_session_state_namespace_mo = {}

    def get_bgp_session_state_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.bgp_session_state_mo,
            self.bgp_session_state_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.bgp_session_state_mo, self.bgp_session_state_namespace_mo = self.get_namespaced_resources(
            'BGPSessionState', 
            'frrk8s.metallb.io/v1beta1', 
            self.bgp_session_state_mo,
            self.bgp_session_state_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
