from lib import filter_helper


class K8sServiceMonitorInfo():
    def __init__(self):
        self.service_monitor = None

    def get_service_monitor_info(self, service_monitor_mo):
        if service_monitor_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['spec'] = filter_helper.get(service_monitor_mo, 'spec')

        metadata_info = self.get_metadata_info(
            service_monitor_mo
        )
        info.update(metadata_info)

        info['any_namespace'] = filter_helper.get(service_monitor_mo, 'spec:namespaceSelector:any', on_error=False, on_none=False)
        info['endpoint_namespace'] = filter_helper.get(service_monitor_mo, 'spec:namespaceSelector:matchNames', on_error=[], on_none=[])
        if len(info['endpoint_namespace']) == 0:
            info['endpoint_namespace'].append(
                info['namespace']
            )

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

    def add_service_monitors_info(self, service_monitors, endpoint_info=False, target_info=False, cache_enabled=True):
        if endpoint_info:
            endpoints = self.get_endpoints(cache_enabled=cache_enabled)
            for service_monitor in service_monitors:
                service_monitor['info']['endpoint'] = []
                service_monitor['info']['endpointT'] = []
                service_monitor['info']['podT'] = []
                if endpoints is None:
                    continue

                endpoint_labels = filter_helper.get(service_monitor['info'], 'spec:selector:matchLabels')
                if endpoint_labels is None:
                    continue

                for endpoint in endpoints:
                    if service_monitor['info']['any_namespace'] or endpoint['namespace'] in service_monitor['info']['endpoint_namespace']:
                        if self.check_endpoint_with_label(endpoint, endpoint_labels):
                            service_monitor['info']['endpoint'].append(
                                endpoint
                            )
                            service_monitor['info']['endpointT'].append(
                                endpoint['namespace']
                            )
                            service_monitor['info']['endpointT'].append(
                                endpoint['name']
                            )
                            service_monitor['info']['podT'] = service_monitor['info']['podT'] + endpoint['podT']

        if target_info:
            targets = self.get_prometheus_targets(cache_enabled=cache_enabled)
            for service_monitor in service_monitors:
                service_monitor['info']['target'] = None
                service_monitor['info']['targetTick'] = None
                if targets is None:
                    continue

                for target in targets:
                    if target['sm_namespace'] != service_monitor['info']['namespace']:
                        continue

                    if target['sm_name'] != service_monitor['info']['name']:
                        continue

                    service_monitor['info']['target'] = target
                    service_monitor['info']['targetTick'] = target['readyTick']
                    service_monitor['info']['__Output']['targetTick'] = target['__Output']['readyTick']

        return service_monitors

    def match_service_monitor(self, service_monitor_info, service_monitor_filter):
        if service_monitor_filter is None or len(service_monitor_filter) == 0:
            return True

        for ap_rule in service_monitor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, service_monitor_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (service_monitor_info['namespace'], service_monitor_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_service_monitor',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_service_monitors(self, object_filter=None, endpoint_info=False, target_info=False, return_mo=False, cache_enabled=True):
        all_service_monitors = self.get_service_monitors_info(cache_enabled=cache_enabled)
        if all_service_monitors is None:
            return None

        all_service_monitors = self.add_service_monitors_info(
            all_service_monitors,
            endpoint_info=endpoint_info,
            target_info=target_info,
            cache_enabled=cache_enabled
        )

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

    def get_service_monitor(self, namespace, name, endpoint_info=False, target_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        service_monitors = self.get_service_monitors(
            object_filter=object_filter,
            endpoint_info=endpoint_info, 
            target_info=target_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if service_monitors is None:
            return None

        if len(service_monitors) == 1:
            return service_monitors[0]

        return None

    def is_service_monitor(self, namespace, name, cache_enabled=True):
        if self.get_service_monitor(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
