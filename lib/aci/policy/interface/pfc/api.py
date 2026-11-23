class PolicyInterfacePfcApi():
    def __init__(self):
        self.policy_interface_pfc_mo = None

    def get_policy_interface_pfc_mo(self):
        if self.policy_interface_pfc_mo is not None:
            return self.policy_interface_pfc_mo

        cache = self.get_object_cache(
            'qosPfcIfPol'
        )
        if cache is not None:
            self.policy_interface_pfc_mo = cache
            self.log.apic_mo(
                'qosPfcIfPol',
                self.policy_interface_pfc_mo
            )
            return self.policy_interface_pfc_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'qosPfcIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_pfc_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['qosPfcIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'qosPfcIfPol'
            )

            self.policy_interface_pfc_mo.append(
                attributes
            )

        self.log.apic_mo(
            'qosPfcIfPol',
            self.policy_interface_pfc_mo
        )

        self.set_object_cache(
            'qosPfcIfPol',
            self.policy_interface_pfc_mo
        )

        return self.policy_interface_pfc_mo
