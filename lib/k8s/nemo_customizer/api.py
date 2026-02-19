import time
import traceback


class K8sNemoCustomizerApi():
    def __init__(self):
        self.nemo_customizer_mo = None

    def get_nemo_customizer_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_customizer_mo is not None:
                return self.nemo_customizer_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps.nvidia.com/v1alpha1',
                kind='NemoCustomizer'
            )
            self.nemo_customizer_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nemo_customizer',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nemo_customizer_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nemo_customizer',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nemo_customizer',
            self.nemo_customizer_mo
        )

        return self.nemo_customizer_mo

    def create_nemo_customizer_mo(self, nemo_customizer):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NemoCustomizer')
            success = True
            response = obj_list.create(
                body=nemo_customizer,
                namespace=nemo_customizer['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_nemo_customizer_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'nemo_customizer',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nemo_customizer_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NemoCustomizer')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_nemo_customizer_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_nemo_customizer',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
