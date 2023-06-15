class PolicyInterfaceTransceiverApi():
    def __init__(self):
        self.policy_interface_transceiver_mo = None

    def get_policy_interface_transceiver_mo(self):
        if self.policy_interface_transceiver_mo is not None:
            return self.policy_interface_transceiver_mo

        cache = self.get_object_cache(
            'xcvrOpticsIfPol'
        )
        if cache is not None:
            self.policy_interface_transceiver_mo = cache
            self.log.apic_mo(
                'xcvrOpticsIfPol',
                self.policy_interface_transceiver_mo
            )
            return self.policy_interface_transceiver_mo

        managed_objects = self.get_class(
            'xcvrOpticsIfPol',
            node_class=True
        )
        if managed_objects is None:
            return None

        self.policy_interface_transceiver_mo = []

        for managed_object in managed_objects['imdata']:
            if 'xcvrZRIfPol' in managed_object:
                attributes = managed_object['xcvrZRIfPol']['attributes']
                attributes['type'] = 'xcvrZRIfPol'
                self.policy_interface_transceiver_mo.append(
                    attributes
                )

            if 'xcvrZRPIfPol' in managed_object:
                attributes = managed_object['xcvrZRPIfPol']['attributes']
                attributes['type'] = 'xcvrZRPIfPol'
                self.policy_interface_transceiver_mo.append(
                    attributes
                )

            self.policy_interface_transceiver_mo.append(
                attributes
            )

        self.log.apic_mo(
            'xcvrOpticsIfPol',
            self.policy_interface_transceiver_mo
        )

        self.set_object_cache(
            'xcvrOpticsIfPol',
            self.policy_interface_transceiver_mo
        )

        return self.policy_interface_transceiver_mo
