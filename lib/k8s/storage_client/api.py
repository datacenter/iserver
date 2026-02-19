import time
import traceback


class K8sStorageClientApi():
    def __init__(self):
        self.storage_client_mo = None

    def get_storage_client_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_client_mo is not None:
                return self.storage_client_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ocs.openshift.io/v1alpha1',
                kind='StorageClient'
            )
            self.storage_client_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'storage_client',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_storage_client_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'storage_client',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'storage_client',
            self.storage_client_mo
        )

        return self.storage_client_mo
