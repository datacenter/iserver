import time
import traceback


class K8sStorageMapApi():
    def __init__(self):
        self.storage_map_mo = None

    def get_storage_map_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_map_mo is not None:
                return self.storage_map_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.konveyor.io/v1beta1',
                kind='StorageMap'
            )
            self.storage_map_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'storage_map',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_storage_map_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'storage_map',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'storage_map',
            self.storage_map_mo
        )

        return self.storage_map_mo

    def create_storage_map_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='StorageMap')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_storage_map', traceback.format_exc())

        self.log.ocp(
            'create',
            'storage_map',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_storage_map_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='StorageMap')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_storage_map_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'storage_map',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_storage_map_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='StorageMap')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_storage_map_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'storage_map',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    