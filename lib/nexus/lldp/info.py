from lib import filter_helper
from lib import ip_helper


class LldpInfo():
    def __init__(self):
        self.lldp = None

    def get_lldp_info(self, lldp_mo):
        if lldp_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in lldp_mo:
            info[key] = lldp_mo[key]

        if isinstance(info['system_capability'], dict):
            info['system_capability'] = None

        return info

    def get_lldps_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.lldp is not None:
                return self.lldp

        managed_objects = self.get_lldp_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_lldps_info',
                'No lldp neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.lldp = []
        for managed_object in managed_objects['TABLE_nbor']['ROW_nbor']:
            lldp_info = self.get_lldp_info(
                managed_object
            )
            self.lldp.append(
                lldp_info
            )

        return self.lldp

    def match_lldp(self, lldp_info, lldp_filter):
        if lldp_filter is None or len(lldp_filter) == 0:
            return True

        for ap_rule in lldp_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, lldp_info['chassis_id']):
                    return False

            if key == 'mac':
                key_found = True

                if lldp_info['port_type'] != 'Mac Address':
                    return False

                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, lldp_info['port_id']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_lldp',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_lldps(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_lldps = self.get_lldps_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_lldps is None:
            self.log.error(
                'get_lldps',
                'Failed to get lldp neighbors: %s' % (self.nexus_name)
            )
            return None

        lldps = []

        for lldp_info in all_lldps:
            if not self.match_lldp(lldp_info, object_filter):
                continue

            lldps.append(
                lldp_info
            )

        return lldps
