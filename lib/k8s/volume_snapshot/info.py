import time
from lib import filter_helper


class K8sVolumeSnapshotInfo():
    def __init__(self):
        self.volume_snapshot = None

    def get_volume_snapshot_info(self, volume_snapshot_mo):
        if volume_snapshot_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_snapshot_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(volume_snapshot_mo, 'spec')
        info['status'] = self.get(volume_snapshot_mo, 'status')

        info['info'] = {}
        info['info']['class_name'] = self.get(volume_snapshot_mo, 'spec:volumeSnapshotClassName')
        info['info']['pvc'] = self.get(volume_snapshot_mo, 'spec:source:persistentVolumeClaimName')
        info['info']['size'] = self.get(volume_snapshot_mo, 'status:restoreSize')
        info['info']['ready'] = self.get(volume_snapshot_mo, 'status:readyToUse')
        if info['info']['ready']:
            info['info']['readyT'] = '\u2713'
            info['__Output']['info.readyT'] = 'Green'
        else:
            info['info']['readyT'] = '\u2717'
            info['__Output']['info.readyT'] = 'Red'

        return info

    def get_volume_snapshots_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_snapshot is not None:
                return self.volume_snapshot

        managed_objects = self.get_volume_snapshot_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_snapshot = []
        for managed_object in managed_objects:
            volume_snapshot_info = {}
            volume_snapshot_info['info'] = self.get_volume_snapshot_info(
                managed_object
            )
            volume_snapshot_info['mo'] = managed_object
            self.volume_snapshot.append(
                volume_snapshot_info
            )

        return self.volume_snapshot

    def match_volume_snapshot(self, volume_snapshot_info, volume_snapshot_filter):
        if volume_snapshot_filter is None or len(volume_snapshot_filter) == 0:
            return True

        for ap_rule in volume_snapshot_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, volume_snapshot_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (volume_snapshot_info['namespace'], volume_snapshot_info['name'])):
                    return False

            if key == 'sc':
                key_found = True
                if not filter_helper.match_string(value, volume_snapshot_info['info']['class_name']):
                    return False
                
            if key == 'pvcs':
                key_found = True
                found = False
                for item in value.split(','):
                    if not filter_helper.match_string(item.split('/')[0], volume_snapshot_info['namespace']):
                        continue

                    if not filter_helper.match_string(item.split('/')[1], volume_snapshot_info['info']['pvc']):
                        continue

                    found = True
                    break

                if not found:
                    return False
                
            if not key_found:
                self.log.error(
                    'match_volume_snapshot',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_snapshots(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_snapshots = self.get_volume_snapshots_info(cache_enabled=cache_enabled)
        if all_volume_snapshots is None:
            return None

        volume_snapshots = []

        for volume_snapshot_info in all_volume_snapshots:
            if not self.match_volume_snapshot(volume_snapshot_info['info'], object_filter):
                continue

            if return_mo:
                volume_snapshots.append(
                    volume_snapshot_info['mo']
                )
                continue

            volume_snapshots.append(
                volume_snapshot_info['info']
            )

        return volume_snapshots

    def get_volume_snapshot(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        volume_snapshots = self.get_volume_snapshots(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if volume_snapshots is None:
            return None

        if len(volume_snapshots) == 1:
            return volume_snapshots[0]

        return None

    def wait_no_volume_snapshot(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            volume_snapshot_info = self.get_volume_snapshot(
                namespace,
                name,
                cache_enabled=False
            )
            if volume_snapshot_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_volume_snapshot',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

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
    