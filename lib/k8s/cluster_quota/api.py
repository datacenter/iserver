import time
import traceback


class K8sClusterQuotaApi():
    def __init__(self):
        self.cluster_quota_mo = None

    def get_cluster_quota_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_quota_mo is not None:
                return self.cluster_quota_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='quota.openshift.io/v1',
                kind='ClusterResourceQuota'
            )
            self.cluster_quota_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'cluster_quota',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_cluster_quota_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'cluster_quota',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'cluster_quota',
            self.cluster_quota_mo
        )

        return self.cluster_quota_mo
