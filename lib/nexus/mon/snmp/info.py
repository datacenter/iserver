from lib import filter_helper
from lib import ip_helper


class MonSnmpInfo():
    def __init__(self):
        self.snmp = None

    def get_snmp_info(self, snmp_mo):
        if snmp_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in snmp_mo:
            info[key] = snmp_mo[key]

        info['mac'] = info['remote_intf_mac']

        return info

    def get_snmps_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.snmp is not None:
                return self.snmp

        managed_objects = self.get_snmp_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_snmps_info',
                'No snmp neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.snmp = []
        for managed_object in managed_objects['TABLE_snmp_neighbor_detail_info']['ROW_snmp_neighbor_detail_info']:
            snmp_info = self.get_snmp_info(
                managed_object
            )
            self.snmp.append(
                snmp_info
            )

        return self.snmp

    def match_snmp(self, snmp_info, snmp_filter):
        if snmp_filter is None or len(snmp_filter) == 0:
            return True

        for ap_rule in snmp_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True

                if snmp_info['mac'] is None:
                    return False

                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, snmp_info['mac']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_snmp',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_snmps(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_snmps = self.get_snmps_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_snmps is None:
            self.log.error(
                'get_snmps',
                'Failed to get snmp neighbors: %s' % (self.nexus_name)
            )
            return None

        snmps = []

        for snmp_info in all_snmps:
            if not self.match_snmp(snmp_info, object_filter):
                continue

            snmps.append(
                snmp_info
            )

        return snmps
