class InterfaceManagementStateInfo():
    def __init__(self, log_id=None):
        self.interface_management_state = {}

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

        # "dn": "topology/pod-1/node-205/sys/mgmt-[mgmt0]/mgmt",
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = info['dn'].split('mgmt-[')[1].split(']')[0]

        return info

    def get_interfaces_management_state_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_management_state:
            return self.interface_management_state[key]

        managed_objects = self.get_interface_management_state_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.interface_management_state[key] = []
        for managed_object in managed_objects:
            self.interface_management_state[key].append(
                self.get_interface_management_state_info(
                    managed_object
                )
            )

        return self.interface_management_state[key]

    def get_interface_management_state(self, pod_id, node_id, interface_id):
        interfaces_info = self.get_interfaces_management_state_info(pod_id, node_id)
        if interfaces_info is None:
            return None

        for interface_info in interfaces_info:
            if interface_id == interface_info['interface_id']:
                return interface_info

        return None
