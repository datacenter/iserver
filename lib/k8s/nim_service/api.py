import time
import traceback


class K8sNimServiceApi():
    def __init__(self):
        self.nim_service_mo = None

    def get_nim_service_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_service_mo is not None:
                return self.nim_service_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps.nvidia.com/v1alpha1',
                kind='NIMService'
            )
            self.nim_service_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nim_service',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nim_service_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nim_service',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nim_service',
            self.nim_service_mo
        )

        return self.nim_service_mo

    def create_nim_service_mo(self, nim_service):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NIMService')
            success = True
            response = obj_list.create(
                body=nim_service,
                namespace=nim_service['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_nim_service_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'nim_service',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nim_service_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NIMService')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_nim_service_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_nim_service',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
