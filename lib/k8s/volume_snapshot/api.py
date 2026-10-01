class K8sVolumeSnapshotApi():
    def __init__(self):
        self.volume_snapshot_mo = None
        self.volume_snapshot_namespace_mo = {}

    def get_volume_snapshot_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.volume_snapshot_mo,
            self.volume_snapshot_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.volume_snapshot_mo, self.volume_snapshot_namespace_mo = self.get_namespaced_resources(
            'VolumeSnapshot', 
            'snapshot.storage.k8s.io/v1', 
            self.volume_snapshot_mo,
            self.volume_snapshot_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_volume_snapshot_mo(self, namespace, name):
        success, _ = self.delete_resource('VolumeSnapshot', 'snapshot.storage.k8s.io/v1', name, namespace=namespace)
        return success