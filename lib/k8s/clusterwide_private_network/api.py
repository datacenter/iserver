import time
import traceback


class K8sClusterwidePrivateNetworkApi():
    def __init__(self):
        self.clusterwide_private_network_mo = None

    def get_clusterwide_private_network_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.clusterwide_private_network_mo is not None:
                return self.clusterwide_private_network_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='isovalent.com/v1alpha1',
                kind='ClusterwidePrivateNetwork'
            )
            self.clusterwide_private_network_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'clusterwide_private_network',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_clusterwide_private_network_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'clusterwide_private_network',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.log.k8s_mo(
            'clusterwide_private_network',
            self.clusterwide_private_network_mo
        )

        return self.clusterwide_private_network_mo

    def create_clusterwide_private_network_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='isovalent.com/v1alpha1', kind='ClusterwidePrivateNetwork')
            success = True
            response = obj_list.create(
                body=body
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_clusterwide_private_network', traceback.format_exc())

        self.log.ocp(
            'create',
            'clusterwide_private_network',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_clusterwide_private_network_mo(self, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='isovalent.com/v1alpha1', kind='ClusterwidePrivateNetwork')
            success = True
            response = obj_list.delete(
                name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_clusterwide_private_network', traceback.format_exc())

        self.log.ocp(
            'delete',
            'clusterwide_private_network',
            success,
            int(time.time() * 1000) - start_time
        )

        return success