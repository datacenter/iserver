import time
import traceback


class K8sEventApi():
    def __init__(self):
        self.event_mo = None

    def get_event_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.event_mo is not None:
                return self.event_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_event_for_all_namespaces
        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_event_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'event',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_events.get_events', traceback.format_exc())
            self.log.k8s(
                'get',
                'event',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.event_mo = []
        for item in response.items:
            event_mo = self.convert_object(item.to_dict())
            self.event_mo.append(
                event_mo
            )

        self.log.k8s_mo(
            'event',
            self.event_mo
        )

        return self.event_mo
