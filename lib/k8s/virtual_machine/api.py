import time
import traceback


class K8sVirtualMachineApi():
    def __init__(self):
        self.virtual_machine_mo = None

    def get_virtual_machine_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                return self.virtual_machine_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='kubevirt.io/v1',
                kind='VirtualMachine'
            )
            self.virtual_machine_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_virtual_machine_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'virtual_machine',
            self.virtual_machine_mo
        )

        return self.virtual_machine_mo
