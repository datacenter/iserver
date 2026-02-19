from lib import filter_helper


class K8sPortworxStorageClusterInfo():
    def __init__(self):
        self.portworx_storage_cluster = None

    def get_portworx_storage_cluster_info(self, portworx_storage_cluster_mo):
        if portworx_storage_cluster_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            portworx_storage_cluster_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(portworx_storage_cluster_mo, 'spec')
        info['status'] = self.get(portworx_storage_cluster_mo, 'status')

        info['local_storage_sc'] = None
        info['storage_class'] = None
        devices_mo = self.get(portworx_storage_cluster_mo, 'spec:storageDeviceSets', on_error=[], on_none=[])
        for device_mo in devices_mo:
            info['local_storage_sc'] = self.get(device_mo, 'dataPVCTemplate:spec:storageClassName')
            info['storage_class'] = self.get(device_mo, 'name')

        info['phase'] = self.get(portworx_storage_cluster_mo, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['hostnames'] = self.get(portworx_storage_cluster_mo, 'status:nodeTopologies:labels:kubernetes.io/hostname', on_error=[], on_none=[])
        if len(info['hostnames']) == 0:
            info['hostnamesT'] = '--'
        else:
            info['hostnamesT'] = ', '.join(info['hostnames'])
        
        info['version'] = self.get(portworx_storage_cluster_mo, 'status:version')
        info['current_mon_count'] = self.get(portworx_storage_cluster_mo, 'status:currentMonCount')
        info['expected_osd_count'] = None
        device_sets_mo = self.get(portworx_storage_cluster_mo, 'spec:storageDeviceSets')
        if device_sets_mo is not None and len(device_sets_mo) == 1:
            try:
                info['expected_osd_count'] = self.get(device_sets_mo[0], 'replica') * self.get(device_sets_mo[0], 'count')
            except BaseException:
                pass

        return info

    def get_portworx_storage_clusters_info(self, cache_enabled=True):
        if cache_enabled:
            if self.portworx_storage_cluster is not None:
                return self.portworx_storage_cluster

        managed_objects = self.get_portworx_storage_cluster_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.portworx_storage_cluster = []
        for managed_object in managed_objects:
            portworx_storage_cluster_info = {}
            portworx_storage_cluster_info['info'] = self.get_portworx_storage_cluster_info(
                managed_object
            )
            portworx_storage_cluster_info['mo'] = managed_object
            self.portworx_storage_cluster.append(
                portworx_storage_cluster_info
            )

        return self.portworx_storage_cluster

    def match_portworx_storage_cluster(self, portworx_storage_cluster_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, portworx_storage_cluster_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, portworx_storage_cluster_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_portworx_storage_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_portworx_storage_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_portworx_storage_clusters = self.get_portworx_storage_clusters_info(cache_enabled=cache_enabled)
        if all_portworx_storage_clusters is None:
            return None

        portworx_storage_clusters = []

        for portworx_storage_cluster_info in all_portworx_storage_clusters:
            if not self.match_portworx_storage_cluster(portworx_storage_cluster_info['info'], object_filter):
                continue

            if return_mo:
                portworx_storage_clusters.append(
                    portworx_storage_cluster_info['mo']
                )
                continue

            portworx_storage_clusters.append(
                portworx_storage_cluster_info['info']
            )

        return portworx_storage_clusters

    def is_portworx_storage_cluster(self, cache_enabled=True):
        if self.get_portworx_storage_cluster(cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_portworx_storage_cluster(self, return_mo=False, cache_enabled=True):
        portworx_storage_clusters = self.get_portworx_storage_clusters(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if portworx_storage_clusters is None:
            return None

        if len(portworx_storage_clusters) == 1:
            return portworx_storage_clusters[0]

        return None

