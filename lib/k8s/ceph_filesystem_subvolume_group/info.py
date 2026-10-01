from lib import filter_helper


class K8sCephFilesystemSubVolumeGroupInfo():
    def __init__(self):
        self.ceph_filesystem_subvolume_group = None

    def get_ceph_filesystem_subvolume_group_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)

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

        info['cluster_id'] = self.get(managed_object, 'status:info:clusterID')
        info['pinning'] = self.get(managed_object, 'status:info:pinning')

        return info

    def get_ceph_filesystem_subvolume_groups(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_filesystem_subvolume_group', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_filesystem_subvolume_group(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_filesystem_subvolume_group', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_filesystem_subvolume_group(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_filesystem_subvolume_group(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_filesystem_subvolume_group(self, cache_enabled=True):
        infos = self.get_ceph_filesystem_subvolume_groups(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True