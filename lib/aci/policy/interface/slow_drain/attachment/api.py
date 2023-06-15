class PolicyInterfaceSlowDrainAttachmentApi():
    def __init__(self):
        self.policy_interface_slow_drain_attachment_mo = None

    def get_policy_interface_slow_drain_attachment_mo(self):
        if self.policy_interface_slow_drain_attachment_mo is not None:
            return self.policy_interface_slow_drain_attachment_mo

        cache = self.get_object_cache(
            'l1RsQosSdIfPolCons'
        )
        if cache is not None:
            self.policy_interface_slow_drain_attachment_mo = cache
            self.log.apic_mo(
                'l1RsQosSdIfPolCons',
                self.policy_interface_slow_drain_attachment_mo
            )
            return self.policy_interface_slow_drain_attachment_mo

        managed_objects = self.get_class(
            'l1RsQosSdIfPolCons'
        )
        if managed_objects is None:
            return None

        self.policy_interface_slow_drain_attachment_mo = []

        for managed_object in managed_objects['imdata']:
            self.policy_interface_slow_drain_attachment_mo.append(
                managed_object['l1RsQosSdIfPolCons']['attributes']
            )

        self.log.apic_mo(
            'l1RsQosSdIfPolCons',
            self.policy_interface_slow_drain_attachment_mo
        )

        self.set_object_cache(
            'l1RsQosSdIfPolCons',
            self.policy_interface_slow_drain_attachment_mo
        )

        return self.policy_interface_slow_drain_attachment_mo
