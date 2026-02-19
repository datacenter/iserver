import time
import traceback


class K8sPrivateNetworkEndpointSliceApi():
    def __init__(self):
        self.private_network_endpoint_slice_mo = None

    def get_private_network_endpoint_slice_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.private_network_endpoint_slice_mo is not None:
                return self.private_network_endpoint_slice_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='isovalent.com/v1alpha1',
                kind='PrivateNetworkEndpointSlice'
            )
            self.private_network_endpoint_slice_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'private_network_endpoint_slice',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_private_network_endpoint_slice_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'private_network_endpoint_slice',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.log.k8s_mo(
            'private_network_endpoint_slice',
            self.private_network_endpoint_slice_mo
        )

        return self.private_network_endpoint_slice_mo

    def create_private_network_endpoint_slice_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='isovalent.com/v1alpha1', kind='PrivateNetworkEndpointSlice')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_private_network_endpoint_slice', traceback.format_exc())

        self.log.ocp(
            'create',
            'private_network_endpoint_slice',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_private_network_endpoint_slice_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='isovalent.com/v1alpha1', kind='PrivateNetworkEndpointSlice')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_private_network_endpoint_slice', traceback.format_exc())

        self.log.ocp(
            'delete',
            'private_network_endpoint_slice',
            success,
            int(time.time() * 1000) - start_time
        )

        return success