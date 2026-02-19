import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sGrafanaDatasourceInfo():
    def __init__(self):
        self.grafana_datasource = None

    def get_grafana_datasource_info(self, managed_object):
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

        if 'DatasourceSynchronized' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['uid'] = self.get(managed_object, 'status:uid')
        info['ds_type'] = self.get(managed_object, 'spec:datasource:type')
        info['ds_name'] = self.get(managed_object, 'spec:datasource:name')
        return info

    def get_grafana_datasources_info(self, cache_enabled=True):
        if cache_enabled:
            if self.grafana_datasource is not None:
                return self.grafana_datasource

        managed_objects = self.get_grafana_datasource_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.grafana_datasource = []
        for managed_object in managed_objects:
            grafana_info = {}
            grafana_info['info'] = self.get_grafana_datasource_info(
                managed_object
            )
            grafana_info['mo'] = managed_object
            self.grafana_datasource.append(
                grafana_info
            )

        return self.grafana_datasource

    def match_grafana_datasource(self, grafana_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, grafana_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (grafana_info['namespace'], grafana_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_grafana',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_grafana_datasources(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_grafanas = self.get_grafana_datasources_info(cache_enabled=cache_enabled)
        if all_grafanas is None:
            return None

        grafanas = []

        for grafana_info in all_grafanas:
            if not self.match_grafana_datasource(grafana_info['info'], object_filter):
                continue

            if return_mo:
                grafanas.append(
                    grafana_info['mo']
                )
                continue

            grafanas.append(
                grafana_info['info']
            )

        return grafanas

    def is_grafana_datasource(self, namespace, name, cache_enabled=True):
        if self.get_grafana_datasource(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_grafana_datasource(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        grafanas = self.get_grafana_datasources(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if grafanas is None:
            return None

        if len(grafanas) == 1:
            return grafanas[0]

        return None

    def get_instance_datasource(self, instance_name, datasource_type):
        datasources = self.get_grafana_datasources(return_mo=True, cache_enabled=False)
        if datasources is None:
            return None

        for datasource in datasources:
            dashboards = filter_helper.get(datasource, 'spec:instanceSelector:matchLabels:dashboards')
            if dashboards is None:
                continue

            if dashboards != instance_name:
                continue

            spec_datasource_type = filter_helper.get(datasource, 'spec:datasource:type')
            if spec_datasource_type is None:
                continue

            if spec_datasource_type != datasource_type:
                continue

            return filter_helper.get(datasource, 'spec:datasource:name')

        return None
    