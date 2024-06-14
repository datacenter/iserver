class NsoCnfmDeviceOutput():
    def __init__(self):
        pass

    def print_cnfm_state(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM Device - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'device.address_port',
            'device.authgroup',
            'device.device_type',
            'device.ned',
            'device.state',
            'device.syncTick',
            'cluster_count',
            'cnfi_summary'
        ]

        headers = [
            'Device Name',
            'Address',
            'AuthGroup',
            'Type',
            'NED',
            'State',
            'Sync',
            'Cluster',
            'Cnfi'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True,
            merge=True
        )

    def print_cnfm_clusters(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM Device - Cluster [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        clusters = []
        for item in info:
            for cluster_info in item['cluster']:
                new_item = {}
                new_item['cnfm'] = item['name']
                for key in cluster_info:
                    new_item[key] = cluster_info[key]

                if new_item['access'] is None:
                    new_item['access'] = '--'

                if new_item['namespace'] is None:
                    new_item['namespace'] = ['--']

                clusters.append(
                    new_item
                )

        order = [
            'cnfm',
            'name',
            'type',
            'access',
            'namespace',
            'cnfi_summary'
        ]

        headers = [
            'Device Name',
            'Cluster Name',
            'Type',
            'Namespace Access',
            'Namespace',
            'Cnfi'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                clusters,
                order,
                ['namespace']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True,
            merge=True
        )
