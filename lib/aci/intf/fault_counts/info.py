class InterfaceFaultCountsInfo():
    def __init__(self):
        pass

    def get_interface_fault_counts_info(self, managed_object):
        keys = [
            'crit',
            'critAcked',
            'critAckedandDelegated',
            'critDelegated',
            'maj',
            'majAcked',
            'majAckedandDelegated',
            'majDelegated',
            'minor',
            'minorAcked',
            'minorAckedandDelegated',
            'minorDelegated',
            'warn',
            'warnAckedandDelegated',
            'warnDelegated'
        ]

        info = {}
        for key in keys:
            info[key] = managed_object[key]

        return info

    def get_interface_fault_counts(self, pod_id, node_id, interface_type, interface_id):
        managed_object = self.get_interface_fault_counts_mo(pod_id, node_id, interface_type, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_fault_counts_info(managed_object)
