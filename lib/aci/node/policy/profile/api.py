class NodeInterfacePolicyProfileApi():
    def __init__(self):
        self.node_interface_policy_profile_mo = {}

    def get_node_interface_policy_profile_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.node_interface_policy_profile_mo:
            return self.node_interface_policy_profile_mo[key]

        cache = self.get_object_cache(
            'infraRsInterfacePolProfile',
            object_selector=key
        )
        if cache is not None:
            self.node_interface_policy_profile_mo[key] = cache
            self.log.apic_mo(
                'infraRsInterfacePolProfile.%s' % (key),
                self.node_interface_policy_profile_mo[key]
            )
            return self.node_interface_policy_profile_mo[key]

        # https://<apic>/api/node/mo/uni/infra/nodecfgcont/node-205.json?query-target=subtree&target-subtree-class=infraRsInterfacePolProfile,infraRsFexGrp&_dc=1684139156603
        distinguished_name = 'uni/infra/nodecfgcont/node-%s' % (
            node_id
        )
        query = 'query-target=subtree&target-subtree-class=infraRsInterfacePolProfile'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_node_interface_policy_profile_mo',
                'API failed'
            )
            return None

        self.node_interface_policy_profile_mo[key] = []

        for managed_object in managed_objects['imdata']:
            if 'infraRsInterfacePolProfile' in managed_object:
                self.node_interface_policy_profile_mo[key].append(
                    managed_object['infraRsInterfacePolProfile']['attributes']
                )

        self.log.apic_mo(
            'infraRsInterfacePolProfile.%s' % (key),
            self.node_interface_policy_profile_mo[key]
        )

        self.set_object_cache(
            'infraRsInterfacePolProfile',
            self.node_interface_policy_profile_mo[key],
            object_selector=key
        )

        return self.node_interface_policy_profile_mo[key]
