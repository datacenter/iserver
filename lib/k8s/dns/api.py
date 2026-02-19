import time
import traceback


class K8sDnsApi():
    def __init__(self):
        self.dns_mo = None

    def get_dns_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.dns_mo is not None:
                return self.dns_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='config.openshift.io/v1',
                kind='DNS'
            )
            self.dns_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'dns',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_dns_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'dns',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'dns',
            self.dns_mo
        )

        return self.dns_mo
