class K8sGrafanaInfo():
    def __init__(self):
        self.grafana = None

    def get_grafana_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)

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

    def get_grafanas(self, object_filter=None, datasource_info=False, route_info=False, return_mo=False, cache_enabled=True):
        all_grafanas = self.get_infos(
            'grafana', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if all_grafanas is None:
            return None

        if return_mo:
            return all_grafanas
        
        grafanas = []

        routes = None
        if route_info:
            routes = self.get_routes(cache_enabled=cache_enabled)

        datasources = None
        if datasource_info:
            datasources = self.get_grafana_datasources(cache_enabled=cache_enabled)

        for grafana_info in all_grafanas:
            grafana_info = self.add_grafana_info(grafana_info, routes, datasources)
            grafanas.append(
                grafana_info
            )

        return grafanas

    def get_grafana(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'grafana', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_grafana(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_grafana(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True