class K8sNodeNetworkConfigurationPolicyLldp():
    def __init__(self):
        pass

    def set_nncp_interface_lldp_enabled(self, interface_name, policy_name=None, node_name=None):
        policy = {}
        policy['apiVersion'] = 'nmstate.io/v1'
        policy['kind'] = 'NodeNetworkConfigurationPolicy'
        policy['metadata'] = {}

        if policy_name is None:
            if node_name is not None:
                policy_name = 'enable-lldp-%s-%s' % (node_name, interface_name)
            else:
                policy_name = 'enable-lldp-%s' % (interface_name)

        policy['metadata']['name'] = self.get_new_nncp_name(policy_name)

        policy['spec'] = {}
        policy['spec']['nodeSelector'] = {}

        if node_name is not None:
            policy['spec']['nodeSelector']['kubernetes.io/hostname'] = node_name
        else:
            policy['spec']['nodeSelector']['node-role.kubernetes.io/worker'] = '""'

        policy['spec']['desiredState'] = {}
        policy['spec']['desiredState']['interfaces'] = []

        interface_mo = {}
        interface_mo['name'] = interface_name
        interface_mo['type'] = 'ethernet'
        interface_mo['lldp'] = {}
        interface_mo['lldp']['enabled'] = True
        policy['spec']['desiredState']['interfaces'].append(
            interface_mo
        )

        return self.create_node_network_configuration_policy(policy), policy['metadata']['name']
