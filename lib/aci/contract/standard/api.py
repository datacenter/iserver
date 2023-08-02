class ContractStandardApi():
    def __init__(self):
        self.standard_contract_mo = None

    def get_standard_contract_mo(self):
        if self.standard_contract_mo is not None:
            return self.standard_contract_mo

        cache = self.get_object_cache(
            'vzBrCP'
        )
        if cache is not None:
            self.standard_contract_mo = cache
            self.log.apic_mo(
                'vzBrCP',
                self.standard_contract_mo
            )
            return self.standard_contract_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv'
        managed_objects = self.get_class(
            'vzBrCP',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_standard_contract_mo',
                'API failed'
            )
            return None

        self.standard_contract_mo = []
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
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vzBrCP',
                managed_object,
                'faultCounts'
            )
            self.standard_contract_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzBrCP',
            self.standard_contract_mo
        )

        self.set_object_cache(
            'vzBrCP',
            self.standard_contract_mo
        )

        return self.standard_contract_mo
