class K8sNodeNetworkConfigurationPolicyLldp():
    def __init__(self):
        pass

    def get_nncp_interface_lldp_enable_body(
            self, 
            interface_name, 
            policy_name=None, 
            node_name=None,            
        ):
        body = {}
        body['apiVersion'] = 'nmstate.io/v1'
        body['kind'] = 'NodeNetworkConfigurationPolicy'
        body['metadata'] = {}

        if policy_name is None:
            if node_name is not None:
                policy_name = 'enable-lldp-%s-%s' % (node_name, interface_name)
            else:
                policy_name = 'enable-lldp-%s' % (interface_name)

        body['metadata']['name'] = self.get_new_nncp_name(policy_name)

        body['spec'] = {}
        body['spec']['nodeSelector'] = {}

        if node_name is not None:
            body['spec']['nodeSelector']['kubernetes.io/hostname'] = node_name
        else:
            body['spec']['nodeSelector']['node-role.kubernetes.io/worker'] = '""'

        body['spec']['desiredState'] = {}
        body['spec']['desiredState']['interfaces'] = []

        interface_mo = {}
        interface_mo['name'] = interface_name
        interface_mo['type'] = 'ethernet'
        interface_mo['lldp'] = {}
        interface_mo['lldp']['enabled'] = True
        body['spec']['desiredState']['interfaces'].append(
            interface_mo
        )

        return body
    
    def set_nncp_interface_lldp_enabled(
            self, 
            interface_name, 
            policy_name=None, 
            node_name=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):

        body = self.get_nncp_interface_lldp_enable_body(
            interface_name, 
            policy_name=policy_name, 
            node_name=node_name
        )
        success = self.create_node_network_configuration_policy(
            body,
            confirmation=confirmation,
            my_output=my_output,
            wait=wait
        )
        return success, body['metadata']['name']