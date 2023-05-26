class InterfaceManagementStateInfo():
    def __init__(self, log_id=None):
        pass

    def get_interface_management_state_info(self, managed_object):
        keys = [
            'backplaneMac',
            'dn',
            'lastLinkStChg',
            'operDuplex',
            'operMtu',
            'operRouterMac',
            'operSpeed',
            'operSt',
            'operStQual',
            'vdcId'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_interface_management_state(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_management_state_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_management_state_info(managed_object)
