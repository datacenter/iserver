from lib import filter_helper
from lib import ip_helper


class LacpInfo():
    def __init__(self):
        self.lacp = None

    def get_lacp_info(self, lacp_mo):
        if lacp_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name
        info['interface'] = lacp_mo['interface']
        info['port'] = []

        if isinstance(lacp_mo['TABLE_member']['ROW_member'], dict):
            port_info = {}
            for key in lacp_mo['TABLE_member']['ROW_member']:
                port_info[key.replace('-', '_')] = lacp_mo['TABLE_member']['ROW_member'][key]
            info['port'].append(
                port_info
            )

        if isinstance(lacp_mo['TABLE_member']['ROW_member'], list):
            for port_mo in lacp_mo['TABLE_member']['ROW_member']:
                port_info = {}
                for key in port_mo:
                    port_info[key.replace('-', '_')] = port_mo[key]
                info['port'].append(
                    port_info
                )

        for port_info in info['port']:
            port_info['partner_mac'] = None
            if len(port_info['partner_system_id'].split(',')) == 2:
                if len(port_info['partner_system_id'].split(',')[1].split('-')) == 6:
                    mac_address = []
                    for item in port_info['partner_system_id'].split(',')[1].split('-'):
                        if len(item) == 2:
                            mac_address.append(
                                item
                            )
                        else:
                            mac_address.append(
                                '0%s' % (item)
                            )

                    port_info['partner_mac'] = ':'.join(mac_address)

        return info

    def get_lacps_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.lacp is not None:
                return self.lacp

        managed_objects = self.get_lacp_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_lacps_info',
                'No lacp neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.lacp = []
        for managed_object in managed_objects['TABLE_interface']['ROW_interface']:
            lacp_info = self.get_lacp_info(
                managed_object
            )
            self.lacp.append(
                lacp_info
            )

        return self.lacp

    def match_lacp(self, lacp_info, lacp_filter):
        if lacp_filter is None or len(lacp_filter) == 0:
            return True

        for ap_rule in lacp_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True
                found = False
                for mac_address in value.split(','):
                    for port_info in lacp_info['port']:
                        if port_info['partner_mac'] is not None:
                            if ip_helper.is_mac_match(mac_address, port_info['partner_mac']):
                                found = True

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_lacp',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_lacps(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_lacps = self.get_lacps_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_lacps is None:
            self.log.error(
                'get_lacps',
                'Failed to get lacp neighbors: %s' % (self.nexus_name)
            )
            return None

        lacps = []

        for lacp_info in all_lacps:
            if not self.match_lacp(lacp_info, object_filter):
                continue

            lacps.append(
                lacp_info
            )

        return lacps

    def get_macs_lacp(self, mac_address):
        object_filter = []
        object_filter.append(
            'mac:%s' % (','.join(mac_address))
        )

        lacps = []
        device_interfaces = self.get_lacps(
            object_filter=object_filter
        )
        if device_interfaces is not None:
            lacps = lacps + device_interfaces

        return lacps
