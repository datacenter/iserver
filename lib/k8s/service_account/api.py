import time
import traceback


class K8sServiceAccountApi():
    def __init__(self):
        self.service_account_mo = None

    def get_service_account_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.service_account_mo is not None:
                return self.service_account_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='v1',
                kind='ServiceAccount'
            )
            self.service_account_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'service_account',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_service_account_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'service_account',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'service_account',
            self.service_account_mo
        )

        return self.service_account_mo
