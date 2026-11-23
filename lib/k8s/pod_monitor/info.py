from lib import filter_helper


class K8sPodMonitorInfo():
    def __init__(self):
        self.pod_monitor = None

    def get_pod_monitor_info(self, pod_monitor_mo):
        if pod_monitor_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_pod_monitors_info(self, cache_enabled=True):
        if cache_enabled:
            if self.pod_monitor is not None:
                return self.pod_monitor

        managed_objects = self.get_pod_monitor_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.pod_monitor = []
        for managed_object in managed_objects:
            pod_monitor_info = {}
            pod_monitor_info['info'] = self.get_pod_monitor_info(
                managed_object
            )
            pod_monitor_info['mo'] = managed_object
            self.pod_monitor.append(
                pod_monitor_info
            )

        return self.pod_monitor

    def match_pod_monitor(self, pod_monitor_info, pod_monitor_filter):
        if pod_monitor_filter is None or len(pod_monitor_filter) == 0:
            return True

        for ap_rule in pod_monitor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_pod_monitor',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_pod_monitors(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_pod_monitors = self.get_pod_monitors_info(cache_enabled=cache_enabled)
        if all_pod_monitors is None:
            return None

        pod_monitors = []

        for pod_monitor_info in all_pod_monitors:
            if not self.match_pod_monitor(pod_monitor_info['info'], object_filter):
                continue

            if return_mo:
                pod_monitors.append(
                    pod_monitor_info['mo']
                )
                continue

            pod_monitors.append(
                pod_monitor_info['info']
            )

        return pod_monitors
