import time
import traceback


class K8sSecretApi():
    def __init__(self):
        self.secret_mo = None

    def get_secret_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.secret_mo is not None:
                return self.secret_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='v1',
                kind='Secret'
            )
            self.secret_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'secret',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_secret_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'secret',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'secret',
            self.secret_mo
        )

        return self.secret_mo
