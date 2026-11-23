class K8sVolumeSnapshotClassApi():
    def __init__(self):
        self.volume_snapshot_class_mo = None

    def get_volume_snapshot_class_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.volume_snapshot_class_mo
        )
        if cache_hit:
            return response

        response, self.volume_snapshot_class_mo = self.get_resources(
            'VolumeSnapshotClass', 
            'snapshot.storage.k8s.io/v1', 
            self.volume_snapshot_class_mo,
            name=name
        )

        return response