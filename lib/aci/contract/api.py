class ContractApi():
    def __init__(self):
        self.contracts_mo = None

    def get_contracts_mo(self):
        if self.contracts_mo is not None:
            return self.contracts_mo

        cache = self.get_object_cache(
            'vzBrCP'
        )
        if cache is not None:
            self.contracts_mo = cache
            self.log.apic_mo(
                'vzBrCP',
                self.contracts_mo
            )
            return self.contracts_mo

        query = 'rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv'
        managed_objects = self.get_class(
            'vzBrCP',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_contracts_mo',
                'API failed'
            )
            return None

        self.contracts_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzBrCP']['attributes']
            attributes['vzSubj'] = self.get_mo_children_attributes(
                'vzBrCP',
                managed_object,
                'vzSubj'
            )
            attributes['vzRtCons'] = self.get_mo_children_attributes(
                'vzBrCP',
                managed_object,
                'vzRtCons'
            )
            attributes['vzRtProv'] = self.get_mo_children_attributes(
                'vzBrCP',
                managed_object,
                'vzRtProv'
            )
            self.contracts_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzBrCP',
            self.contracts_mo
        )

        self.set_object_cache(
            'vzBrCP',
            self.contracts_mo
        )

        return self.contracts_mo
