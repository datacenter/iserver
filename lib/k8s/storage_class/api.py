import time
import traceback


class K8sStorageClassApi():
    def __init__(self):
        self.storage_class_mo = None

    def get_storage_class_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_class_mo is not None:
                return self.storage_class_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='storage.k8s.io/v1',
                kind='StorageClass'
            )
            self.storage_class_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'storage_class',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_storage_class_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'storage_class',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'storage_class',
            self.storage_class_mo
        )

        return self.storage_class_mo

    def create_storage_class(self, storage_class):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='storage.k8s.io/v1', kind='StorageClass')
            success = True
            response = obj_list.create(
                body=storage_class
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_storage_class', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_storage_class',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def patch_storage_class_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            obj_list = api_handler.resources.get(api_version='storage.k8s.io/v1', kind='StorageClass')
            obj_list.patch(
                name=body['metadata']['name'],
                body=body,
                content_type='application/merge-patch+json'
            )

        except BaseException:
            self.log.error('k8s.patch_storage_class_mo', traceback.format_exc())
            print(traceback.format_exc())
            return False

        return True
        
    def delete_storage_class_mo(self, storage_class_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='storage.k8s.io/v1', kind='StorageClass')
            success = True
            response = obj_list.delete(
                name=storage_class_name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_storage_class_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'storage_class',
            success,
            int(time.time() * 1000) - start_time
        )

        return success