from lib import filter_helper


class InterfaceVlanStatsInfo():
    def __init__(self):
        self.vlan_stats = {}

    def get_vlan_stats_info(self, managed_object):
        keys = [
            'adminSt',
            'ctrl',
            'dn',
            'encap',
            'epgDn',
            'fabEncap',
            'fwdCtrl',
            'hwId',
            'id',
            'name',
            'operSt',
            'operStQual',
            'type'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key].strip()

        if info['adminSt'] == 'active':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        info['fvxlan'] = ''
        if 'vxlan-' in info['fabEncap']:
            info['fvxlan'] = info['fabEncap'].split('vxlan-')[1]

        info['evlan'] = ''
        if 'vlan-' in info['encap']:
            info['evlan'] = info['encap'].split('vlan-')[1]

        return info

    def get_vlans_stats_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.vlan_stats:
            return self.vlan_stats[key]

        vlan_stats_mo = self.get_vlan_stats_mo(pod_id, node_id)
        if vlan_stats_mo is None:
            return None

        self.vlan_stats[key] = []
        for managed_object in vlan_stats_mo:
            self.vlan_stats[key].append(
                self.get_vlan_stats_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'vlanCktEp.info.%s' % (key),
            self.vlan_stats[key]
        )

        return self.vlan_stats[key]

    def get_oper_vlans_list(self, oper_vlans):
        vlans = []

        for item in oper_vlans.split(','):
            if '-' in item:
                start_index = int(item.split('-')[0])
                end_index = int(item.split('-')[1])

                index = start_index
                while True:
                    vlans.append(str(index))
                    index = index + 1
                    if index > end_index:
                        break

            if '-' not in item:
                vlans.append(item)

        return vlans

    def match_vlan_stats(self, vlan_stats_info, vlan_filter):
        if vlan_filter is None or len(vlan_filter) == 0:
            return True

        for ap_rule in vlan_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'vlans':
                if not filter_helper.match_id(vlan_stats_info['id'], value):
                    return False

            if key == 'vlan':
                if not filter_helper.match_id(vlan_stats_info['id'], value):
                    return False

            if key == 'evlan':
                if not filter_helper.match_id(vlan_stats_info['evlan'], value):
                    return False

            if key == 'evlans':
                if not filter_helper.match_id(vlan_stats_info['evlan'], value):
                    return False

            if key == 'fvxlan':
                if not filter_helper.match_id(vlan_stats_info['fvxlan'], value):
                    return False

            if key == 'epg':
                if not filter_helper.match_string(value, vlan_stats_info['epgDn']):
                    return False

        return True

    def get_vlan_stats(self, pod_id, node_id, vlan_filter=None):
        all_vlan_stats = self.get_vlans_stats_info(pod_id, node_id)
        if all_vlan_stats is None:
            return None

        vlan_stats = []

        for vlan_stats_info in all_vlan_stats:
            if not self.match_vlan_stats(vlan_stats_info, vlan_filter):
                continue

            vlan_stats.append(
                vlan_stats_info
            )

        vlan_stats = sorted(
            vlan_stats,
            key=lambda i: int(i['id'])
        )

        return vlan_stats
