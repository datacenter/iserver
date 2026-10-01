class K8sGrafanaDashboardWait():
    def __init__(self):
        pass

    def wait_grafana_dashboard(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='GrafanaDashboard', max_time=60):
        return self.wait_managed_object(
            'grafana_dashboard',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_grafana_dashboard(self, namespace, name, max_time=60, my_output=None, prompt='GrafanaDashboard'):
        return self.wait_no_managed_object(
            'grafana_dashboard',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )