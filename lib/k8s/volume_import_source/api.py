import time
import traceback


class K8sVolumeImportSourceApi():
    def __init__(self):
        self.volume_import_source_mo = None

    def get_volume_import_source_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_import_source_mo is not None:
                return self.volume_import_source_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cdi.kubevirt.io/v1beta1',
                kind='VolumeImportSource'
            )
            self.volume_import_source_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'volume_import_source',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_volume_import_source_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'volume_import_source',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'volume_import_source',
            self.volume_import_source_mo
        )

        return self.volume_import_source_mo
