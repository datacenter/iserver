class PolicyInterfacePortSecurityApi():
    def __init__(self):
        self.policy_interface_port_security_mo = None

    def get_policy_interface_port_security_mo(self):
        if self.policy_interface_port_security_mo is not None:
            return self.policy_interface_port_security_mo

        cache = self.get_object_cache(
            'l2PortSecurityPol'
        )
        if cache is not None:
            self.policy_interface_port_security_mo = cache
            self.log.apic_mo(
                'l2PortSecurityPol',
                self.policy_interface_port_security_mo
            )
            return self.policy_interface_port_security_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'l2PortSecurityPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_port_security_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2PortSecurityPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'l2PortSecurityPol'
            )

            self.policy_interface_port_security_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l2PortSecurityPol',
            self.policy_interface_port_security_mo
        )

        self.set_object_cache(
            'l2PortSecurityPol',
            self.policy_interface_port_security_mo
        )

        return self.policy_interface_port_security_mo
