class PolicyInterfaceSynceApi():
    def __init__(self):
        self.policy_interface_synce_mo = None

    def get_policy_interface_synce_mo(self):
        if self.policy_interface_synce_mo is not None:
            return self.policy_interface_synce_mo

        cache = self.get_object_cache(
            'synceEthIfPol'
        )
        if cache is not None:
            self.policy_interface_synce_mo = cache
            self.log.apic_mo(
                'synceEthIfPol',
                self.policy_interface_synce_mo
            )
            return self.policy_interface_synce_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'synceEthIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_synce_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['synceEthIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'synceEthIfPol'
            )

            self.policy_interface_synce_mo.append(
                attributes
            )

        self.log.apic_mo(
            'synceEthIfPol',
            self.policy_interface_synce_mo
        )

        self.set_object_cache(
            'synceEthIfPol',
            self.policy_interface_synce_mo
        )

        return self.policy_interface_synce_mo
