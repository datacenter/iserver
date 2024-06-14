from lib import filter_helper
from lib import ip_helper


class MacInfo():
    def __init__(self):
        self.mac = None

    def get_mac_info(self, mac_mo):
        if mac_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        # "disp_mac_addr": "0008.312b.d2a8",
        # "disp_type": "dynamic",
        # "disp_vlan": "3",
        # "disp_age": "0",
        # "disp_is_secure": "F",
        # "disp_is_ntfy": "F",
        # "disp_port": "Po3"
        for key in mac_mo:
            if key.startswith('disp_'):
                info[key[5:]] = mac_mo[key]
            else:
                info[key] = mac_mo[key]

        return info

    def get_macs_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.mac is not None:
                return self.mac

        managed_objects = self.get_mac_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_macs_info',
                'No mac neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.mac = []
        for managed_object in managed_objects['TABLE_mac_address']['ROW_mac_address']:
            mac_info = self.get_mac_info(
                managed_object
            )
            self.mac.append(
                mac_info
            )

        return self.mac

    def match_mac(self, mac_info, mac_filter):
        if mac_filter is None or len(mac_filter) == 0:
            return True

        for ap_rule in mac_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'vlan':
                key_found = True
                if not filter_helper.match_string(value, mac_info['vlan']):
                    return False

            if key == 'mac':
                key_found = True
                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, mac_info['mac_addr']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_mac',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_macs(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_macs = self.get_macs_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_macs is None:
            self.log.error(
                'get_macs',
                'Failed to get mac neighbors: %s' % (self.nexus_name)
            )
            return None

        macs = []

        for mac_info in all_macs:
            if not self.match_mac(mac_info, object_filter):
                continue

            macs.append(
                mac_info
            )

        return macs
