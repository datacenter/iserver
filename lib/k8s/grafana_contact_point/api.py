class K8sGrafanaContactPointApi():
    def __init__(self):
        self.grafana_contact_point_mo = None
        self.grafana_contact_point_namespace_mo = {}

    def get_grafana_contact_point_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.grafana_contact_point_mo,
            self.grafana_contact_point_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.grafana_contact_point_mo, self.grafana_contact_point_namespace_mo = self.get_namespaced_resources(
            'GrafanaContactPoint', 
            'grafana.integreatly.org/v1beta1', 
            self.grafana_contact_point_mo,
            self.grafana_contact_point_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_grafana_contact_point_mo(self, namespace, name):
        success, _ = self.delete_resource('GrafanaContactPoint', 'grafana.integreatly.org/v1beta1', name, namespace=namespace)
        return success