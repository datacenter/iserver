import time
import traceback


class K8sHostPathProvisionerApi():
    def __init__(self):
        self.host_path_provisioner_mo = None

    def get_host_path_provisioner_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.host_path_provisioner_mo is not None:
                return self.host_path_provisioner_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='hostpathprovisioner.kubevirt.io/v1beta1',
                kind='HostPathProvisioner'
            )
            self.host_path_provisioner_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'host_path_provisioner',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_host_path_provisioner_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'host_path_provisioner',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'host_path_provisioner',
            self.host_path_provisioner_mo
        )

        return self.host_path_provisioner_mo
