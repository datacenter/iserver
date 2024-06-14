class ContractFilterApi():
    def __init__(self):
        self.contract_filter_mo = None

    def get_contract_filters_mo(self):
        if self.contract_filter_mo is not None:
            return self.contract_filter_mo

        cache = self.get_object_cache(
            'vzFilter'
        )
        if cache is not None:
            self.contract_filter_mo = cache
            self.log.apic_mo(
                'vzFilter',
                self.contract_filter_mo
            )
            return self.contract_filter_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry'
        managed_objects = self.get_class(
            'vzFilter',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_contract_filters_mo',
                'API failed'
            )
            return None

        self.contract_filter_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzFilter']['attributes']
            attributes['vzEntry'] = self.get_mo_children_attributes(
                'vzFilter',
                managed_object,
                'vzEntry'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vzFilter',
                managed_object,
                'faultCounts'
            )
            self.contract_filter_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzFilter',
            self.contract_filter_mo
        )

        self.set_object_cache(
            'vzFilter',
            self.contract_filter_mo
        )

        return self.contract_filter_mo
