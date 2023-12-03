from lib import filter_helper


class OspVolumeInfo():
    def __init__(self):
        self.volume = None

    def get_volumes_properties(self, managed_objects):
        properties = []
        for managed_object in managed_objects:
            properties.append(
                managed_object.to_dict()
            )
        return properties

    def get_volume_info(self, volume_mo):
        if volume_mo is None:
            return None

        properties = volume_mo.to_dict()

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'status',
            'size',
            'availability_zone',
            'created_at',
            'updated_at',
            'name',
            'description',
            'volume_type',
            'snapshot_id',
            'bootable',
            'encrypted',
            'multiattach',
            'volume_image_metadata'
        ]
        for key in keys:
            info[key] = None
            if key in properties:
                info[key] = properties[key]

        info['tenant_id'] = properties['os-vol-tenant-attr:tenant_id']

        keys = [
            'attachment_id',
            'server_id',
            'host_name',
            'device',
            'attached_at'
        ]
        info['attachment'] = []
        for attachment_mo in properties['attachments']:
            attachment_info = {}
            for key in keys:
                attachment_info[key] = None
                if key in attachment_mo:
                    attachment_info[key] = attachment_mo[key]
            info['attachment'].append(
                attachment_info
            )

        if info['status'] == 'available':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        if info['bootable'] == 'true':
            info['bootableTick'] = '\u2713'
        else:
            info['bootableTick'] = '\u2717'

        if info['encrypted']:
            info['encryptedTick'] = '\u2713'
        else:
            info['encryptedTick'] = '\u2717'

        if info['multiattach']:
            info['multiattachTick'] = '\u2713'
        else:
            info['multiattachTick'] = '\u2717'

        if info['snapshot_id'] is not None:
            info['snapshotTick'] = '\u2713'
        else:
            info['snapshotTick'] = '\u2717'

        info['created_age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        info['updated_age'] = self.convert_timestamp_to_age(
            info['updated_at'],
            on_error='--'
        )

        return info

    def get_volumes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume is not None:
                return self.volume

        managed_objects = self.get_volume_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'volumes',
            self.get_volumes_properties(managed_objects)
        )

        self.volume = []
        for managed_object in managed_objects:
            volume_info = self.get_volume_info(
                managed_object
            )
            self.volume.append(
                volume_info
            )

        self.log.osp_mo(
            'volumes.info',
            self.volume
        )

        return self.volume

    def match_volume(self, volume_info, volume_filter):
        if volume_filter is None or len(volume_filter) == 0:
            return True

        for ap_rule in volume_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, volume_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, volume_info['name']):
                    return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, volume_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in volume_info:
                    if not filter_helper.match_string(value, volume_info['tenant_name']):
                        return False

            if key == 'vm_id':
                key_found = True
                found = False
                for attachment_info in volume_info['attachment']:
                    if filter_helper.match_string(value, attachment_info['server_id']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'vm_name':
                key_found = True
                vm_name_ready = True
                found = False
                for attachment_info in volume_info['attachment']:
                    if 'vm_tenant_name' not in attachment_info:
                        vm_name_ready = False
                        break

                    if filter_helper.match_string(value, attachment_info['vm_tenant_name']):
                        found = True
                        break

                if vm_name_ready and not found:
                    return False

            if key == 'hv':
                key_found = True
                found = False
                for attachment_info in volume_info['attachment']:
                    if filter_helper.match_string(value, attachment_info['host_name']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_volume',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volumes(self, object_filter=None, tenant_info=False, vm_info=False, cache_enabled=True):
        all_volumes = self.get_volumes_info(cache_enabled=cache_enabled)
        if all_volumes is None:
            return None

        volumes = []

        for volume_info in all_volumes:
            if not self.match_volume(volume_info, object_filter):
                continue

            if tenant_info:
                volume_info['tenant_name'] = self.get_tenant_name(
                    volume_info['tenant_id'],
                    cache_enabled=cache_enabled
                )

                if not self.match_volume(volume_info, object_filter):
                    continue

            if vm_info:
                for attachment_info in volume_info['attachment']:
                    attachment_info['vm_tenant_name'] = self.get_virtual_machine_tenant_name(
                        attachment_info['server_id'],
                        cache_enabled=cache_enabled
                    )

            volumes.append(
                volume_info
            )

        volumes = sorted(
            volumes,
            key=lambda i: i['name']
        )

        return volumes

    def get_volume(self, volume_id=None, volume_name=None, cache_enabled=True):
        object_filter = []
        if volume_id is not None:
            object_filter.append(
                'id:%s' % (volume_id)
            )
        if volume_name is not None:
            object_filter.append(
                'name:%s' % (volume_name)
            )

        volumes = self.get_volumes(object_filter=object_filter)
        if volumes is None or len(volumes) != 1:
            return None

        return volumes[0]

    def get_volume_name(self, volume_id, cache_enabled=True):
        volume_info = self.get_volume(volume_id=volume_id, cache_enabled=cache_enabled)
        if volume_info is None:
            return None
        return volume_info['name']
