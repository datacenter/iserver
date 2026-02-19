import time


class K8sGrafanaDatasourceWait():
    def __init__(self):
        pass
    
    def wait_grafana_datasource(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            datasource_info = self.get_grafana_datasource(
                namespace,
                name,
                cache_enabled=False
            )
            if datasource_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_grafana_datasource',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

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

    def wait_no_grafana_datasource(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            grafana_info = self.get_grafana_datasource(
                namespace,
                name,
                cache_enabled=False
            )
            if grafana_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_grafana_datasource',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
