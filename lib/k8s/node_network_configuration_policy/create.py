from lib import ip_helper


class K8sNodeNetworkConfigurationPolicyCreate():
    def __init__(self):
        pass

    def get_new_nncp_name(self, base_name):
        if not self.is_node_network_configuration_policy(base_name, cache_enabled=False):
            return base_name

        while True:
            policy_name = '%s-%s' % (base_name, ip_helper.get_short_uuid())
            if not self.is_node_network_configuration_policy(policy_name, cache_enabled=False):
                return policy_name

    def create_node_network_configuration_policy(
            self, 
            body,
            confirmation=False, 
            my_output=None, 
            wait=True,
            max_time=0
        ):
        if not self.create_resource(body, object_name='node_network_configuration_policy', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_node_network_configuration_policy(
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        if max_time == 0:
            max_time = 180

        success = self.wait_node_network_configuration_policy(
            body['metadata']['name'],
            match_properties={'status':'Available'},
            break_properties={'status':'Degraded'},
            max_time=max_time,
            my_output=my_output
        )
        if not success:
            return False

        return success
