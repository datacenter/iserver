import time
import traceback


class K8sPriorityClassApi():
    def __init__(self):
        self.priority_class_mo = None

    def get_priority_class_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.priority_class_mo is not None:
                return self.priority_class_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='scheduling.k8s.io/v1',
                kind='PriorityClass'
            )
            self.priority_class_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'priority_class',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_priority_class_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'priority_class',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'priority_class',
            self.priority_class_mo
        )

        return self.priority_class_mo
