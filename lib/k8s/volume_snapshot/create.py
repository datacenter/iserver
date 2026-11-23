class K8sVolumeSnapshotCreate():
    def __init__(self):
        pass

    def get_volume_snapshot_definition(self, namespace, snapshot_name, storage_class, pvc_name=None):
        body = {}
        body['apiVersion'] = 'snapshot.storage.k8s.io/v1'
        body['kind'] = 'VolumeSnapshot'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = snapshot_name
        body['spec'] = {}
        body['spec']['volumeSnapshotClassName'] = storage_class
        body['spec']['source'] = {}
        if pvc_name is not None:
            body['spec']['source']['persistentVolumeClaimName'] = pvc_name
        return body