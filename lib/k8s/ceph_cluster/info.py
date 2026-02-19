import time
from lib import filter_helper


class K8sCephClusterInfo():
    def __init__(self):
        self.ceph_cluster = None

    def get_ceph_cluster_info(self, ceph_cluster_mo):
        if ceph_cluster_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ceph_cluster_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ceph_cluster_mo, 'spec')
        info['status'] = self.get(ceph_cluster_mo, 'status')

        info['manager_count'] = self.get(ceph_cluster_mo, 'spec:mgr:count')
        info['monitor_count'] = self.get(ceph_cluster_mo, 'spec:mon:count')
        info['bytes_available'] = self.get(ceph_cluster_mo, 'status:ceph:capacity:bytesAvailable')
        info['bytes_availableT'] = self.info_handler.convert_storage(
            info['bytes_available']
        )
        info['bytes_total'] = self.get(ceph_cluster_mo, 'status:ceph:capacity:bytesTotal')
        info['bytes_totalT'] = self.info_handler.convert_storage(
            info['bytes_total']
        )
        info['bytes_used'] = self.get(ceph_cluster_mo, 'status:ceph:capacity:bytesUsed')
        info['bytes_usedT'] = self.info_handler.convert_storage(
            info['bytes_used']
        )

        try:
            info['used_pct'] = info['bytes_used'] * 100 / info['bytes_total']
            info['used_pctT'] = self.info_handler.convert_pct(
                info['used_pct']
            )
        except BaseException:
            info['used_pct'] = None
            info['used_pctT'] = 'N/A'
        
        info['health'] = self.get(ceph_cluster_mo, 'status:ceph:health', on_error='N/A', on_none='N/A')
        if info['health'] == 'HEALTH_OK':
            info['healthy'] = True
            info['healtyTick'] = '\u2713'
            info['__Output']['health'] = 'Green'
            info['__Output']['healtyTick'] = 'Green'
        else:
            info['healthy'] = True
            info['healtyTick'] = '\u2717'
            info['__Output']['health'] = 'Red'
            info['__Output']['healtyTick'] = 'Red'

        info['phase'] = self.get(ceph_cluster_mo, 'status:phase')
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

        info['state'] = self.get(ceph_cluster_mo, 'status:state')
        if info['state'] is not None and info['state'].lower() == 'created':
            info['created'] = True
            info['createdTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['createdTick'] = 'Green'
        else:
            info['created'] = False
            info['createdTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['createdTick'] = 'Red'

        info['version'] = self.get(ceph_cluster_mo, 'status:version:version')

        return info

    def get_ceph_clusters_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_cluster is not None:
                return self.ceph_cluster

        managed_objects = self.get_ceph_cluster_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ceph_cluster = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = self.get_ceph_cluster_info(
                managed_object
            )
            info['mo'] = managed_object
            self.ceph_cluster.append(
                info
            )

        return self.ceph_cluster

    def match_ceph_cluster(self, object_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, object_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (object_info['namespace'], object_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_ceph_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ceph_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_objects_infos = self.get_ceph_clusters_info(cache_enabled=cache_enabled)
        if all_objects_infos is None:
            return None

        object_infos = []

        for object_info in all_objects_infos:
            if not self.match_ceph_cluster(object_info['info'], object_filter):
                continue

            if return_mo:
                object_infos.append(
                    object_info['mo']
                )
                continue

            object_infos.append(
                object_info['info']
            )

        return object_infos

    def is_ceph_cluster(self, cache_enabled=True):
        if self.get_ceph_cluster(cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ceph_cluster(self, return_mo=False, cache_enabled=True):
        objects_info = self.get_ceph_clusters(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if objects_info is None:
            return None

        if len(objects_info) == 1:
            return objects_info[0]

        return None

    def wait_ceph_cluster(self, max_time=360):
        start_time = int(time.time())
        while True:
            if self.is_ceph_cluster(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_ceph_cluster',
                    'Max time reached'
                )
                return False

            time.sleep(5)