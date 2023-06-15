class PolicyInterfaceStormControlAttachmentApi():
    def __init__(self):
        self.policy_interface_storm_control_attachment_mo = None

    def get_policy_interface_storm_control_attachment_mo(self):
        if self.policy_interface_storm_control_attachment_mo is not None:
            return self.policy_interface_storm_control_attachment_mo

        cache = self.get_object_cache(
            'l1RsStormctrlIfPolCons'
        )
        if cache is not None:
            self.policy_interface_storm_control_attachment_mo = cache
            self.log.apic_mo(
                'l1RsStormctrlIfPolCons',
                self.policy_interface_storm_control_attachment_mo
            )
            return self.policy_interface_storm_control_attachment_mo

        managed_objects = self.get_class(
            'l1RsStormctrlIfPolCons'
        )
        if managed_objects is None:
            return None

        self.policy_interface_storm_control_attachment_mo = []

        for managed_object in managed_objects['imdata']:
            self.policy_interface_storm_control_attachment_mo.append(
                managed_object['l1RsStormctrlIfPolCons']['attributes']
            )

        self.log.apic_mo(
            'l1RsStormctrlIfPolCons',
            self.policy_interface_storm_control_attachment_mo
        )

        self.set_object_cache(
            'l1RsStormctrlIfPolCons',
            self.policy_interface_storm_control_attachment_mo
        )

        return self.policy_interface_storm_control_attachment_mo
