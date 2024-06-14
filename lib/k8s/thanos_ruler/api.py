import time
import traceback


class K8sThanosRulerApi():
    def __init__(self):
        self.thanos_ruler_mo = None

    def get_thanos_ruler_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.thanos_ruler_mo is not None:
                return self.thanos_ruler_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='monitoring.coreos.com/v1',
                kind='ThanosRuler'
            )
            self.thanos_ruler_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'thanos_ruler',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_thanos_ruler_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'thanos_ruler',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'thanos_ruler',
            self.thanos_ruler_mo
        )

        return self.thanos_ruler_mo
