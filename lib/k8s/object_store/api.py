import time
import traceback


class K8sObjectStoreApi():
    def __init__(self):
        self.object_store_mo = None

    def get_object_store_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.object_store_mo is not None:
                return self.object_store_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='aistor.min.io/v1',
                kind='ObjectStore'
            )
            self.object_store_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'object_store',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_object_store_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'object_store',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'object_store',
            self.object_store_mo
        )

        return self.object_store_mo

    def create_object_store_mo(self, object_store):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='aistor.min.io/v1', kind='ObjectStore')
            success = True
            response = obj_list.create(
                body=object_store,
                namespace=object_store['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_object_store_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'object_store',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_object_store_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='aistor.min.io/v1', kind='ObjectStore')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_object_store_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_object_store',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
