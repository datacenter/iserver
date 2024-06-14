import time
import traceback


class K8sVirtualMachineClusterPreferenceApi():
    def __init__(self):
        self.virtual_machine_cluster_preference_mo = None

    def get_virtual_machine_cluster_preference_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_cluster_preference_mo is not None:
                return self.virtual_machine_cluster_preference_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='instancetype.kubevirt.io/v1alpha2',
                kind='VirtualMachineClusterPreference'
            )
            self.virtual_machine_cluster_preference_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'virtual_machine_cluster_preference',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_virtual_machine_cluster_preference_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'virtual_machine_cluster_preference',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'virtual_machine_cluster_preference',
            self.virtual_machine_cluster_preference_mo
        )

        return self.virtual_machine_cluster_preference_mo
