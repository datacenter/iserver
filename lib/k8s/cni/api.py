import time
import traceback


class K8sCniApi():
    def __init__(self):
        self.cni_mo = None

    def get_cni_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cni_mo is not None:
                return self.cni_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='config.openshift.io/v1',
                kind='Network'
            )
            self.cni_mo = response.get().to_dict()['items']

            self.log.k8s(
                'get',
                'cni',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_cni_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'cni',
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        self.log.k8s_mo(
            'cni',
            self.cni_mo
        )

        return self.cni_mo
