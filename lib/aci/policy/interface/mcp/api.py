class PolicyInterfaceMcpApi():
    def __init__(self):
        self.policy_interface_mcp_mo = None

    def get_policy_interface_mcp_mo(self):
        if self.policy_interface_mcp_mo is not None:
            return self.policy_interface_mcp_mo

        cache = self.get_object_cache(
            'mcpIfPol'
        )
        if cache is not None:
            self.policy_interface_mcp_mo = cache
            self.log.apic_mo(
                'mcpIfPol',
                self.policy_interface_mcp_mo
            )
            return self.policy_interface_mcp_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'mcpIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_mcp_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['mcpIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'mcpIfPol'
            )

            self.policy_interface_mcp_mo.append(
                attributes
            )

        self.log.apic_mo(
            'mcpIfPol',
            self.policy_interface_mcp_mo
        )

        self.set_object_cache(
            'mcpIfPol',
            self.policy_interface_mcp_mo
        )

        return self.policy_interface_mcp_mo
