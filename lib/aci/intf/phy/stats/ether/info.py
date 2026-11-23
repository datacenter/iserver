from lib import filter_helper


class InterfacePhyEtherStatsInfo():
    def __init__(self):
        self.interface_phy_ether_stats = {}

    def get_interface_phy_ether_stats_info(self, managed_object):
        keys = [
            'accessVlan',
            'allowedVlans',
            'backplaneMac',
            'bundleIndex',
            'cfgAccessVlan',
            'cfgNativeVlan',
            'dn',
            'encap',
            'intfT',
            'lastLinkStChg',
            'media',
            'nativeVlan',
            'operDuplex',
            'operErrDisQual',
            'operFecMode',
            'operFlowCtrl',
            'operMdix',
            'operMode',
            'operModeDetail',
            'operPhyEnSt',
            'operRouterMac',
            'operSpeed',
            'operSt',
            'operStQual',
            'operVlans',
            'osSum',
            'resetCtr',
            'primaryVlan',
            'txT'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['__Output']['bundleIndex'] = 'Yellow'
        if info['operStQual'] == 'none':
            info['operStQual'] = 'connected'

        if info['bundleIndex'] == 'unspecified':
            info['bundleIndex'] = ''

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_interfaces_phy_ether_stats_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_phy_ether_stats:
            return self.interface_phy_ether_stats[key]

        interfaces_stats_mo = self.get_interface_phy_ether_stats_mo(pod_id, node_id)
        if interfaces_stats_mo is not None:
            self.interface_phy_ether_stats[key] = []
            for interface_stats_mo in interfaces_stats_mo:
                self.interface_phy_ether_stats[key].append(
                    self.get_interface_phy_ether_stats_info(
                        interface_stats_mo
                    )
                )

        self.log.apic_mo(
            'ethpmPhysIf.info.%s' % (key),
            self.interface_phy_ether_stats[key]
        )

        return self.interface_phy_ether_stats[key]

    def match_interface_phy_ether_stats(self, interface_phy_ether_stats_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'dn':
                if not filter_helper.match_string('%s/*' % (value), interface_phy_ether_stats_info['dn']):
                    return False

        return True

    def get_interface_phy_ether_stats(self, pod_id, node_id, interface_filter=None):
        all_interfaces_phy_ether_stats = self.get_interfaces_phy_ether_stats_info(pod_id, node_id)
        if all_interfaces_phy_ether_stats is None:
            return None

        interfaces = []

        for interface_phy_ether_stats_info in all_interfaces_phy_ether_stats:
            if not self.match_interface_phy_ether_stats(interface_phy_ether_stats_info, interface_filter):
                continue

            interfaces.append(
                interface_phy_ether_stats_info
            )

        return interfaces
