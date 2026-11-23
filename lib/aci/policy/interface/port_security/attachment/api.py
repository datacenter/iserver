class PolicyInterfacePortSecurityAttachmentApi():
    def __init__(self):
        self.policy_interface_port_security_attachment_mo = None

    def get_policy_interface_port_security_attachment_mo(self):
        if self.policy_interface_port_security_attachment_mo is not None:
            return self.policy_interface_port_security_attachment_mo

        cache = self.get_object_cache(
            'l1RsL2PortSecurityCons'
        )
        if cache is not None:
            self.policy_interface_port_security_attachment_mo = cache
            self.log.apic_mo(
                'l1RsL2PortSecurityCons',
                self.policy_interface_port_security_attachment_mo
            )
            return self.policy_interface_port_security_attachment_mo

        managed_objects = self.get_class(
            'l1RsL2PortSecurityCons'
        )
        if managed_objects is None:
            return None

        self.policy_interface_port_security_attachment_mo = []

        for managed_object in managed_objects['imdata']:
            self.policy_interface_port_security_attachment_mo.append(
                managed_object['l1RsL2PortSecurityCons']['attributes']
            )

        self.log.apic_mo(
            'l1RsL2PortSecurityCons',
            self.policy_interface_port_security_attachment_mo
        )

        self.set_object_cache(
            'l1RsL2PortSecurityCons',
            self.policy_interface_port_security_attachment_mo
        )

        return self.policy_interface_port_security_attachment_mo
