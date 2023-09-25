import time
import traceback


class K8sMachineConfigApi():
    def __init__(self):
        self.machine_config_mo = None

    def get_machine_config_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.machine_config_mo is not None:
                return self.machine_config_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='machineconfiguration.openshift.io/v1',
                kind='MachineConfig'
            )
            self.machine_config_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'machine_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_machine_config_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'machine_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'machine_config',
            self.machine_config_mo
        )

        return self.machine_config_mo

    def set_machine_config_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='machineconfiguration.openshift.io/v1', kind='MachineConfig')
            response = obj_list.replace(
                body=body
            )
            self.log.k8s(
                'set',
                'machine_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_machine_config_mo', traceback.format_exc())
            self.log.k8s(
                'set',
                'machine_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True
