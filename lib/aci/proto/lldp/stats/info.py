class ProtocolLldpStatsInfo():
    def __init__(self):
        pass

    def get_protocol_lldp_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        info['errors'] = False
        info['errorsTick'] = '\u2717'
        info['__Output']['errorsTick'] = 'Green'

        errors = [
            'pktDiscarded',
            'errPktRcvd',
            'unrecogTLV'
        ]
        for key in errors:
            if info[key] != '0':
                info['__Output'][key] = 'Red'
                info['errors'] = True
                info['errorsTick'] = '\u2713'
                info['__Output']['errorsTick'] = 'Red'

        return info

    def get_protocol_lldp_stats(self, pod_id, node_id):
        managed_object = self.get_protocol_lldp_stats_mo(pod_id, node_id)
        if managed_object is None or len(managed_object) == 0:
            return None

        return self.get_protocol_lldp_stats_info(managed_object)
