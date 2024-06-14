import time
import traceback


class K8sKubevirtApi():
    def __init__(self):
        self.kubevirt_mo = None

    def get_kubevirt_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.kubevirt_mo is not None:
                return self.kubevirt_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='kubevirt.io/v1',
                kind='KubeVirt'
            )
            self.kubevirt_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'kubevirt',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_kubevirt_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'kubevirt',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'kubevirt',
            self.kubevirt_mo
        )

        return self.kubevirt_mo
