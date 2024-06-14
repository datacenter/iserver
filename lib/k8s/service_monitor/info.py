from lib import filter_helper


class K8sServiceMonitorInfo():
    def __init__(self):
        self.service_monitor = None

    def get_service_monitor_info(self, service_monitor_mo):
        if service_monitor_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            service_monitor_mo
        )
        info.update(metadata_info)

        return info

    def get_service_monitors_info(self, cache_enabled=True):
        if cache_enabled:
            if self.service_monitor is not None:
                return self.service_monitor

        managed_objects = self.get_service_monitor_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.service_monitor = []
        for managed_object in managed_objects:
            service_monitor_info = {}
            service_monitor_info['info'] = self.get_service_monitor_info(
                managed_object
            )
            service_monitor_info['mo'] = managed_object
            self.service_monitor.append(
                service_monitor_info
            )

        return self.service_monitor

    def match_service_monitor(self, service_monitor_info, service_monitor_filter):
        if service_monitor_filter is None or len(service_monitor_filter) == 0:
            return True

        for ap_rule in service_monitor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_service_monitor',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_service_monitors(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_service_monitors = self.get_service_monitors_info(cache_enabled=cache_enabled)
        if all_service_monitors is None:
            return None

        service_monitors = []

        for service_monitor_info in all_service_monitors:
            if not self.match_service_monitor(service_monitor_info['info'], object_filter):
                continue

            if return_mo:
                service_monitors.append(
                    service_monitor_info['mo']
                )
                continue

            service_monitors.append(
                service_monitor_info['info']
            )

        return service_monitors
