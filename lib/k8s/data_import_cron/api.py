import time
import traceback


class K8sDataImportCronApi():
    def __init__(self):
        self.data_import_cron_mo = None

    def get_data_import_cron_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.data_import_cron_mo is not None:
                return self.data_import_cron_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cdi.kubevirt.io/v1beta1',
                kind='DataImportCron'
            )
            self.data_import_cron_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'data_import_cron',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_data_import_cron_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'data_import_cron',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'data_import_cron',
            self.data_import_cron_mo
        )

        return self.data_import_cron_mo
