import time
import traceback


class K8sNetworkApi():
    def __init__(self):
        self.network_mo = None

    def get_network_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.network_mo is not None:
                return self.network_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='config.openshift.io/v1',
                kind='Network'
            )
            self.network_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'network',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_network_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'network',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'network',
            self.network_mo
        )

        return self.network_mo

    def patch_network_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            obj_list = api_handler.resources.get(api_version='config.openshift.io/v1', kind='Network')
            obj_list.patch(
                body=body,
                content_type='application/merge-patch+json'
            )

        except BaseException:
            self.log.error('k8s.patch_network_mo', traceback.format_exc())
            print(traceback.format_exc())
            return False

        return True
    