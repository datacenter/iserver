import copy


class InterfacePhyQosStatsLive():
    def __init__(self):
        pass

    def get_interface_phy_qos_stats_delta(self, qos_stats, qos_stats_reference):
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

        qos_delta = copy.deepcopy(qos_stats)
        qos_delta['__Output'] = {}
        for key in keys:
            if qos_stats[key] < qos_stats_reference[key]:
                self.log.error('get_interface_phy_qos_stats_delta', qos_stats['interface_id'])
                qos_delta[key] = 0
                continue

            qos_delta[key] = qos_stats[key] - qos_stats_reference[key]

        keys = [
            'RxDropBytesCount',
            'RxDropPacketsCount',
            'TxDropBytesCount',
            'TxDropPacketsCount'
        ]

        for key in keys:
            if qos_delta[key] > 0:
                qos_delta['__Output'][key] = 'Red'

        return qos_delta
