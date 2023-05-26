class PolicyGroupAccessInterfaceVpcNodeApi():
    def __init__(self):
        self.policy_group_access_interface_vpc_node_mo = None

    def get_policy_group_access_interface_vpc_node_mo(self):
        if self.policy_group_access_interface_vpc_node_mo is not None:
            return self.policy_group_access_interface_vpc_node_mo

        distinguished_name = 'uni/infra/funcprof'
        query = 'query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_vpc_node_mo',
                'API failed'
            )
            return None

        self.policy_group_access_interface_vpc_node_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAccBndlGrp']['attributes']

            attributes['pconsNodeDeployCtx'] = []
            if 'children' in managed_object['infraAccBndlGrp']:
                for child in managed_object['infraAccBndlGrp']['children']:
                    if 'pconsNodeDeployCtx' in child:
                        node_attributes = child['pconsNodeDeployCtx']['attributes']
                        attributes['pconsNodeDeployCtx'].append(
                            node_attributes
                        )

            self.policy_group_access_interface_vpc_node_mo.append(
                attributes
            )

        self.log.apic_mo(
            'AccBaseGrpToEthIf',
            self.policy_group_access_interface_vpc_node_mo
        )

        return self.policy_group_access_interface_vpc_node_mo
