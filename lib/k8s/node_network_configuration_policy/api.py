import time
import traceback


class K8sNodeNetworkConfigurationPolicyApi():
    def __init__(self):
        self.node_network_configuration_policy_mo = None

    def set_node_network_configuration_policy_mo(self, managed_objects):
        self.node_network_configuration_policy_mo = managed_objects
        
    def get_node_network_configuration_policy_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_configuration_policy_mo is not None:
                return self.node_network_configuration_policy_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='nmstate.io/v1',
                kind='NodeNetworkConfigurationPolicy'
            )
            self.node_network_configuration_policy_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'node_network_configuration_policy',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_node_network_configuration_policy_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'node_network_configuration_policy',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'node_network_configuration_policy',
            self.node_network_configuration_policy_mo
        )

        return self.node_network_configuration_policy_mo

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
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nmstate.io/v1', kind='NodeNetworkConfigurationPolicy')
            success = True
            response = obj_list.delete(
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_node_network_configuration_policy', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_node_network_configuration_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
