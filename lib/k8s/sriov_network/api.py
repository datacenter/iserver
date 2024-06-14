import time
import traceback


class K8sSriovNetworkApi():
    def __init__(self):
        self.sriov_network_mo = None

    def get_sriov_network_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_network_mo is not None:
                return self.sriov_network_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='sriovnetwork.openshift.io/v1',
                kind='SriovNetwork'
            )
            self.sriov_network_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'sriov_network',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_sriov_network_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'sriov_network',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'sriov_network',
            self.sriov_network_mo
        )

        return self.sriov_network_mo

    def create_sriov_network(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetwork')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_ocp_sriov_network', traceback.format_exc())

        self.log.ocp(
            'create',
            'sriov_network',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_sriov_network(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetwork')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ocp_sriov_network', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_ocp_sriov_network',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
