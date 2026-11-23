from lib import filter_helper


class OspSnapshotInfo():
    def __init__(self):
        self.snapshot = None

    def get_snapshots_properties(self, managed_objects):
        properties = []
        for managed_object in managed_objects:
            properties.append(
                managed_object.to_dict()
            )
        return properties

    def get_snapshot_info(self, snapshot_mo):
        if snapshot_mo is None:
            return None

        properties = snapshot_mo.to_dict()
        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'description',
            'volume_id',
            'status',
            'size',
            'metadata',
            'created_at',
            'updated_at'
        ]
        for key in keys:
            info[key] = None
            if key in properties:
                info[key] = properties[key]

        info['tenant_id'] = None
        if 'os-extended-snapshot-attributes:project_id' in properties:
            info['tenant_id'] = properties['os-extended-snapshot-attributes:project_id']

        info['progress'] = None
        if 'os-extended-snapshot-attributes:progress' in properties:
            info['progress'] = properties['os-extended-snapshot-attributes:progress']

        if info['status'] == 'available':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        info['created_age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        info['updated_age'] = self.convert_timestamp_to_age(
            info['updated_at'],
            on_error='--'
        )

        return info

    def get_snapshots_info(self, cache_enabled=True):
        if cache_enabled:
            if self.snapshot is not None:
                return self.snapshot

        managed_objects = self.get_snapshot_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'snapshots',
            self.get_snapshots_properties(managed_objects)
        )

        self.snapshot = []
        for managed_object in managed_objects:
            snapshot_info = self.get_snapshot_info(
                managed_object
            )
            self.snapshot.append(
                snapshot_info
            )

        self.log.osp_mo(
            'snapshots.info',
            self.snapshot
        )

        return self.snapshot

    def match_snapshot(self, snapshot_info, snapshot_filter):
        if snapshot_filter is None or len(snapshot_filter) == 0:
            return True

        for ap_rule in snapshot_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if len(value.split('/')) == 1:
                    if not filter_helper.match_string(value, snapshot_info['name']):
                        return False
                if len(value.split('/')) == 2:
                    if not filter_helper.match_string(value.split('/')[1], snapshot_info['name']):
                        return False

                    if 'tenant_name' in snapshot_info:
                        if not filter_helper.match_string(value.split('/')[0], snapshot_info['tenant_name']):
                            return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, snapshot_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in snapshot_info:
                    if not filter_helper.match_string(value, snapshot_info['tenant_name']):
                        return False

            if key == 'volume_id':
                key_found = True
                if not filter_helper.match_string(value, snapshot_info['volume_id']):
                    return False

            if key == 'volume_name':
                key_found = True
                if 'volume_name' in snapshot_info:
                    if not filter_helper.match_string(value, snapshot_info['volume_name']):
                        return False

            if not key_found:
                self.log.error(
                    'match_snapshot',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_snapshots(self, object_filter=None, tenant_info=False, volume_info=False, cache_enabled=True):
        all_snapshots = self.get_snapshots_info(cache_enabled=cache_enabled)
        if all_snapshots is None:
            return None

        snapshots = []

        for snapshot_info in all_snapshots:
            if not self.match_snapshot(snapshot_info, object_filter):
                continue

            if tenant_info:
                snapshot_info['tenant_name'] = self.get_tenant_name(
                    snapshot_info['tenant_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_snapshot(snapshot_info, object_filter):
                    continue

            if volume_info:
                snapshot_info['volume_name'] = self.get_volume_name(
                    snapshot_info['volume_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_snapshot(snapshot_info, object_filter):
                    continue

            snapshots.append(
                snapshot_info
            )

        return snapshots
