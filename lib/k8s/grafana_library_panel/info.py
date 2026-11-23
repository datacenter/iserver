from lib import filter_helper


class K8sGrafanaLibraryPanelInfo():
    def __init__(self):
        self.grafana_library_panel = None

    def get_grafana_library_panel_info(self, grafana_library_panel_mo):
        if grafana_library_panel_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            grafana_library_panel_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(grafana_library_panel_mo, 'spec')
        return info

    def get_grafana_library_panels_info(self, cache_enabled=True):
        if cache_enabled:
            if self.grafana_library_panel is not None:
                return self.grafana_library_panel

        managed_objects = self.get_grafana_library_panel_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.grafana_library_panel = []
        for managed_object in managed_objects:
            grafana_info = {}
            grafana_info['info'] = self.get_grafana_info(
                managed_object
            )
            grafana_info['mo'] = managed_object
            self.grafana_library_panel.append(
                grafana_info
            )

        return self.grafana_library_panel

    def match_grafana_library_panel(self, grafana_info, object_filter):
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

    def get_grafana_library_panels(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_grafanas = self.get_grafana_library_panels_info(cache_enabled=cache_enabled)
        if all_grafanas is None:
            return None

        grafanas = []

        for grafana_info in all_grafanas:
            if not self.match_grafana_library_panel(grafana_info['info'], object_filter):
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

    def is_grafana_library_panel(self, namespace, name, cache_enabled=True):
        if self.get_grafana_library_panel(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_grafana_library_panel(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        grafanas = self.get_grafana_library_panels(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if grafanas is None:
            return None

        if len(grafanas) == 1:
            return grafanas[0]

        return None

    def set_grafana_library_panel(self, namespace, name, library_panel_selector, jbody):
        body = {}
        body['kind'] = 'GrafanaLibraryPanel'
        body['apiVersion'] = 'grafana.integreatly.org/v1beta1'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['instanceSelector'] = {}
        body['spec']['instanceSelector']['matchLabels'] = {}
        body['spec']['instanceSelector']['matchLabels']['library_panels'] = library_panel_selector
        body['spec']['json'] = jbody

        grafana_library_panel_mo = self.get_grafana_library_panel(namespace, name, cache_enabled=False, return_mo=True)
        if grafana_library_panel_mo is not None:
            body['metadata']['resourceVersion'] = self.get(grafana_library_panel_mo, 'metadata:resourceVersion')
            return self.replace_grafana_library_panel(body)

        return self.create_grafana_library_panel(body)
