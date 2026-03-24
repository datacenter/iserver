class K8sNodeNetworkConfigurationPolicyDelete():
    def __init__(self):
        pass

    def delete_node_network_configuration_policy(self, name, my_output=None, wait=True):
        info = self.get_node_network_configuration_policy(
            name,
            cache_enabled=False
        )

        success = self.delete_resource(
            'NodeNetworkConfigurationPolicy', 
            'nmstate.io/v1',
            name, 
            object_name='node_network_configuration_policy',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_node_network_configuration_policy(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True

    def delete_node_network_configuration_policies(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Node Network Configuration Policies', before_newline=True, underline=True)

        items = self.get_node_network_configuration_policies(cache_enabled=False)
        if items is None:
            if my_output is not None:
                my_output.error('Failed to get nncp information')
            return False
        
        if len(items) == 0:
            if my_output is not None:
                my_output.default('- no nncp found')
            return True
        
        for item in items:
            if my_output is not None:
                my_output.default('- %s' % (item['name']))

            success = self.delete_node_network_configuration_policy_mo(item['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
            
            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nncp...')
                
                success = self.wait_no_node_network_configuration_policy(item['name'])
                if not success:
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False
                
        return True
