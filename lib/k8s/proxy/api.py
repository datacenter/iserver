import time
import traceback


class K8sProxyApi():
    def __init__(self):
        self.proxy_mo = None

    def get_proxy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.proxy_mo
        )
        if cache_hit:
            return response

        response, self.proxy_mo = self.get_resources(
            'Proxy', 
            'config.openshift.io/v1', 
            self.proxy_mo,
            name=name
        )

        return response
