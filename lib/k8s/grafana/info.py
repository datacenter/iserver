import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sGrafanaInfo():
    def __init__(self):
        self.grafana = None

    def get_grafana_info(self, managed_object):
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

        info['url'] = self.get(managed_object, 'status:adminUrl')

        info['authentication'] = False
        disable_login_form = self.get(managed_object, 'spec:config:auth:disable_login_form')
        if disable_login_form is None or disable_login_form == 'false':
            info['authentication'] = True

        info['username'] = self.get(managed_object, 'spec:config:security:admin_user')
        info['password'] = self.get(managed_object, 'spec:config:security:admin_password')

        info['credentials'] = None
        if info['authentication'] and info['username'] is not None and info['password'] is not None:
            info['credentials'] = '%s/%s' % (info['username'], info['password'])

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        if 'GrafanaReady' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['dashboard'] = self.get(managed_object, 'status:dashboards', on_error=[], on_none=[])
        info['dashboardCount'] = len(info['dashboard'])
        
        return info

    def add_grafana_info(self, info, routes, datasources):
        if datasources is not None:
            info['datasource'] = []

            datasources_mo = self.get(info, 'status:datasources', on_error=[], on_none=[])
            for datasource_mo in datasources_mo:
                try:
                    datasource_uid = datasource_mo.split('/')[2]
                except BaseException:
                    datasource_uid = None

                if datasource_uid is None:
                    continue

                for datasource in datasources:
                    if datasource['uid'] == datasource_uid:
                        ds_info = {}
                        ds_info['name'] = datasource['name']
                        ds_info['ds_type'] = datasource['ds_type']
                        ds_info['ds_name'] = datasource['ds_name']
                        ds_info['dsT'] = '%s (%s)' % (
                            datasource['ds_name'],
                            datasource['ds_type']
                        )
                        ds_info['uid'] = datasource['uid']
                        info['datasource'].append(
                            ds_info
                        )


        if routes is not None:
            info['route'] = None
            info['access'] = []
            for route in routes:
                if route['owner_kind'] == 'Grafana' and route['owner_name'] == info['name']:
                    info['route'] = route['route']
                    info['access'].append(
                        'https://%s' % (info['route'])
                    )
                    if info['credentials'] is not None:
                        info['access'].append(
                            info['credentials']
                        )

        return info
    
    def get_grafanas_info(self, cache_enabled=True):
        if cache_enabled:
            if self.grafana is not None:
                return self.grafana

        managed_objects = self.get_grafana_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.grafana = []
        for managed_object in managed_objects:
            grafana_info = {}
            grafana_info['info'] = self.get_grafana_info(
                managed_object
            )
            grafana_info['mo'] = managed_object
            self.grafana.append(
                grafana_info
            )

        return self.grafana

    def match_grafana(self, grafana_info, object_filter):
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

    def get_grafanas(self, object_filter=None, datasource_info=False, route_info=False, return_mo=False, cache_enabled=True):
        all_grafanas = self.get_grafanas_info(cache_enabled=cache_enabled)
        if all_grafanas is None:
            return None

        grafanas = []

        routes = None
        if route_info:
            routes = self.get_routes(cache_enabled=cache_enabled)

        datasources = None
        if datasource_info:
            datasources = self.get_grafana_datasources(cache_enabled=cache_enabled)

        for grafana_info in all_grafanas:
            grafana_info['info'] = self.add_grafana_info(grafana_info['info'], routes, datasources)

            if not self.match_grafana(grafana_info['info'], object_filter):
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

    def is_grafana(self, namespace, name, cache_enabled=True):
        if self.get_grafana(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_grafana(self, namespace, name, datasource_info=False, return_mo=False, cache_enabled=True, route_info=False):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        grafanas = self.get_grafanas(
            object_filter=object_filter,
            datasource_info=datasource_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled,
            route_info=route_info
        )
        if grafanas is None:
            return None

        if len(grafanas) == 1:
            return grafanas[0]

        return None
