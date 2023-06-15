class ProtocolLldpStatsInfo():
    def __init__(self):
        pass

    def get_protocol_lldp_stats_info(self, managed_object):
        # "childAction": "",
        # "dn": "topology/pod-1/node-205/sys/lldp/inst/inststats",
        # "entriesAged": "0",
        # "errPktRcvd": "0",
        # "lastAdjChgTs": "2023-06-12T16:52:47.652+02:00",
        # "modTs": "never",
        # "numAdjAdded": "16",
        # "numAdjRemoved": "0",
        # "pktDiscarded": "0",
        # "pktRcvd": "109173",
        # "pktSent": "109091",
        # "status": "",
        # "unrecogTLV": "0"

        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # "dn": "topology/pod-1/node-205/sys/lldp/inst/inststats"
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
