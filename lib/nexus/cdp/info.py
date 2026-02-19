from lib import filter_helper
from lib import ip_helper


class CdpInfo():
    def __init__(self):
        self.cdp = None

    def get_cdp_info(self, cdp_mo):
        if cdp_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in cdp_mo:
            info[key] = cdp_mo[key]

        info['mac'] = info['remote_intf_mac']

        return info

    def get_cdps_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.cdp is not None:
                return self.cdp

        managed_objects = self.get_cdp_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_cdps_info',
                'No cdp neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.cdp = []
        for managed_object in managed_objects['TABLE_cdp_neighbor_detail_info']['ROW_cdp_neighbor_detail_info']:
            cdp_info = self.get_cdp_info(
                managed_object
            )
            self.cdp.append(
                cdp_info
            )

        return self.cdp

    def match_cdp(self, cdp_info, cdp_filter):
        if cdp_filter is None or len(cdp_filter) == 0:
            return True

        for ap_rule in cdp_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True

                if cdp_info['mac'] is None:
                    return False

                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, cdp_info['mac']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_cdp',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cdps(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_cdps = self.get_cdps_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_cdps is None:
            self.log.error(
                'get_cdps',
                'Failed to get cdp neighbors: %s' % (self.nexus_name)
            )
            return None

        cdps = []

        for cdp_info in all_cdps:
            if not self.match_cdp(cdp_info, object_filter):
                continue

            cdps.append(
                cdp_info
            )

        return cdps
