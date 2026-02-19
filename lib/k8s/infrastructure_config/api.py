import time
import traceback


class K8sInfrastructureConfigApi():
    def __init__(self):
        self.infrastructure_config_mo = None

    def get_infrastructure_config_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.infrastructure_config_mo is not None:
                return self.infrastructure_config_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='config.openshift.io/v1',
                kind='Infrastructure'
            )
            self.infrastructure_config_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'infrastructure_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_infrastructure_config_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'infrastructure_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'infrastructure_config',
            self.infrastructure_config_mo
        )

        return self.infrastructure_config_mo
