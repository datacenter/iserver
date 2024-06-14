from lib import filter_helper


class K8sClusterQuotaInfo():
    def __init__(self):
        self.cluster_quota = None

    def get_cluster_quota_info(self, cluster_quota_mo):
        if cluster_quota_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_quota_mo
        )
        info.update(metadata_info)

        return info

    def get_cluster_quotas_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_quota is not None:
                return self.cluster_quota

        managed_objects = self.get_cluster_quota_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_quota = []
        for managed_object in managed_objects:
            cluster_quota_info = {}
            cluster_quota_info['info'] = self.get_cluster_quota_info(
                managed_object
            )
            cluster_quota_info['mo'] = managed_object
            self.cluster_quota.append(
                cluster_quota_info
            )

        return self.cluster_quota

    def match_cluster_quota(self, cluster_quota_info, cluster_quota_filter):
        if cluster_quota_filter is None or len(cluster_quota_filter) == 0:
            return True

        for ap_rule in cluster_quota_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_cluster_quota',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_quotas(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cluster_quotas = self.get_cluster_quotas_info(cache_enabled=cache_enabled)
        if all_cluster_quotas is None:
            return None

        cluster_quotas = []

        for cluster_quota_info in all_cluster_quotas:
            if not self.match_cluster_quota(cluster_quota_info['info'], object_filter):
                continue

            if return_mo:
                cluster_quotas.append(
                    cluster_quota_info['mo']
                )
                continue

            cluster_quotas.append(
                cluster_quota_info['info']
            )

        return cluster_quotas
