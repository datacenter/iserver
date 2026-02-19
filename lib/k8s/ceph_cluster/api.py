import time
import traceback


class K8sCephClusterApi():
    def __init__(self):
        self.ceph_cluster_mo = None

    def get_ceph_cluster_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_cluster_mo is not None:
                return self.ceph_cluster_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ceph.rook.io/v1',
                kind='CephCluster'
            )
            self.ceph_cluster_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'ceph_cluster',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_ceph_cluster_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'ceph_cluster',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'ceph_cluster',
            self.ceph_cluster_mo
        )

        return self.ceph_cluster_mo
