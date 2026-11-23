class K8sGrafanaLibraryPanelApi():
    def __init__(self):
        self.grafana_library_panel_mo = None
        self.grafana_library_panel_namespace_mo = {}

    def get_grafana_library_panel_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.grafana_library_panel_mo,
            self.grafana_library_panel_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.grafana_library_panel_mo, self.grafana_library_panel_namespace_mo = self.get_namespaced_resources(
            'GrafanaLibraryPanel', 
            'grafana.integreatly.org/v1beta1', 
            self.grafana_library_panel_mo,
            self.grafana_library_panel_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_grafana_library_panel_mo(self, namespace, name):
        success, _ = self.delete_resource('GrafanaLibraryPanel', 'grafana.integreatly.org/v1beta1', name, namespace=namespace)
        return success