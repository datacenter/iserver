class PolicyGroupAccessInterfaceVpcPortInfo():
    def __init__(self):
        self.policy_group_access_interface_vpc_port = {}

    def get_policy_group_access_interface_vpc_port_info(self, managed_object, policy_group_name, node_id):
        port_info = {}
        port_info['dn'] = managed_object['ctxDn']
        port_info['pod_id'] = managed_object['ctxDn'].split('/')[1].split('-')[1]
        port_info['node_id'] = str(node_id)
        port_info['node_name'] = self.get_node_name(
            node_id,
            pod_id=port_info['pod_id']
        )

        if managed_object['ctxClass'] == 'l1PhysIf':
            # topology/pod-1/node-2205/sys/phys-[eth1/11]
            port_info['port_id'] = managed_object['ctxDn'].split('phys-[')[1].rstrip(']')
            port_info['ep'] = 'pod-%s:node-%s:%s (%s)' % (
                port_info['pod_id'],
                port_info['node_id'],
                port_info['port_id'],
                policy_group_name
            )

        if managed_object['ctxClass'] not in ['l1PhysIf']:
            self.log.error(
                'get_policy_group_interface_vpc_info',
                'Unsupported port: %s' % (managed_object)
            )

        return port_info

    def get_policy_group_access_interface_vpc_ports_info(self, policy_group_name, node_id):
        key = '%s.%s' % (
            policy_group_name,
            node_id
        )
        if key in self.policy_group_access_interface_vpc_port:
            return self.policy_group_access_interface_vpc_port[key]

        managed_objects = self.get_policy_group_access_interface_vpc_port_mo(
            policy_group_name,
            node_id
        )
        if managed_objects is None:
            return None

        self.policy_group_access_interface_vpc_port[key] = []
        for managed_object in managed_objects:
            self.policy_group_access_interface_vpc_port[key].append(
                self.get_policy_group_access_interface_vpc_port_info(
                    managed_object,
                    policy_group_name,
                    node_id
                )
            )

        return self.policy_group_access_interface_vpc_port[key]

    def get_policy_group_access_interface_vpc_ports(self, policy_group_name, node_id):
        all_ports = self.get_policy_group_access_interface_vpc_ports_info(
            policy_group_name,
            node_id
        )
        return all_ports
