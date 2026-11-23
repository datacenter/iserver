class L3OutExternalEpgInfo():
    def __init__(self):
        self.l3out_external_epg = {}

    def init_l3out_external_epg(self):
        self.l3out_external_epg = {}

    def get_l3out_external_epg_subnet_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'aggregate',
            'annotation',
            'dn',
            'ip',
            'name',
            'scope'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_l3out_external_epg_info(self, managed_objects):
        info = []
        for managed_object in managed_objects:
            info.append(
                self.get_l3out_external_epg_subnet_info(
                    managed_object
                )
            )

        return info

    def get_l3out_external_epg(self, tenant_name, l3out_name, epg_name, cache_enabled=True):
        key = '%s.%s.%s' % (tenant_name, l3out_name, epg_name)
        if cache_enabled:
            if key in self.l3out_external_epg:
                return self.l3out_external_epg[key]

        subnets_mo = self.get_l3out_external_epg_mo(
            tenant_name,
            l3out_name,
            epg_name,
            cache_enabled=cache_enabled
        )
        if subnets_mo is None:
            return None

        self.l3out_external_epg[key] = self.get_l3out_external_epg_info(
            subnets_mo
        )

        self.log.apic_mo(
            'l3OutExternalEpg.%s.info' % (key),
            self.l3out_external_epg[key]
        )

        return self.l3out_external_epg[key]

    def is_l3out_external_epg_subnet(self, tenant_name, l3out_name, epg_name, subnet, cache_enabled=True):
        info = self.get_l3out_external_epg(
            tenant_name,
            l3out_name,
            epg_name,
            cache_enabled=cache_enabled
        )
        if info is None:
            return False

        for item in info:
            if item['ip'] == subnet:
                return True

        return False
