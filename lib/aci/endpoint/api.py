class EndpointApi():
    def __init__(self):
        self.endpoints_mo = None

    def get_endpoints_mo(self):
        if self.endpoints_mo is not None:
            return self.endpoints_mo

        cache = self.get_object_cache(
            'fvCEp'
        )
        if cache is not None:
            self.endpoints_mo = cache
            self.log.apic_mo(
                'fvCEp',
                self.endpoints_mo
            )
            return self.endpoints_mo

        query = 'rsp-subtree-include=health,fault-count&rsp-subtree=children'
        children = [
            'fvIp',
            'fvRsCEpToPathEp',
            'fvRsToVm',
            'fvRsHyper',
            'fvRsToNic'
        ]
        for child in children:
            query = '%s&rsp-subtree-class=%s' % (query, child)

        managed_objects = self.get_class(
            'fvCEp',
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_endpoint_mo',
                'API failed'
            )
            return None

        self.endpoints_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvCEp']['attributes']

            attributes['fvIp'] = self.get_mo_children_attributes(
                'fvCEp',
                managed_object,
                'fvIp'
            )

            attributes['fvRsCEpToPathEp'] = self.get_mo_child_attributes(
                'fvCEp',
                managed_object,
                'fvRsCEpToPathEp'
            )

            attributes['fvRsToVm'] = self.get_mo_child_attributes(
                'fvCEp',
                managed_object,
                'fvRsToVm'
            )

            attributes['fvRsHyper'] = self.get_mo_child_attributes(
                'fvCEp',
                managed_object,
                'fvRsHyper'
            )

            attributes['fvRsToNic'] = self.get_mo_child_attributes(
                'fvCEp',
                managed_object,
                'fvRsToNic'
            )

            self.endpoints_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvCEp',
            self.endpoints_mo
        )

        self.set_object_cache(
            'fvCEp',
            self.endpoints_mo
        )

        return self.endpoints_mo
