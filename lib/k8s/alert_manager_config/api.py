import time
import traceback


class K8sAlertManagerConfigApi():
    def __init__(self):
        self.alert_manager_config_mo = None

    def get_alert_manager_config_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.alert_manager_config_mo is not None:
                return self.alert_manager_config_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='monitoring.coreos.com/v1beta1',
                kind='AlertmanagerConfig'
            )
            self.alert_manager_config_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'alert_manager_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_alert_manager_config_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'alert_manager_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'alert_manager_config',
            self.alert_manager_config_mo
        )

        return self.alert_manager_config_mo
