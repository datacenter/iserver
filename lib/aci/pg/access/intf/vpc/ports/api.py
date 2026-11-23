class PolicyGroupAccessInterfaceVpcPortApi():
    def __init__(self):
        self.policy_group_access_interface_vpc_port_mo = {}

    def get_policy_group_access_interface_vpc_port_mo(self, policy_group_name, node_id):
        key = '%s.%s' % (
            policy_group_name,
            node_id
        )
        if key in self.policy_group_access_interface_vpc_port_mo:
            return self.policy_group_access_interface_vpc_port_mo[key]

        cache = self.get_object_cache(
            'AccBaseGrpToEthIf',
            object_selector=key
        )
        if cache is not None:
            self.policy_group_access_interface_vpc_port_mo[key] = cache
            self.log.apic_mo(
                'AccBaseGrpToEthIf.%s' % (key),
                self.policy_group_access_interface_vpc_port_mo[key]
            )
            return self.policy_group_access_interface_vpc_port_mo[key]

        distinguished_name = 'uni/infra/funcprof/accbundle-%s' % (policy_group_name)
        query = 'rsp-subtree-include=full-deployment&target-node=%s&target-path=AccBaseGrpToEthIf' % (node_id)

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_vpc_port_mo',
                'API failed'
            )
            return None

        self.log.apic_mo(
            'AccBaseGrpToEthIf.mo.%s' % (key),
            managed_objects
        )

        self.policy_group_access_interface_vpc_port_mo[key] = []

        for managed_object in managed_objects['imdata']:
            for child in managed_object['infraAccBndlGrp']['children']:
                if 'pconsNodeDeployCtx' in child:
                    for node_child in child['pconsNodeDeployCtx']['children']:
                        if 'pconsResourceCtx' in node_child:
                            self.policy_group_access_interface_vpc_port_mo[key].append(
                                node_child['pconsResourceCtx']['attributes']
                            )

        self.log.apic_mo(
            'AccBaseGrpToEthIf.%s' % (key),
            self.policy_group_access_interface_vpc_port_mo[key]
        )

        self.set_object_cache(
            'AccBaseGrpToEthIf',
            self.policy_group_access_interface_vpc_port_mo[key],
            object_selector=key
        )

        return self.policy_group_access_interface_vpc_port_mo[key]
