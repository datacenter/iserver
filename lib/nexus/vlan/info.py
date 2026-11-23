class VlanInfo():
    def __init__(self):
        self.vlan = None

    def get_vlan_info(self, vlan_mo, mtu_mo):
        if vlan_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        info['id'] = vlan_mo['vlanshowbr-vlanid']
        info['name'] = vlan_mo['vlanshowbr-vlanname']
        info['state'] = vlan_mo['vlanshowbr-vlanstate']
        info['interfaces'] = []
        if 'vlanshowplist-ifidx' in vlan_mo:
            info['interfaces'] = vlan_mo['vlanshowplist-ifidx'].split(',')
        info['type'] = None
        info['mode'] = None
        if mtu_mo is not None:
            info['type'] = mtu_mo['vlanshowinfo-media-type']
            info['mode'] = mtu_mo['vlanshowinfo-vlanmode']

        return info

    def get_vlans_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.vlan is not None:
                return self.vlan

        managed_objects = self.get_vlan_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_vlans_info',
                'No vlan neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.vlan = []
        for vlan_managed_object in managed_objects['TABLE_vlanbrief']['ROW_vlanbrief']:
            mtu_managed_object = None
            for item in managed_objects['TABLE_mtuinfo']['ROW_mtuinfo']:
                if vlan_managed_object['vlanshowbr-vlanid'] == item['vlanshowinfo-vlanid']:
                    mtu_managed_object = item

            self.vlan.append(
                self.get_vlan_info(
                    vlan_managed_object,
                    mtu_managed_object
                )
            )

        return self.vlan

    def match_vlan(self, vlan_info, vlan_filter):
        if vlan_filter is None or len(vlan_filter) == 0:
            return True

        for ap_rule in vlan_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_vlan',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_vlans(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_vlans = self.get_vlans_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_vlans is None:
            self.log.error(
                'get_vlans',
                'Failed to get vlan neighbors: %s' % (self.nexus_name)
            )
            return None

        vlans = []

        for vlan_info in all_vlans:
            if not self.match_vlan(vlan_info, object_filter):
                continue

            vlans.append(
                vlan_info
            )

        return vlans
