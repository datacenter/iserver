class K8sDnsInfo():
    def __init__(self):
        self.dns = None

    def get_dns_info(self, dns_mo):
        if dns_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            dns_mo
        )
        info.update(metadata_info)

        info['domain'] = self.get(dns_mo, 'spec:baseDomain')
        return info

    def get_dns(self, return_mo=False, cache_enabled=True):
        dns_mo = self.get_dns_mo(cache_enabled=cache_enabled)
        if dns_mo is None or len(dns_mo) != 1:
            return None
        
        if return_mo:
            return dns_mo[0]
        
        return self.get_dns_info(dns_mo[0])
