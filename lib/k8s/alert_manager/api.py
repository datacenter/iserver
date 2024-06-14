import time
import traceback


class K8sAlertManagerApi():
    def __init__(self):
        self.alert_manager_mo = None

    def get_alert_manager_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.alert_manager_mo is not None:
                return self.alert_manager_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='monitoring.coreos.com/v1',
                kind='Alertmanager'
            )
            self.alert_manager_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'alert_manager',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_alert_manager_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'alert_manager',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'alert_manager',
            self.alert_manager_mo
        )

        return self.alert_manager_mo
