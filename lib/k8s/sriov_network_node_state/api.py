import time
import traceback


class K8sSriovNetworkNodeStateApi():
    def __init__(self):
        self.sriov_network_node_state_mo = None

    def get_sriov_network_node_state_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_network_node_state_mo is not None:
                return self.sriov_network_node_state_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='sriovnetwork.openshift.io/v1',
                kind='SriovNetworkNodeState'
            )
            self.sriov_network_node_state_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'sriov_network_node_state',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_sriov_network_node_state_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'sriov_network_node_state',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'sriov_network_node_state',
            self.sriov_network_node_state_mo
        )

        return self.sriov_network_node_state_mo
