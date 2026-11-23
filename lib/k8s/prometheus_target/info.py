from lib import filter_helper


class K8sPrometheusTargetInfo():
    def __init__(self):
        self.prometheus_target_platform = None
        self.prometheus_target_user = None

    def get_prometheus_target_info(self, managed_object, target_type):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        info['type'] = target_type
        for key in managed_object:
            info[key] = managed_object[key]

        info['sm_namespace'] = None
        info['sm_name'] = None
        if managed_object['scrapePool'].split('/')[0] == 'serviceMonitor':
            info['sm_namespace'] = managed_object['scrapePool'].split('/')[1]
            info['sm_name'] = managed_object['scrapePool'].split('/')[2]

        info['sm_namespace_nameT'] = []
        if info['sm_namespace'] is None:
            info['sm_namespace_nameT'].append(None)
        else:
            info['sm_namespace_nameT'].append(info['sm_namespace'])
            info['sm_namespace_nameT'].append(info['sm_name'])

        info['service_namespace'] = filter_helper.get(managed_object, 'labels:namespace')
        info['service_name'] = filter_helper.get(managed_object, 'labels:service')
        info['service_endpoint'] = filter_helper.get(managed_object, 'labels:endpoint')
        info['pod'] = filter_helper.get(managed_object, 'labels:pod')
        
        info['serviceT'] = []
        if info['service_namespace'] is not None:
            info['serviceT'].append(info['service_namespace'])

        if info['service_name'] is not None:
            info['serviceT'].append(info['service_name'])

        if info['service_endpoint'] is not None:
            info['serviceT'].append('ep:%s' % (info['service_endpoint']))

        if info['pod'] is not None:
            info['serviceT'].append('pod:%s' % (info['pod']))

        if info['health'] == 'up':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['readyTick'] = 'Red'

        info['lastScrapeDurationT'] = '{:.2f}'.format(round(info['lastScrapeDuration'] * 1000, 2))
        info['lastScrapeT'] = '.'.join(info['lastScrape'].split('.')[:-1])
        return info

    def get_prometheus_targets_platform_info(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus_target_platform is not None:
                return self.prometheus_target_platform

        managed_objects = self.get_prometheus_target_platform_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.prometheus_target_platform = []
        for managed_object in managed_objects:
            self.prometheus_target_platform.append(
                self.get_prometheus_target_info(
                    managed_object,
                    'P'
                )
            )

        return self.prometheus_target_platform

    def get_prometheus_targets_user_info(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus_target_user is not None:
                return self.prometheus_target_user

        managed_objects = self.get_prometheus_target_user_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.prometheus_target_user = []
        for managed_object in managed_objects:
            self.prometheus_target_user.append(
                self.get_prometheus_target_info(
                    managed_object,
                    'U'
                )
            )

        return self.prometheus_target_user

    def match_prometheus_target(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')
            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, info['sm_namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (info['sm_namespace'], info['sm_name'])):
                    return False

            if key == 'type':
                key_found = True
                if not filter_helper.match_string(value, info['type']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_prometheus_target_platform',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_prometheus_targets(self, object_filter=None, cache_enabled=True):
        all_prometheus_targets = []
        
        platform = self.get_prometheus_targets_platform_info(cache_enabled=cache_enabled)
        if platform is not None:
            all_prometheus_targets = all_prometheus_targets + platform

        user = self.get_prometheus_targets_user_info(cache_enabled=cache_enabled)
        if user is not None:
            all_prometheus_targets = all_prometheus_targets + user

        prometheus_targets = []

        for prometheus_target in all_prometheus_targets:
            if not self.match_prometheus_target(prometheus_target, object_filter):
                continue

            prometheus_targets.append(
                prometheus_target
            )

        return prometheus_targets
