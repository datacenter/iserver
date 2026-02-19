import time
import traceback


class K8sGrafanaNotificationPolicyRouteApi():
    def __init__(self):
        self.grafana_notification_policy_route_mo = None

    def get_grafana_notification_policy_route_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.grafana_notification_policy_route_mo is not None:
                return self.grafana_notification_policy_route_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='grafana.integreatly.org/v1beta1',
                kind='GrafanaDashboard'
            )
            self.grafana_notification_policy_route_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'grafana_notification_policy_route',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_grafana_notification_policy_route_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'grafana_notification_policy_route',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'grafana_notification_policy_route',
            self.grafana_notification_policy_route_mo
        )

        return self.grafana_notification_policy_route_mo

    def create_grafana_notification_policy_route_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='grafana.integreatly.org/v1beta1', kind='GrafanaDashboard')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_grafana_notification_policy_route', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_grafana_notification_policy_route',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_grafana_notification_policy_route_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='grafana.integreatly.org/v1beta1', kind='GrafanaDashboard')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_grafana_notification_policy_route', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_grafana_notification_policy_route',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_grafana_notification_policy_route_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='grafana.integreatly.org/v1beta1', kind='GrafanaDashboard')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_grafana_notification_policy_route', traceback.format_exc())

        self.log.ocp(
            'delete',
            'grafana_notification_policy_route',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
