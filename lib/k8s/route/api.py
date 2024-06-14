import time
import traceback


class K8sRouteApi():
    def __init__(self):
        self.route_mo = None

    def get_route_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.route_mo is not None:
                return self.route_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='route.openshift.io/v1',
                kind='Route'
            )
            self.route_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'route',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_route_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'route',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'route',
            self.route_mo
        )

        return self.route_mo
