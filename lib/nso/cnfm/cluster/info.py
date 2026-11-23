from lib import filter_helper


class NsoCnfmClusterInfo():
    def __init__(self):
        self.cnfm_cluster = {}

    def get_cnfm_cluster_info(self, cnfm_cluster_mo):
        if cnfm_cluster_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = self.get(
            cnfm_cluster_mo,
            'name'
        )

        return info

    def get_cnfm_clusters_info(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.cnfm_cluster:
                return self.cnfm_cluster[device_name]

        managed_objects = self.get_cnfm_cluster_mo(device_name, cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cnfm_cluster[device_name] = []
        for managed_object in managed_objects:
            cnfm_cluster_info = self.get_cnfm_cluster_info(
                managed_object
            )
            self.cnfm_cluster[device_name].append(
                cnfm_cluster_info
            )

        return self.cnfm_cluster[device_name]

    def match_cnfm_cluster(self, cnfm_cluster_info, cnfm_cluster_filter):
        if cnfm_cluster_filter is None or len(cnfm_cluster_filter) == 0:
            return True

        for ap_rule in cnfm_cluster_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cnfm_cluster_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_clusters(self, device_name, object_filter=None, cache_enabled=True):
        all_cnfm_clusters = self.get_cnfm_clusters_info(device_name, cache_enabled=cache_enabled)
        if all_cnfm_clusters is None:
            return None

        cnfm_clusters = []

        for cnfm_cluster_info in all_cnfm_clusters:
            if not self.match_cnfm_cluster(cnfm_cluster_info, object_filter):
                continue

            cnfm_clusters.append(
                cnfm_cluster_info
            )

        return cnfm_clusters
