class VpcKeepaliveInfo():
    def __init__(self):
        self.vpc_keepalive = None

    def get_vpc_keepalive_info(self, vpc_keepalive_mo):
        if vpc_keepalive_mo is None:
            return None


        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name
        for key in vpc_keepalive_mo:
            info[key] = vpc_keepalive_mo[key]

        return info

    def get_vpc_keepalive(self, cache_enabled=True):
        if not self.is_feature_enabled('vpc'):
            return None

        vpc_keepalive_mo = self.get_vpc_keepalive_mo(cache_enabled=cache_enabled)
        if vpc_keepalive_mo is None:
            self.log.error(
                'get_vpc_keepalive',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_vpc_keepalive_info(vpc_keepalive_mo)
