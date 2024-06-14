import time
import traceback


class K8sStatefulSetApi():
    def __init__(self):
        self.stateful_set_mo = None

    def get_stateful_set_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.stateful_set_mo is not None:
                return self.stateful_set_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps/v1',
                kind='StatefulSet'
            )
            self.stateful_set_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'stateful_set',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_stateful_set_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'stateful_set',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'stateful_set',
            self.stateful_set_mo
        )

        return self.stateful_set_mo
