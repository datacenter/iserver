import time
import traceback


class K8sLogicalVolumeApi():
    def __init__(self):
        self.logical_volume_mo = None

    def get_logical_volume_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.logical_volume_mo is not None:
                return self.logical_volume_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='topolvm.io/v1',
                kind='LogicalVolume'
            )
            self.logical_volume_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'logical_volume',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_logical_volume_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'logical_volume',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'logical_volume',
            self.logical_volume_mo
        )

        return self.logical_volume_mo
