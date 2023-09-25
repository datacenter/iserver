import time
import traceback


class K8sPodMonitorApi():
    def __init__(self):
        self.pod_monitor_mo = None

    def get_pod_monitor_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pod_monitor_mo is not None:
                return self.pod_monitor_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='monitoring.coreos.com/v1',
                kind='PodMonitor'
            )
            self.pod_monitor_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'pod_monitor',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pod_monitor_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'pod_monitor',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'pod_monitor',
            self.pod_monitor_mo
        )

        return self.pod_monitor_mo
