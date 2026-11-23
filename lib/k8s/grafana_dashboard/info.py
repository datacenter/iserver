import json
from lib import filter_helper


class K8sGrafanaDashboardInfo():
    def __init__(self):
        self.grafana_dashboard = None

    def get_grafana_dashboard_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        if 'DashboardSynchronized' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['folder'] = self.get(managed_object, 'spec:folder')
        info['uid'] = self.get(managed_object, 'status:uid')
        info['resync'] = self.get(managed_object, 'status:lastResync')
        try:
            info['title'] = json.loads(self.get(managed_object, 'spec:json'))['title']
        except BaseException:
            info['title'] = None

        return info

    def add_grafana_dashboard_info(self, info, instances):
        if instances is not None:
            info['instance'] = []

            dashboard_ref = '%s/%s/%s' % (
                info['namespace'],
                info['name'],
                info['uid']
            )

            for instance in instances:
                if dashboard_ref in instance['dashboard']:
                    info['instance'].append(
                        instance['name']
                    )

        return info
    
    def get_grafana_dashboards_info(self, cache_enabled=True):
        if cache_enabled:
            if self.grafana_dashboard is not None:
                return self.grafana_dashboard

        managed_objects = self.get_grafana_dashboard_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.grafana_dashboard = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = self.get_grafana_dashboard_info(
                managed_object
            )
            info['mo'] = managed_object
            self.grafana_dashboard.append(
                info
            )

        return self.grafana_dashboard

    def match_grafana_dashboard(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (info['namespace'], info['name'])):
                    return False

            if key == 'instance':
                key_found = True
                if 'instance' not in info:
                    return False
                
                match = False
                for item in info['instance']:
                    if filter_helper.match_string(value, item):
                        match = True

                if not match:
                    return False

            if not key_found:
                self.log.error(
                    'match_grafana',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_grafana_dashboards(self, object_filter=None, instance_info=False, return_mo=False, cache_enabled=True):
        all_dashboards = self.get_grafana_dashboards_info(cache_enabled=cache_enabled)
        if all_dashboards is None:
            return None

        dashboards = []

        instances = None
        if instance_info:
            instances = self.get_grafanas(cache_enabled=cache_enabled)

        for dashboard_info in all_dashboards:
            dashboard_info['info'] = self.add_grafana_dashboard_info(dashboard_info['info'], instances)

            if not self.match_grafana_dashboard(dashboard_info['info'], object_filter):
                continue

            if return_mo:
                dashboards.append(
                    dashboard_info['mo']
                )
                continue

            dashboards.append(
                dashboard_info['info']
            )

        return dashboards

    def is_grafana_dashboard(self, namespace, name, cache_enabled=True):
        if self.get_grafana_dashboard(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_grafana_dashboard(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        grafanas = self.get_grafana_dashboards(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if grafanas is None:
            return None

        if len(grafanas) == 1:
            return grafanas[0]

        return None
