import time
import traceback


class K8sNodeNetworkConfigurationPolicyApi():
    def __init__(self):
        self.node_network_configuration_policy_mo = None

    def set_node_network_configuration_policy_mo(self, managed_objects):
        self.node_network_configuration_policy_mo = managed_objects

    def get_node_network_configuration_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.node_network_configuration_policy_mo
        )
        if cache_hit:
            return response

        response, self.node_network_configuration_policy_mo = self.get_resources(
            'NodeNetworkConfigurationPolicy', 
            'nmstate.io/v1', 
            self.node_network_configuration_policy_mo,
            name=name
        )

        return response  
    
    def create_node_network_configuration_policy(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nmstate.io/v1', kind='NodeNetworkConfigurationPolicy')
            success = True
            response = obj_list.create(
                body=policy
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_node_network_configuration_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'nncp',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_node_network_configuration_policy_mo(self, name):
        return self.delete_resource('NodeNetworkConfigurationPolicy', 'nmstate.io/v1', name)
    