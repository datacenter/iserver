from lib import ip_helper


class VrfInfo():
    def __init__(self):
        self.vrf = None

    def get_vrf_info(self, vrf_mo):
        if vrf_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        keys = [
            'vrf_id',
            'vrf_name',
            'vrf_state',
            'vpnid',
            'rd',
            'vni',
            'mac_routes',
            'mid_threshold'
        ]
        for key in keys:
            info[key] = None
            if key in vrf_mo:
                info[key] = vrf_mo[key]

        keys = [
            'tib_id',
            'tib_af',
            'tib_nonce',
            'tib_state'
        ]
        info['table'] = []
        if 'TABLE_tib' in vrf_mo:
            if 'ROW_tib' in vrf_mo['TABLE_tib']:
                if isinstance(vrf_mo['TABLE_tib']['ROW_tib'], dict):
                    item = {}
                    for key in keys:
                        item[key] = None
                        if key in vrf_mo['TABLE_tib']['ROW_tib']:
                            item[key.split('_')[1]] = vrf_mo['TABLE_tib']['ROW_tib'][key]
                    info['table'].append(
                        item
                    )
                if isinstance(vrf_mo['TABLE_tib']['ROW_tib'], list):
                    for item_mo in vrf_mo['TABLE_tib']['ROW_tib']:
                        item = {}
                        for key in keys:
                            item[key] = None
                            if key in item_mo:
                                item[key.split('_')[1]] = item_mo[key]
                        info['table'].append(
                            item
                        )

        return info

    def get_vrfs_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.vrf is not None:
                return self.vrf

        managed_objects = self.get_vrf_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_vrfs_info',
                'No vrf neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.vrf = []
        for managed_object in managed_objects['TABLE_vrf']['ROW_vrf']:
            vrf_info = self.get_vrf_info(
                managed_object
            )
            self.vrf.append(
                vrf_info
            )

        return self.vrf

    def match_vrf(self, vrf_info, vrf_filter):
        if vrf_filter is None or len(vrf_filter) == 0:
            return True

        for ap_rule in vrf_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True

                if vrf_info['mac'] is None:
                    return False

                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, vrf_info['mac']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_vrf',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_vrfs(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_vrfs = self.get_vrfs_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_vrfs is None:
            self.log.error(
                'get_vrfs',
                'Failed to get vrf neighbors: %s' % (self.nexus_name)
            )
            return None

        vrfs = []

        for vrf_info in all_vrfs:
            if not self.match_vrf(vrf_info, object_filter):
                continue

            vrfs.append(
                vrf_info
            )

        return vrfs
