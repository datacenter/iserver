class ContractFilterFaultApi():
    def __init__(self):
        self.filter_contract_fault_mo = None
        self.filter_contract_fault_record_mo = None

    def get_filter_contract_fault_mo(self):
        cache = self.get_object_cache(
            'vzFilter.fault'
        )
        if cache is not None:
            self.filter_contract_fault_mo = cache
            self.log.apic_mo(
                'vzFilter.fault',
                self.filter_contract_fault_mo
            )
            return self.filter_contract_fault_mo

        query = 'rsp-subtree-include=faults,no-scoped,subtree'
        managed_objects = self.get_class(
            'vzFilter',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_filter_contract_fault_mo',
                'API failed'
            )
            return None

        self.filter_contract_fault_mo = []

        for managed_object in managed_objects['imdata']:
            if 'faultInst' in managed_object:
                attributes = managed_object['faultInst']['attributes']
                attributes['object'] = 'faultInst'
                attributes['delegated'] = False
                self.filter_contract_fault_mo.append(
                    attributes
                )

            if 'faultDelegate' in managed_object:
                attributes = managed_object['faultDelegate']['attributes']
                attributes['object'] = 'faultInst'
                attributes['delegated'] = True
                self.filter_contract_fault_mo.append(
                    attributes
                )

        self.log.apic_mo(
            'vzFilter.fault',
            self.filter_contract_fault_mo
        )

        self.set_object_cache(
            'vzFilter.fault',
            self.filter_contract_fault_mo
        )

        return self.filter_contract_fault_mo

    def get_filter_contract_fault_record_mo(self):
        cache = self.get_object_cache(
            'vzFilter.faultRecord'
        )
        if cache is not None:
            self.filter_contract_fault_record_mo = cache
            self.log.apic_mo(
                'vzFilter.faultRecord',
                self.filter_contract_fault_record_mo
            )
            return self.filter_contract_fault_record_mo

        query = 'rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=%s' % (self.api_fault_limit)
        managed_objects = self.get_class(
            'vzFilter',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_filter_contract_fault_record_mo',
                'API failed'
            )
            return None

        self.filter_contract_fault_record_mo = []

        for managed_object in managed_objects['imdata']:
            if 'faultRecord' in managed_object:
                attributes = managed_object['faultRecord']['attributes']
                attributes['object'] = 'faultRecord'
                attributes['delegated'] = False
                self.filter_contract_fault_record_mo.append(
                    attributes
                )

            if 'faultDelegate' in managed_object:
                attributes = managed_object['faultDelegate']['attributes']
                attributes['object'] = 'faultRecord'
                attributes['delegated'] = True
                self.filter_contract_fault_record_mo.append(
                    attributes
                )

        self.log.apic_mo(
            'vzFilter.faultRecord',
            self.filter_contract_fault_record_mo
        )

        self.set_object_cache(
            'vzFilter.faultRecord',
            self.filter_contract_fault_record_mo
        )

        return self.filter_contract_fault_record_mo
