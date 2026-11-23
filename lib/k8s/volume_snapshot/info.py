class K8sVolumeSnapshotInfo():
    def __init__(self):
        self.volume_snapshot = None

    def get_volume_snapshot_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)

        info['info'] = {}
        info['info']['class_name'] = self.get(managed_object, 'spec:volumeSnapshotClassName')
        info['info']['pvc'] = self.get(managed_object, 'spec:source:persistentVolumeClaimName')
        info['info']['size'] = self.get(managed_object, 'status:restoreSize')
        info['info']['ready'] = self.get(managed_object, 'status:readyToUse')
        if info['info']['ready']:
            info['info']['readyT'] = '\u2713'
            info['__Output']['info.readyT'] = 'Green'
        else:
            info['info']['readyT'] = '\u2717'
            info['__Output']['info.readyT'] = 'Red'

        return info

    def get_volume_snapshots(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'volume_snapshot', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_volume_snapshot(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'volume_snapshot', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_volume_snapshot(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_volume_snapshot(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_volume_snapshot(self, cache_enabled=True):
        infos = self.get_volume_snapshots(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True