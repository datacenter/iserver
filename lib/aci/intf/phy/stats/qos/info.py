class InterfacePhyQosStatsInfo():
    def __init__(self):
        self.interface_phy_qos_stats = {}

    def get_interface_phy_qos_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        info['id'] = managed_object['id']
        info['dn'] = managed_object['dn']
        info['interface_id'] = managed_object['dn'].split('[')[1].split(']')[0]

        keys = [
            'RxAdmitBytesCount',
            'RxAdmitPacketsCount',
            'RxDropBytesCount',
            'RxDropPacketsCount',
            'TxAdmitBytesCount',
            'TxAdmitPacketsCount',
            'TxDropBytesCount',
            'TxDropPacketsCount'
        ]

        for key in keys:
            try:
                info[key] = int(managed_object[key].strip())
            except BaseException:
                info[key] = 0

        keys = [
            'RxDropBytesCount',
            'RxDropPacketsCount',
            'TxDropBytesCount',
            'TxDropPacketsCount'
        ]

        for key in keys:
            if info[key] > 0:
                info['__Output'][key] = 'Red'

        return info

    def get_interfaces_phy_qos_stats_info(self, pod_id, node_id, cache_enabled=True):
        key = '%s.%s' % (pod_id, node_id)
        if cache_enabled:
            if key in self.interface_phy_qos_stats:
                return self.interface_phy_qos_stats[key]

        interfaces_qos_stats_mo = self.get_interface_phy_qos_stats_mo(pod_id, node_id, cache_enabled=cache_enabled)
        if interfaces_qos_stats_mo is not None:
            self.interface_phy_qos_stats[key] = []
            for interface_qos_stats_mo in interfaces_qos_stats_mo:
                self.interface_phy_qos_stats[key].append(
                    self.get_interface_phy_qos_stats_info(
                        interface_qos_stats_mo
                    )
                )

        self.log.apic_mo(
            'qosmIfClass.info.%s' % (key),
            self.interface_phy_qos_stats[key]
        )

        return self.interface_phy_qos_stats[key]

    def match_interface_phy_qos_stats(self, interface_phy_qos_stats_info, qos_stats_filter):
        if qos_stats_filter is None or len(qos_stats_filter) == 0:
            return True

        for ap_rule in qos_stats_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'interface_id':
                if value != interface_phy_qos_stats_info['interface_id']:
                    return False

            if key == 'qos':
                if value == 'data':
                    keys = [
                        'RxAdmitBytesCount',
                        'RxAdmitPacketsCount',
                        'TxAdmitBytesCount',
                        'TxAdmitPacketsCount',
                        'RxDropBytesCount',
                        'RxDropPacketsCount',
                        'TxDropBytesCount',
                        'TxDropPacketsCount'
                    ]
                    is_traffic = False
                    for key in keys:
                        if interface_phy_qos_stats_info[key] > 0:
                            is_traffic = True

                    if not is_traffic:
                        return False

                if value == 'data-rx':
                    keys = [
                        'RxAdmitBytesCount',
                        'RxAdmitPacketsCount',
                        'RxDropBytesCount',
                        'RxDropPacketsCount'
                    ]
                    is_traffic = False
                    for key in keys:
                        if interface_phy_qos_stats_info[key] > 0:
                            is_traffic = True

                    if not is_traffic:
                        return False

                if value == 'data-tx':
                    keys = [
                        'TxAdmitBytesCount',
                        'TxAdmitPacketsCount',
                        'TxDropBytesCount',
                        'TxDropPacketsCount'
                    ]
                    is_traffic = False
                    for key in keys:
                        if interface_phy_qos_stats_info[key] > 0:
                            is_traffic = True

                    if not is_traffic:
                        return False

                if value == 'drops':
                    keys = [
                        'RxDropBytesCount',
                        'RxDropPacketsCount',
                        'TxDropBytesCount',
                        'TxDropPacketsCount'
                    ]

                    is_drops = False
                    for key in keys:
                        if interface_phy_qos_stats_info[key] > 0:
                            is_drops = True

                    if not is_drops:
                        return False

                if value == 'drops-rx':
                    keys = [
                        'RxDropBytesCount',
                        'RxDropPacketsCount'
                    ]

                    is_drops = False
                    for key in keys:
                        if interface_phy_qos_stats_info[key] > 0:
                            is_drops = True

                    if not is_drops:
                        return False

                if value == 'drops-tx':
                    keys = [
                        'TxDropBytesCount',
                        'TxDropPacketsCount'
                    ]

                    is_drops = False
                    for key in keys:
                        if interface_phy_qos_stats_info[key] > 0:
                            is_drops = True

                    if not is_drops:
                        return False

        return True

    def get_interface_phy_qos_stats(self, pod_id, node_id, interface_id):
        stats = self.get_interfaces_phy_qos_stats(
            pod_id,
            node_id,
            qos_filter=['interface_id:%s' % (interface_id)]
        )

        return stats

    def get_interfaces_phy_qos_stats(self, pod_id, node_id, qos_filter=None, qos_references=None):
        cache_enabled = True
        if qos_references is not None:
            cache_enabled = False

        all_interfaces_phy_qos_stats = self.get_interfaces_phy_qos_stats_info(pod_id, node_id, cache_enabled=cache_enabled)
        if all_interfaces_phy_qos_stats is None:
            return None

        stats = []
        for interface_phy_qos_stats in all_interfaces_phy_qos_stats:
            if qos_references is not None:
                for qos_reference in qos_references:
                    if qos_reference['id'] == interface_phy_qos_stats['interface_id']:
                        for interface_phy_qos_reference_class in qos_reference['qos']:
                            if interface_phy_qos_reference_class['id'] == interface_phy_qos_stats['id']:
                                interface_phy_qos_stats = self.get_interface_phy_qos_stats_delta(
                                    interface_phy_qos_stats,
                                    interface_phy_qos_reference_class
                                )

            if not self.match_interface_phy_qos_stats(interface_phy_qos_stats, qos_filter):
                continue

            stats.append(
                interface_phy_qos_stats
            )

        stats = sorted(
            stats,
            key=lambda i: (i['interface_id'], i['id'].lower())
        )

        return stats
