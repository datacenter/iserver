class ProtocolNdInstanceInfo():
    def __init__(self):
        pass

    def get_protocol_nd_instance_info(self, pod_id, node_id):
        managed_object = self.get_protocol_nd_instance_mo(pod_id, node_id)

        if managed_object is None:
            return None

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

        if info['adminSt'] == 'enabled':
            info['enable'] = True
            info['__Output']['adminSt'] = 'Green'
        else:
            info['enable'] = False
            info['__Output']['adminSt'] = 'Red'

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info
