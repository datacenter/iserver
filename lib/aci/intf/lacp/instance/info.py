class InterfaceLacpInstanceInfo():
    def __init__(self):
        pass

    def get_lacp_instance_info(self, managed_object):
        keys = [
            'adminPrio',
            'adminSt',
            'dn',
            'operPrio',
            'sysMac'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_lacp_instance(self, pod_id, node_id):
        managed_object = self.get_lacp_instance_mo(pod_id, node_id)
        if managed_object is None:
            return None

        return self.get_lacp_instance_info(managed_object)
