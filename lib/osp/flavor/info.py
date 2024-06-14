from lib import filter_helper


class OspFlavorInfo():
    def __init__(self):
        self.flavor = None
        self.flavor_keys = None

    def get_flavors_properties(self, managed_objects):
        properties = []
        for managed_object in managed_objects:
            properties.append(
                managed_object.to_dict()
            )
        return properties

    def get_flavor_info(self, flavor_mo):
        if flavor_mo is None:
            return None

        properties = flavor_mo.to_dict()

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'vcpus',
            'ram',
            'disk',
            'rxtx_factor'
        ]
        for key in keys:
            info[key] = properties[key]

        info['resource'] = 'C:%s M:%s D:%s' % (
            info['vcpus'],
            info['ram'],
            info['disk']
        )

        info['public'] = properties['os-flavor-access:is_public']
        if info['public']:
            info['publicTick'] = '\u2713'
            info['__Output']['publicTick'] = 'Green'
        else:
            info['publicTick'] = '\u2717'
            info['__Output']['publicTick'] = 'Red'

        info['enabled'] = not properties['OS-FLV-DISABLED:disabled']
        if info['enabled']:
            info['enabledTick'] = '\u2713'
            info['__Output']['enabledTick'] = 'Green'
        else:
            info['enabledTick'] = '\u2717'
            info['__Output']['enabledTick'] = 'Red'

        info['ephemeral'] = properties['OS-FLV-EXT-DATA:ephemeral']
        return info

    def get_flavors_info(self, cache_enabled=True):
        if cache_enabled:
            if self.flavor is not None:
                return self.flavor

        managed_objects = self.get_flavor_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'flavors',
            self.get_flavors_properties(managed_objects)
        )

        self.flavor = []
        for managed_object in managed_objects:
            flavor_info = self.get_flavor_info(
                managed_object
            )
            self.flavor.append(
                flavor_info
            )

        self.log.osp_mo(
            'flavors.info',
            self.flavor
        )

        return self.flavor

    def get_flavor_keys_info(self, flavor_keys_mo):
        info = {}
        for key in flavor_keys_mo:
            info[key] = flavor_keys_mo[key]
        return info

    def get_flavors_keys_info(self, cache_enabled=True):
        if cache_enabled:
            if self.flavor_keys is not None:
                return self.flavor_keys

        flavor_keys_mo = self.get_flavor_keys_mo(cache_enabled=cache_enabled)
        if flavor_keys_mo is None:
            return None

        self.flavor_keys = {}
        for flavor_id in flavor_keys_mo:
            self.flavor_keys[flavor_id] = self.get_flavor_keys_info(flavor_keys_mo[flavor_id])

        self.log.osp_mo(
            'flavors_keys.info',
            self.flavor_keys
        )

        return self.flavor_keys

    def get_flavor_keys(self, flavor_id, cache_enabled=True):
        flavors_keys = self.get_flavors_keys_info(cache_enabled=cache_enabled)
        if flavors_keys is None:
            return None

        if flavor_id not in flavors_keys:
            return None

        return flavors_keys[flavor_id]

    def match_flavor(self, flavor_info, flavor_filter):
        if flavor_filter is None or len(flavor_filter) == 0:
            return True

        key_filter = None
        value_filter = None
        for ap_rule in flavor_filter:
            key = ap_rule.split(':')[0]
            if key == 'key':
                key_filter = ':'.join(ap_rule.split(':')[1:])
            if key == 'value':
                value_filter = ':'.join(ap_rule.split(':')[1:])

        for ap_rule in flavor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, flavor_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, flavor_info['name']):
                    return False

            if key == 'vm':
                key_found = True
                if 'vm' in flavor_info:
                    found = False
                    for vm_info in flavor_info['vm']:
                        if filter_helper.match_tenant_name(value, vm_info['tenant_name']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'value':
                key_found = True
                if key_filter is None and 'keys' in flavor_info:
                    found = False
                    for key in flavor_info['keys']:
                        if filter_helper.match_string(value, flavor_info['keys'][key]):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'key':
                key_found = True
                if 'keys' in flavor_info:
                    found = False
                    for key in flavor_info['keys']:
                        if filter_helper.match_string(value, key):
                            if value_filter is None:
                                found = True
                                break

                            if value_filter is not None:
                                if filter_helper.match_string(value_filter, flavor_info['keys'][key]):
                                    found = True
                                    break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_flavor',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_flavors(self, object_filter=None, keys_info=False, vm_info=False, cache_enabled=True):
        all_flavors = self.get_flavors_info(cache_enabled=cache_enabled)
        if all_flavors is None:
            return None

        flavors = []

        for flavor_info in all_flavors:
            if not self.match_flavor(flavor_info, object_filter):
                continue

            if keys_info:
                flavor_info['keys'] = self.get_flavor_keys(flavor_info['id'], cache_enabled=cache_enabled)
                if not self.match_flavor(flavor_info, object_filter):
                    continue

            if vm_info:
                flavor_info['vm'] = []
                flavor_vms = self.get_virtual_machines(
                    object_filter=[
                        'flavor_id:%s' % (flavor_info['id'])
                    ],
                    tenant_info=True
                )
                if flavor_vms is None:
                    self.log.error(
                        'get_flavors',
                        'Get vm with flavors failed: %s' % (flavor_info['id'])
                    )
                else:
                    for flavor_vm in flavor_vms:
                        flavor_vm_info = {}
                        flavor_vm_info['tenant'] = flavor_vm['tenant_name']
                        flavor_vm_info['name'] = flavor_vm['name']
                        flavor_vm_info['tenant_name'] = '%s/%s' % (
                            flavor_vm['tenant_name'],
                            flavor_vm['name']
                        )
                        flavor_info['vm'].append(
                            flavor_vm_info
                        )

                if not self.match_flavor(flavor_info, object_filter):
                    continue

            flavors.append(
                flavor_info
            )

        flavors = sorted(
            flavors,
            key=lambda i: i['name'].lower()
        )

        return flavors

    def get_flavor(self, flavor_id=None, flavor_name=None, keys_info=False, vm_info=False, cache_enabled=True):
        object_filter = []
        if flavor_id is not None:
            object_filter.append(
                'id:%s' % (flavor_id)
            )
        if flavor_name is not None:
            object_filter.append(
                'name:%s' % (flavor_name)
            )

        flavors = self.get_flavors(
            object_filter=object_filter,
            keys_info=keys_info,
            vm_info=vm_info,
            cache_enabled=cache_enabled
        )
        if flavors is None or len(flavors) != 1:
            return None

        return flavors[0]

    def is_flavor(self, flavor_id=None, flavor_name=None, cache_enabled=True):
        if self.get_flavor(flavor_id=flavor_id, flavor_name=flavor_name) is None:
            return False
        return True
