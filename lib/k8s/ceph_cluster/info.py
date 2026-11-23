class K8sCephClusterInfo():
    def __init__(self):
        self.ceph_cluster = None

    def get_ceph_cluster_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)

        info['manager_count'] = self.get(managed_object, 'spec:mgr:count')
        info['monitor_count'] = self.get(managed_object, 'spec:mon:count')
        info['bytes_available'] = self.get(managed_object, 'status:ceph:capacity:bytesAvailable')
        info['bytes_availableT'] = self.info_handler.convert_storage(
            info['bytes_available']
        )
        info['bytes_total'] = self.get(managed_object, 'status:ceph:capacity:bytesTotal')
        info['bytes_totalT'] = self.info_handler.convert_storage(
            info['bytes_total']
        )
        info['bytes_used'] = self.get(managed_object, 'status:ceph:capacity:bytesUsed')
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
        
        info['health'] = self.get(managed_object, 'status:ceph:health', on_error='N/A', on_none='N/A')
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

        info['phase'] = self.get(managed_object, 'status:phase')
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

        info['state'] = self.get(managed_object, 'status:state')
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

        info['version'] = self.get(managed_object, 'status:version:version')

        return info

    def get_ceph_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_cluster', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_cluster(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_cluster', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_cluster(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_cluster(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_cluster(self, cache_enabled=True):
        infos = self.get_ceph_clusters(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True