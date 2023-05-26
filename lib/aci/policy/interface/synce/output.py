class PolicyInterfaceSyncEOutput():
    def __init__(self):
        pass

    def print_policy_interface_synce(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'adminSt',
            'selinput',
            'srcpriority',
            'ssm',
            'wtr',
            'qlrcvlval',
            'qlrcvexactval',
            'qlrcvhval',
            'qltxlval',
            'qltxexactval',
            'qltxhval'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Input Selection',
            'Source Priority',
            'Sync Status Msg',
            'Wait-To-Restore',
            'Rx Qual Min',
            'Rx Qual Eq',
            'Rx Qual Max',
            'Tx Qual Min',
            'Tx Qual Eq',
            'Tx Qual Max'
        ]

        self.print_policy_interface(
            info,
            'SyncE Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_synce(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'selinput',
            'srcpriority',
            'ssm',
            'wtr',
            'qlrcv',
            'qltx'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Input Selection',
            'Source Priority',
            'Sync Status Msg',
            'Wait-To-Restore',
            'Rx Qual',
            'Tx Qual'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose,
            expand_lists=['qlrcv', 'qltx']
        )

    def print_policy_interface_synce_node(self, info):
        for item in info:
            if 'qlrcv' in item['policy']:
                item['qlrcv'] = item['policy']['qlrcv']
                item['qltx'] = item['policy']['qltx']
            else:
                item['qlrcv'] = []
                item['qltx'] = []

        order = [
            'policy.name',
            'policy.adminSt',
            'policy.selinput',
            'policy.srcpriority',
            'policy.ssm',
            'policy.wtr',
            'qlrcv',
            'qltx'
        ]

        headers = [
            'SyncE Policy Name',
            'Admin State',
            'Input Selection',
            'Source Priority',
            'Sync Status Msg',
            'Wait-To-Restore',
            'Rx Qual',
            'Tx Qual'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers,
            expand_lists=['qlrcv', 'qltx']
        )
