import time
import traceback


class K8sOpenstackVolumePopulatorApi():
    def __init__(self):
        self.openstack_volume_populator_mo = None

    def get_openstack_volume_populator_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.openstack_volume_populator_mo is not None:
                return self.openstack_volume_populator_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.cdi.kubevirt.io/v1beta1',
                kind='OpenstackVolumePopulator'
            )
            self.openstack_volume_populator_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'openstack_volume_populator',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_openstack_volume_populator_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'openstack_volume_populator',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'openstack_volume_populator',
            self.openstack_volume_populator_mo
        )

        return self.openstack_volume_populator_mo
