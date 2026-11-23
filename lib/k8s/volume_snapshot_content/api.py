class K8sVolumeSnapshotContentApi():
    def __init__(self):
        self.volume_snapshot_content_mo = None
        self.volume_snapshot_content_namespace_mo = {}

    def get_volume_snapshot_content_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.volume_snapshot_content_mo,
            self.volume_snapshot_content_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.volume_snapshot_content_mo, self.volume_snapshot_content_namespace_mo = self.get_namespaced_resources(
            'VolumeSnapshotContent', 
            'snapshot.storage.k8s.io/v1', 
            self.volume_snapshot_content_mo,
            self.volume_snapshot_content_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response