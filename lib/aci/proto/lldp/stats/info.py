class ProtocolLldpStatsInfo():
    def __init__(self):
        pass

    def get_protocol_lldp_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_protocol_lldp_stats(self, pod_id, node_id):
        managed_object = self.get_protocol_lldp_stats_mo(pod_id, node_id)
        if managed_object is None:
            return None

        return self.get_protocol_lldp_stats_info(managed_object)
