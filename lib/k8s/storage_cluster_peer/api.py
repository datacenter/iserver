import time
import traceback


class K8sStorageClusterPeerApi():
    def __init__(self):
        self.storage_cluster_peer_mo = None

    def get_storage_cluster_peer_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_cluster_peer_mo is not None:
                return self.storage_cluster_peer_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ocs.openshift.io/v1',
                kind='StorageClusterPeer'
            )
            self.storage_cluster_peer_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'storage_cluster_peer',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_storage_cluster_peer_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'storage_cluster_peer',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'storage_cluster_peer',
            self.storage_cluster_peer_mo
        )

        return self.storage_cluster_peer_mo
