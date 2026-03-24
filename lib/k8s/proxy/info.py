class K8sProxyInfo():
    def __init__(self):
        self.proxy = None

    def get_proxy_info(self, proxy_mo):
        if proxy_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            proxy_mo
        )
        info.update(metadata_info)

        info['http_proxy'] = self.get(proxy_mo, 'spec:httpProxy')
        info['https_proxy'] = self.get(proxy_mo, 'spec:httpsProxy')
        info['no_proxy'] = self.get(proxy_mo, 'spec:noProxy')
        return info

    def get_proxy(self, name, return_mo=False, cache_enabled=True):
        proxy_mo = self.get_proxy_mo(cache_enabled=cache_enabled)
        if proxy_mo is None or len(proxy_mo) != 1:
            return None
        
        if proxy_mo[0]['metadata']['name'] != name:
            return None
        
        if return_mo:
            return proxy_mo[0]
        
        return self.get_proxy_info(proxy_mo[0])
    
    def is_proxy(self, name, cache_enabled=True):
        if self.get_proxy(name, cache_enabled=cache_enabled):
            return True
        return False
