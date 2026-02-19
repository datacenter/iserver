import time
import traceback


class K8sStorageSystemApi():
    def __init__(self):
        self.storage_system_mo = None

    def get_storage_system_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_system_mo is not None:
                return self.storage_system_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='odf.openshift.io/v1alpha1',
                kind='StorageSystem'
            )
            self.storage_system_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'storage_system',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_storage_system_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'storage_system',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'storage_system',
            self.storage_system_mo
        )

        return self.storage_system_mo

    def delete_storage_system_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='odf.openshift.io/v1alpha1', kind='StorageSystem')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_storage_system', traceback.format_exc())

        self.log.ocp(
            'delete',
            'storage_system',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def set_storage_system_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='odf.openshift.io/v1alpha1', kind='StorageSystem')
            response = obj_list.replace(
                body=body
            )
            self.log.k8s(
                'set',
                'storage_system',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.storage_system', traceback.format_exc())
            self.log.k8s(
                'set',
                'storage_system',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True
