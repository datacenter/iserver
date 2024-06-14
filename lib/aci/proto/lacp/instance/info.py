class ProtocolLacpInstanceInfo():
    def __init__(self):
        pass

    def get_protocol_lacp_instance_info(self, managed_object):
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

        return info

    def get_protocol_lacp_instance(self, pod_id, node_id):
        managed_object = self.get_protocol_lacp_instance_mo(pod_id, node_id)
        if managed_object is None or len(managed_object) == 0:
            return None

        return self.get_protocol_lacp_instance_info(managed_object)
