import json


class K8sLvmClusterOutput():
    def __init__(self):
        pass

    def print_lvm_cluster(self, info):
        order = [
            'namespace',
            'name',
            'info.state',
            'info.readyTick'        
        ]

        headers = [
            'Namespace',
            'Name',
            'State',
            'Ready'
        ]

        order.append('info.resourcesAvailableTick')
        headers.append('Resources')
        if not info['info']['resourcesAvailable']:
            order.append('info.resourcesAvailableDescription')
            headers.append('Reason')


        order.append('info.vgsReadyTick')
        headers.append('VGs')
        if not info['info']['vgsReady']:
            order.append('info.vgsReadyDescription')
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

        for device_class in info['info']['deviceClass']:
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

            self.my_output.default('')
            for node_status in device_class['nodeStatus']:
                if node_status['status'] != 'Ready' and 'reason' in node_status:
                    self.my_output.default('[%s] %s' % (
                        node_status['node'],
                        node_status['reason']
                    ))
                    
        # self.my_output.default(json.dumps(info, indent=4))