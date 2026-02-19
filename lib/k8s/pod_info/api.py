import time
import traceback


class K8sPodInfoApi():
    def __init__(self):
        self.pod_info_mo = None

    def get_pod_info_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pod_info_mo is not None:
                return self.pod_info_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cilium.io/v1alpha1',
                kind='PodInfo'
            )
            self.pod_info_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'pod_info',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pod_info_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'pod_info',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'pod_info',
            self.pod_info_mo
        )

        return self.pod_info_mo

    def create_pod_info_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='PodInfo')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_pod_info', traceback.format_exc())

        self.log.ocp(
            'create',
            'pod_info',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_pod_info_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='PodInfo')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_pod_info', traceback.format_exc())

        self.log.ocp(
            'replace',
            'pod_info',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_pod_info(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='PodInfo')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_pod_info', traceback.format_exc())

        self.log.ocp(
            'create',
            'pod_info',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
