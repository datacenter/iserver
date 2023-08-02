class ContractTabooApi():
    def __init__(self):
        self.taboo_contract_mo = None

    def get_taboo_contract_mo(self):
        if self.taboo_contract_mo is not None:
            return self.taboo_contract_mo

        cache = self.get_object_cache(
            'vzTaboo'
        )
        if cache is not None:
            self.taboo_contract_mo = cache
            self.log.apic_mo(
                'vzTaboo',
                self.taboo_contract_mo
            )
            return self.taboo_contract_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy'
        managed_objects = self.get_class(
            'vzTaboo',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_taboo_contract_mo',
                'API failed'
            )
            return None

        self.taboo_contract_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzTaboo']['attributes']
            attributes['vzTSubj'] = self.get_mo_children_attributes(
                'vzTaboo',
                managed_object,
                'vzTSubj'
            )
            attributes['vzRtProtBy'] = self.get_mo_children_attributes(
                'vzTaboo',
                managed_object,
                'vzRtProtBy'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vzTaboo',
                managed_object,
                'faultCounts'
            )
            self.taboo_contract_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzTaboo',
            self.taboo_contract_mo
        )

        self.set_object_cache(
            'vzTaboo',
            self.taboo_contract_mo
        )

        return self.taboo_contract_mo
