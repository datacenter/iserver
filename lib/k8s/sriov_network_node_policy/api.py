import time
import traceback


class K8sSriovNetworkNodePolicyApi():
    def __init__(self):
        self.sriov_network_node_policy_mo = None

    def get_sriov_network_node_policy_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_network_node_policy_mo is not None:
                return self.sriov_network_node_policy_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='sriovnetwork.openshift.io/v1',
                kind='SriovNetworkNodePolicy'
            )
            self.sriov_network_node_policy_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'sriov_network_node_policy',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_sriov_network_node_policy_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'sriov_network_node_policy',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'sriov_network_node_policy',
            self.sriov_network_node_policy_mo
        )

        return self.sriov_network_node_policy_mo

    def create_sriov_network_node_policy(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetworkNodePolicy')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('k8s.create_sriov_network_node_policy', traceback.format_exc())

        self.log.k8s(
            'create',
            'sriov_network',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_sriov_network_node_policy(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetworkNodePolicy')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('k8s.delete_sriov_network_node_policy', traceback.format_exc())

        self.log.k8s(
            'delete',
            'delete_sriov_network_node_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
