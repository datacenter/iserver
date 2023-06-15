class PolicyInterfaceCoppProtocolApi():
    def __init__(self):
        self.policy_interface_copp_protocol_mo = None

    def get_policy_interface_copp_protocol_mo(self):
        if self.policy_interface_copp_protocol_mo is not None:
            return self.policy_interface_copp_protocol_mo

        cache = self.get_object_cache(
            'coppProtoClassP'
        )
        if cache is not None:
            self.policy_interface_copp_protocol_mo = cache
            self.log.apic_mo(
                'coppProtoClassP',
                self.policy_interface_copp_protocol_mo
            )
            return self.policy_interface_copp_protocol_mo

        managed_objects = self.get_class(
            'coppProtoClassP'
        )
        if managed_objects is None:
            return None

        self.policy_interface_copp_protocol_mo = []

        for managed_object in managed_objects['imdata']:
            self.policy_interface_copp_protocol_mo.append(
                managed_object['coppProtoClassP']['attributes']
            )

        self.log.apic_mo(
            'coppProtoClassP',
            self.policy_interface_copp_protocol_mo
        )

        self.set_object_cache(
            'coppProtoClassP',
            self.policy_interface_copp_protocol_mo
        )

        return self.policy_interface_copp_protocol_mo
