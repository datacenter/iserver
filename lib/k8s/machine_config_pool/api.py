import time
import traceback


class K8sMachineConfigPoolApi():
    def __init__(self):
        self.machine_config_pool_mo = None

    def get_machine_config_pool_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.machine_config_pool_mo is not None:
                return self.machine_config_pool_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='machineconfiguration.openshift.io/v1',
                kind='MachineConfigPool'
            )
            self.machine_config_pool_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'machine_config_pool',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_machine_config_pool_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'machine_config_pool',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'machine_config_pool',
            self.machine_config_pool_mo
        )

        return self.machine_config_pool_mo
