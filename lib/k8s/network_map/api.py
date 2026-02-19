import time
import traceback


class K8sNetworkMapApi():
    def __init__(self):
        self.network_map_mo = None

    def get_network_map_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.network_map_mo is not None:
                return self.network_map_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.konveyor.io/v1beta1',
                kind='NetworkMap'
            )
            self.network_map_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'network_map',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_network_map_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'network_map',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'network_map',
            self.network_map_mo
        )

        return self.network_map_mo

    def create_network_map_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='NetworkMap')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_network_map', traceback.format_exc())

        self.log.ocp(
            'create',
            'network_map',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_network_map_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='NetworkMap')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_network_map_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'network_map',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_network_map_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='NetworkMap')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_network_map_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'network_map',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    