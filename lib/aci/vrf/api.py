class VrfApi():
    def __init__(self):
        self.vrfs_mo = None
        self.vrf_ipv4_mo = {}
        self.vrf_ipv6_mo = {}

    def get_vrf_ipv4_mo(self, tenant, name):
        key = '%s:%s' % (tenant, name)
        if key in self.vrf_ipv4_mo:
            return self.vrf_ipv4_mo[key]

        query = 'query-target-filter=wcard(uribv4Nexthop.dn,"sys/uribv4/dom-%s:%s/db-rt")' % (
            tenant,
            name
        )
        managed_objects = self.get_class(
            'uribv4Nexthop',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_vrf_ipv4_mo',
                'API failed'
            )
            return None

        self.vrf_ipv4_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['uribv4Nexthop']['attributes']
            self.vrf_ipv4_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'uribv4Nexthop.%s.%s' % (tenant, name),
            self.vrf_ipv4_mo[key]
        )

        return self.vrf_ipv4_mo[key]

    def get_vrf_ipv6_mo(self, tenant, name):
        key = '%s:%s' % (tenant, name)
        if key in self.vrf_ipv6_mo:
            return self.vrf_ipv6_mo[key]

        query = 'query-target-filter=wcard(uribv6Nexthop.dn,"sys/uribv6/dom-%s:%s/db-rt")' % (
            tenant,
            name
        )
        managed_objects = self.get_class(
            'uribv6Nexthop',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_vrf_ipv6_mo',
                'API failed'
            )
            return None

        self.vrf_ipv6_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['uribv6Nexthop']['attributes']
            self.vrf_ipv6_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'uribv6Nexthop.%s.%s' % (tenant, name),
            self.vrf_ipv6_mo[key]
        )

        return self.vrf_ipv6_mo[key]

    def get_vrfs_mo(self):
        if self.vrfs_mo is not None:
            return self.vrfs_mo

        managed_objects = self.get_class(
            'fvCtx'
        )

        if managed_objects is None:
            self.log.error(
                'get_vrfs_mo',
                'API failed'
            )
            return None

        self.vrfs_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvCtx']['attributes']
            self.vrfs_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvCtx',
            self.vrfs_mo
        )

        return self.vrfs_mo
