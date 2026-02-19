import time
import traceback


class K8sGrafanaApi():
    def __init__(self):
        self.grafana_mo = None

    def get_grafana_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.grafana_mo is not None:
                return self.grafana_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='grafana.integreatly.org/v1beta1',
                kind='Grafana'
            )
            self.grafana_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'grafana',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_grafana_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'grafana',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'grafana',
            self.grafana_mo
        )

        return self.grafana_mo

    def create_grafana_mo(self, grafana):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='grafana.integreatly.org/v1beta1', kind='Grafana')
            success = True
            response = obj_list.create(
                body=grafana,
                namespace=grafana['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_grafana_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'grafana',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_grafana_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='grafana.integreatly.org/v1beta1', kind='Grafana')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_grafana_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'grafana',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_grafana_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='grafana.integreatly.org/v1beta1', kind='Grafana')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_grafana', traceback.format_exc())

        self.log.ocp(
            'delete',
            'grafana',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
