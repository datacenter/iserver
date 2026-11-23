class K8sLvmClusterOutput():
    def __init__(self):
        pass

    def print_lvm_cluster(self, info, show_device_class=True, show_node_status=True):
        order = [
            'namespace',
            'name',
            'state',
            'readyTick'        
        ]

        headers = [
            'Namespace',
            'Name',
            'State',
            'Ready'
        ]

        order.append('resourcesAvailableTick')
        headers.append('Resources')
        if not info['resourcesAvailable']:
            order.append('resourcesAvailableDescription')
            headers.append('Reason')

        order.append('vgsReadyTick')
        headers.append('VGs')
        if not info['vgsReady']:
            order.append('vgsReadyDescription')
            headers.append('Reason')

        self.my_output.dictionary(
            info,
            title='LVMCluster',
            prefix='- ',
            keys=order,
            justify=True,
            values=order,
            title_keys=headers,
            start='\n\n'
        )

        if show_device_class:
            self.print_lvm_cluster_device_class(info, show_node_status=show_node_status)
    
    def print_lvm_cluster_device_class(self, info, show_node_status=True):
        for device_class in info['deviceClass']:
            order = [
                'name',
                'fstype',
                'defaultTick',
                'nodesSummary'
            ]

            headers = [
                'Name',
                'Filesystem Type',
                'Default',
                'Nodes Ready'
            ]

            self.my_output.dictionary(
                device_class,
                title='Device Class',
                prefix='- ',
                keys=order,
                justify=True,
                values=order,
                title_keys=headers
            )

            order = [
                'node',
                'deviceDiscoveryPolicy',
                'status',
                'devices',
                'excludedDevices',
                'excludedReasons'
            ]

            headers = [
                'Node',
                'Discovery Policy',
                'Status',
                'Devices',
                'Excluded',
                'Reason'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    device_class['nodeStatus'],
                    order,
                    ['devices', 'excludedDevices', 'excludedReasons']
                ),
                order=order,
                headers=headers,
                row_separator=True,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

            if show_node_status:
                self.my_output.default('')

                for node_status in device_class['nodeStatus']:
                    if node_status['status'] != 'Ready' and 'reason' in node_status:
                        self.my_output.default('[%s] %s' % (
                            node_status['node'],
                            node_status['reason']
                        ))