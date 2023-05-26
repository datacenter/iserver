import time
import traceback


class OcpApiSriovNetworkNodePolicy():
    def __init__(self):
        self.sriov_network_node_policies = None

    def is_ocp_sriov_network_node_policy(self, sriov_network_node_policy_namespace, sriov_network_node_policy_name, cache=True):
        if self.get_ocp_sriov_network_node_policy(sriov_network_node_policy_namespace, sriov_network_node_policy_name, cache=cache) is None:
            return False
        return True

    def get_ocp_sriov_network_node_policy(self, sriov_network_node_policy_namespace, sriov_network_node_policy_name, cache=True):
        if not self.get_ocp_sriov_network_node_policies(cache=cache):
            return None

        for data_volume in self.sriov_network_node_policies:
            if data_volume['metadata']['name'] == sriov_network_node_policy_name and data_volume['metadata']['namespace'] == sriov_network_node_policy_namespace:
                return data_volume

        return None

    def get_ocp_sriov_network_node_policies(self, cache=True):
        if not self.connect():
            return False

        if self.sriov_network_node_policies is not None and cache:
            return True

        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetworkNodePolicy')
            self.sriov_network_node_policies = obj_list.get().to_dict()['items']

            self.log.ocp(
                'get',
                'get_ocp_sriov_network_node_policies',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('ocp.get_ocp_sriov_network_node_policies', traceback.format_exc())
            self.log.ocp(
                'get',
                'get_ocp_sriov_network_node_policies',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.ocp_mo(
            'get_ocp_sriov_network_node_policies',
            self.sriov_network_node_policies
        )

        return True

    def create_ocp_sriov_network_node_policy(self, policy):
        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetworkNodePolicy')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_ocp_sriov_network_node_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'sriov_network_node_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_ocp_sriov_network_node_policy(self, namespace, name):
        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetworkNodePolicy')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ocp_sriov_network_node_policy', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_ocp_sriov_network_node_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
