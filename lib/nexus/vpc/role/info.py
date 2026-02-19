class VpcRoleInfo():
    def __init__(self):
        self.vpc_role = None

    def get_vpc_role_info(self, vpc_role_mo):
        if vpc_role_mo is None:
            return None


        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in vpc_role_mo:
            info[key] = vpc_role_mo[key]

        return info

    def get_vpc_role(self, cache_enabled=True):
        if not self.is_feature_enabled('vpc'):
            return None

        vpc_role_mo = self.get_vpc_role_mo(cache_enabled=cache_enabled)
        if vpc_role_mo is None:
            self.log.error(
                'get_vpc_role',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_vpc_role_info(vpc_role_mo)
