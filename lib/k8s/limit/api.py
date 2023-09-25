import time
import traceback


class K8sLimitApi():
    def __init__(self):
        self.limit_mo = None

    def get_limit_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.limit_mo is not None:
                return self.limit_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='v1',
                kind='LimitRange'
            )
            self.limit_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'limit',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_limit_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'limit',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'limit',
            self.limit_mo
        )

        return self.limit_mo
