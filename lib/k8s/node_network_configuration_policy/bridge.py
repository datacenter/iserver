class K8sNodeNetworkConfigurationPolicyBridge():
    def __init__(self):
        pass

    def delete_bridge_via_node_network_configuration_policy(self, name, node=None, my_output=None, confirmation=False):
        body = {}
        body['apiVersion'] = 'nmstate.io/v1'
        body['kind'] = 'NodeNetworkConfigurationPolicy'
        body['metadata'] = {}
        body['metadata']['name'] = self.get_new_nncp_name('no-bridge')
        body['spec'] = {}
        if node is not None:
            body['spec']['nodeSelector'] = {}
            body['spec']['nodeSelector']['kubernetes.io/hostname'] = node

        body['spec']['desiredState'] = {}
        body['spec']['desiredState']['interfaces'] = []

        interface_mo = {}
        interface_mo['name'] = name
        interface_mo['state'] = 'absent'
        interface_mo['type'] = 'linux-bridge'
        body['spec']['desiredState']['interfaces'].append(interface_mo)

        if not self.create_resource(body, object_name='node_network_configuration_policy', my_output=my_output, confirmation=confirmation):
            return False
        
        success = self.wait_node_network_configuration_policy(body['metadata']['name'], my_output=my_output)
        if not success:
            return False
        
        success = self.wait_node_network_configuration_policy(
            body['metadata']['name'],
            match_properties={'status':'Available'},
            break_properties={'status':'Degraded'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            self.delete_node_network_configuration_policy(
                body['metadata']['name'],
                my_output=my_output
            )
            return False

        success = self.delete_node_network_configuration_policy(
            body['metadata']['name'],
            my_output=my_output
        )
        return success
