class K8sClusterPolicyOutput():
    def __init__(self):
        pass

    def print_cluster_policies(self, info):
        if len(info) == 0:
            return

        for item in info:
            self.print_cluster_policy(item)

    def print_cluster_policy(self, info):
        order = [
            'namespace',
            'name',
            'state',
            'ds_summary',
            'dcgmEnabledTick',
            'dcgmExporterEnabledTick',
            'dcgmServiceMonitorEnabledTick',
            'devicePluginEnabledTick',
            'driverEnabledTick',
            'gdrcopyEnabledTick',
            'gdsEnabledTick',
            'gfdEnabledTick',
            'migStrategy',
            'migManagerEnabledTick',
            'nodeStatusExporterEnabledTick',
            'sandboxDevicePluginEnabledTick',
            'toolkitEnabledTick',
            'vfioManagerEnabledTick',
            'vgpuDeviceManagerEnabledTick',
            'vgpuManagerEnabledTick'
        ]

        headers = [
            'Namespace',
            'Name',
            'State',
            'Daemon Sets',
            'DCGM',
            'DCGM Exporter',
            'DCGM Service Monitor',
            'Device Plugin',
            'Driver',
            'GDR Copy',
            'GDS',
            'GFD',
            'Mig Strategy',
            'Mig Manager',
            'Node Status Exporter',
            'Sandbox Device Plugin',
            'Toolkit',
            'VFID Manager',
            'vGPU Device Manager',
            'vGPU Manager'
        ]

        self.my_output.dictionary(
            info,
            title='NVIDIA Cluster Policy',
            prefix='- ',
            keys=order,
            justify=True,
            values=order,
            title_keys=headers,
            start='\n\n'
        )
