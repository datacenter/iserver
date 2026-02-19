import time
import traceback


class K8sAaqApi():
    def __init__(self):
        self.aaq_mo = None

    def get_aaq_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.aaq_mo is not None:
                return self.aaq_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='aaq.kubevirt.io/v1alpha1',
                kind='AAQ'
            )
            self.aaq_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'aaq',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_aaq_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'aaq',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'aaq',
            self.aaq_mo
        )

        return self.aaq_mo
