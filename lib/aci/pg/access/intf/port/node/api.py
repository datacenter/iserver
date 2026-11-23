class PolicyGroupAccessInterfacePortNodeApi():
    def __init__(self):
        self.policy_group_access_interface_port_node_mo = {}

    def get_policy_group_access_interface_port_node_mo(self, policy_name):
        if policy_name in self.policy_group_access_interface_port_node_mo:
            return self.policy_group_access_interface_port_node_mo[policy_name]

        key = policy_name
        cache = self.get_object_cache(
            'infraAccPortGrp.%s' % (key)
        )
        if cache is not None:
            self.policy_group_access_interface_port_node_mo[key] = cache
            self.log.apic_mo(
                'infraAccPortGrp.%s' % (key),
                self.policy_group_access_interface_port_node_mo[key]
            )
            return self.policy_group_access_interface_port_node_mo[key]

        distinguished_name = 'uni/infra/funcprof/accportgrp-%s' % (policy_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_port_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_policy_group_access_interface_port_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAccPortGrp']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'infraAccPortGrp',
                managed_object
            )
            self.policy_group_access_interface_port_node_mo[key] = attributes

        self.log.apic_mo(
            'infraAccPortGrp.%s' % (key),
            self.policy_group_access_interface_port_node_mo[key]
        )

        self.set_object_cache(
            'infraAccPortGrp.%s' % (key),
            self.policy_group_access_interface_port_node_mo[key]
        )

        return self.policy_group_access_interface_port_node_mo[key]
