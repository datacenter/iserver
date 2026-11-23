class PolicyGroupAccessInterfaceBreakoutApi():
    def __init__(self):
        self.policy_group_access_interface_breakout_mo = None

    def get_policy_group_access_interface_breakout_mo(self):
        if self.policy_group_access_interface_breakout_mo is not None:
            return self.policy_group_access_interface_breakout_mo

        # url: https://<apic>/api/node/class/infraBrkoutPortGrp.json

        cache = self.get_object_cache(
            'infraBrkoutPortGrp'
        )
        if cache is not None:
            self.policy_group_access_interface_breakout_mo = cache
            self.log.apic_mo(
                'infraBrkoutPortGrp',
                self.policy_group_access_interface_breakout_mo
            )
            return self.policy_group_access_interface_breakout_mo

        managed_objects = self.get_class(
            'infraBrkoutPortGrp',
            node_class=True
        )
        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_breakout_mo',
                'API failed'
            )
            return None

        self.policy_group_access_interface_breakout_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraBrkoutPortGrp']['attributes']
            self.policy_group_access_interface_breakout_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraBrkoutPortGrp',
            self.policy_group_access_interface_breakout_mo
        )

        self.set_object_cache(
            'infraBrkoutPortGrp',
            self.policy_group_access_interface_breakout_mo
        )

        return self.policy_group_access_interface_port_mo
