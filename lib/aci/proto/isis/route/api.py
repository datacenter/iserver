class ProtocolIsisRouteApi():
    def __init__(self):
        self.isis_domain_routes_mo = {}

    def get_protocol_isis_domain_routes_mo(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_routes_mo:
            return self.isis_domain_routes_mo[key]

        cache = self.get_object_cache(
            'isisRoute',
            object_selector=key
        )
        if cache is not None:
            self.isis_domain_routes_mo[key] = cache
            self.log.apic_mo(
                'isisRoute.%s' % (key),
                self.isis_domain_routes_mo[key]
            )
            return self.isis_domain_routes_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/isis/inst-%s/dom-%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        query = 'query-target=subtree&target-subtree-class=isisRoute&target-subtree-class=isisRsNhAtt'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_isis_domain_routes_mo',
                'API failed'
            )
            return None

        self.isis_domain_routes_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'isisRoute' in managed_object:
                attributes = managed_object['isisRoute']['attributes']
                attributes['isisNexthop'] = []
                self.isis_domain_routes_mo[key].append(
                    attributes
                )

        for managed_object in managed_objects['imdata']:
            if 'isisRsNhAtt' in managed_object:
                attributes = managed_object['isisRsNhAtt']['attributes']
                for route in self.isis_domain_routes_mo[key]:
                    pfx = route['dn'].split('rt-[')[1].split(']')[0]
                    if route['pfx'] == pfx:
                        if attributes['tDn'] not in route['isisNexthop']:
                            route['isisNexthop'].append(
                                attributes['tDn']
                            )

        self.log.apic_mo(
            'isisRoute.%s' % (key),
            self.isis_domain_routes_mo[key]
        )

        self.set_object_cache(
            'isisRoute',
            self.isis_domain_routes_mo[key],
            object_selector=key
        )

        return self.isis_domain_routes_mo[key]
