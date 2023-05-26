import time
import traceback


class OcpApiSriovNetwork():
    def __init__(self):
        self.sriov_networks = None

    def is_ocp_sriov_network(self, sriov_network_namespace, sriov_network_name, cache=True):
        if self.get_ocp_sriov_network(sriov_network_namespace, sriov_network_name, cache=cache) is None:
            return False
        return True

    def get_ocp_sriov_network(self, sriov_network_namespace, sriov_network_name, cache=True):
        if not self.get_ocp_sriov_networks(cache=cache):
            return None

        for sriov_network in self.sriov_networks:
            if sriov_network['metadata']['name'] == sriov_network_name and sriov_network['metadata']['namespace'] == sriov_network_namespace:
                return sriov_network

        return None

    def get_ocp_sriov_networks(self, cache=True):
        if not self.connect():
            return False

        if self.sriov_networks is not None and cache:
            return True

        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetwork')
            self.sriov_networks = obj_list.get().to_dict()['items']

            self.log.ocp(
                'get',
                'get_ocp_sriov_networks',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('ocp.get_ocp_sriov_networks', traceback.format_exc())
            self.log.ocp(
                'get',
                'get_ocp_sriov_networks',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.ocp_mo(
            'get_ocp_sriov_networks',
            self.sriov_networks
        )

        return True

    def create_ocp_sriov_network(self, policy):
        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetwork')
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

    def delete_ocp_sriov_network(self, namespace, name):
        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovNetwork')
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
