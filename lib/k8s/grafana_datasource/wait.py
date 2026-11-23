import time


class K8sGrafanaDatasourceWait():
    def __init__(self):
        pass

    def wait_grafana_datasource(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='GrafanaDatasource', max_time=60):
        return self.wait_managed_object(
            'grafana_datasource',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_grafana_datasource(self, namespace, name, max_time=60, my_output=None, prompt='GrafanaDatasource'):
        return self.wait_no_managed_object(
            'grafana_datasource',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_grafana_datasource_in_instance(self, namespace, name, instance, max_time=360):
        start_time = int(time.time())
        while True:
            grafana_info = self.get_grafana(
                namespace,
                instance,
                datasource_info=True,
                cache_enabled=False
            )
            if grafana_info is not None:
                for grafana_datasource in grafana_info['datasource']:
                    if grafana_datasource['name'] == name:
                        return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_grafana_datasource_in_instance',
                    'Max time reached: %s/%s instance %s' % (namespace, name, instance)
                )
                return False

            time.sleep(5)