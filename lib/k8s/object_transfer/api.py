import time
import traceback


class K8sObjectTransferApi():
    def __init__(self):
        self.object_transfer_mo = None

    def get_object_transfer_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.object_transfer_mo is not None:
                return self.object_transfer_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cdi.kubevirt.io/v1beta1',
                kind='ObjectTransfer'
            )
            self.object_transfer_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'object_transfer',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_object_transfer_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'object_transfer',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'object_transfer',
            self.object_transfer_mo
        )

        return self.object_transfer_mo
