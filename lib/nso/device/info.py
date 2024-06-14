from lib import filter_helper


class NsoDeviceInfo():
    def __init__(self):
        self.nso_device_base = None
        self.nso_device_sync = {}

    def get_device_base_info(self, nso_device_mo):
        if nso_device_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = self.get(
            nso_device_mo,
            'name'
        )

        info['address'] = self.get(
            nso_device_mo,
            'address'
        )

        info['port'] = self.get(
            nso_device_mo,
            'port'
        )

        info['address_port'] = '%s:%s' % (
            info['address'],
            info['port']
        )

        info['authgroup'] = self.get(
            nso_device_mo,
            'authgroup'
        )

        device_type = info['ned-id'] = self.get(
            nso_device_mo,
            'device-type'
        )
        info['ned_type'] = None
        info['ned_id'] = None
        if 'cli' in device_type:
            info['ned_type'] = 'cli'
            info['ned_id'] = self.get(
                nso_device_mo,
                'device-type:cli:ned-id'
            )

        if 'generic' in device_type:
            info['ned_type'] = 'generic'
            info['ned_id'] = self.get(
                nso_device_mo,
                'device-type:generic:ned-id'
            )
        if 'netconf' in device_type:
            info['ned_type'] = 'netconf'
            info['ned_id'] = self.get(
                nso_device_mo,
                'device-type:netconf:ned-id'
            )

        if info['ned_id'] is not None:
            if len(info['ned_id'].split(':')) == 2:
                if info['ned_id'].split(':')[0] == info['ned_id'].split(':')[1]:
                    info['ned_id'] = info['ned_id'].split(':')[0]

        info['ned'] = None
        if info['ned_type'] is not None and info['ned_id'] is not None:
            info['ned'] = '%s:%s' % (
                info['ned_type'],
                info['ned_id']
            )

        info['device_type'] = None
        if info['ned_id'].startswith('cisco-apicdc'):
            info['device_type'] = 'APIC'

        if info['ned_id'].startswith('cisco-iosxr'):
            info['device_type'] = 'IOS-XR'

        if info['ned_id'].startswith('cisco-ios-'):
            info['device_type'] = 'IOS-XE'

        if info['ned_id'].startswith('cnfm-nc-'):
            info['device_type'] = 'CNFM'

        if info['ned_id'].startswith('openstack-'):
            info['device_type'] = 'OpenStack'

        if info['ned_id'].startswith('etsi-sol003-'):
            info['device_type'] = 'VNFM ETSI'

        if info['ned_id'].startswith('tailf-ned-esc-'):
            info['device_type'] = 'VNFM ESC'

        if info['ned_id'].startswith('juniper-junos'):
            info['device_type'] = 'Junos'

        info['state'] = self.get(
            nso_device_mo,
            'state:admin-state'
        )

        if info['state'] == 'unlocked':
            info['__Output']['state'] = 'Green'
        else:
            info['__Output']['state'] = 'Red'

        return info

    def get_devices_base_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nso_device_base is not None:
                return self.nso_device_base

        managed_objects = self.get_device_base_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nso_device_base = []
        for managed_object in managed_objects:
            nso_device_base_info = self.get_device_base_info(
                managed_object
            )
            self.nso_device_base.append(
                nso_device_base_info
            )

        return self.nso_device_base

    def match_device(self, device_base_info, device_base_filter):
        if device_base_filter is None or len(device_base_filter) == 0:
            return True

        for ap_rule in device_base_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, device_base_info['name']):
                    return False

            if key == 'type':
                key_found = True
                if not filter_helper.match_string(value, device_base_info['device_type']):
                    return False

            if not key_found:
                self.log.error(
                    'match_device_base',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_devices(self, object_filter=None, sync_info=False, cache_enabled=True):
        all_devices = self.get_devices_base_info(cache_enabled=cache_enabled)
        if all_devices is None:
            return None

        devices = []

        for device_info in all_devices:
            if not self.match_device(device_info, object_filter):
                continue

            if sync_info:
                device_info['sync'] = self.get_device_sync(device_info['name'])
                if device_info['sync']:
                    device_info['syncTick'] = '\u2713'
                    device_info['__Output']['syncTick'] = 'Green'
                else:
                    device_info['syncTick'] = '\u2717'
                    device_info['__Output']['syncTick'] = 'Red'

            devices.append(
                device_info
            )

        return devices

    def get_device_sync(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.nso_device_sync:
                return self.nso_device_sync[device_name]

        sync_mo = self.get_device_sync_mo(
            device_name,
            cache_enabled=cache_enabled
        )

        if sync_mo is None:
            return False

        in_sync = False
        for line in sync_mo.split('\n'):
            if '>in-sync<' in line:
                in_sync = True

        return in_sync

    def get_device(self, device_name, sync_info=False, cache_enabled=True):
        devices_info = self.get_devices(
            object_filter=['name:%s' % (device_name)],
            sync_info=sync_info,
            cache_enabled=cache_enabled
        )
        if devices_info is None or len(devices_info) != 1:
            return None
        return devices_info[0]
