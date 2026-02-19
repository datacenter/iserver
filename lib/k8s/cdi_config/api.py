import time
import traceback


class K8sCdiConfigApi():
    def __init__(self):
        self.cdi_config_mo = None

    def get_cdi_config_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cdi_config_mo is not None:
                return self.cdi_config_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cdi.kubevirt.io/v1beta1',
                kind='CDIConfig'
            )
            self.cdi_config_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'cdi_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_cdi_config_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'cdi_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'cdi_config',
            self.cdi_config_mo
        )

        return self.cdi_config_mo
