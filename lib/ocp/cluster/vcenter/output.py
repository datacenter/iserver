class OcpClusterVcenterOutput():
    def __init__(self):
        pass

    def print_ocp_clusters_vcenter(self, clusters):
        order = [
            'name',
            'vcenter.name',
            'vms.stateFlag',
            'vms.name',
            'vms.host',
            'vms.cpu.info',
            'vms.cpuUsageUnit',
            'vms.memoryUnit',
            'vms.guestMemoryUsagePct',
            'vms.numEthernetCards',
            'vms.provisionedStorageUnit',
            'vms.usedStoragePct'
        ]

        headers = [
            'Name',
            'vCenter',
            'SF',
            'VM Name',
            'Host',
            'CPU',
            'Usage',
            'Memory',
            '[%]',
            'NIC',
            'Storage',
            '[%]'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                clusters,
                order,
                ['vms']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_ocp_cluster_vcenter(self, info):
        order = [
            'stateFlag',
            'name',
            'host',
            'cpu.info',
            'cpuUsageUnit',
            'memoryUnit',
            'guestMemoryUsagePct',
            'numEthernetCards',
            'provisionedStorageUnit',
            'usedStoragePct'
        ]

        headers = [
            'SF',
            'VM Name',
            'Host',
            'CPU',
            'Usage',
            'Memory',
            '[%]',
            'NIC',
            'Storage',
            '[%]'
        ]

        self.my_output.my_table(
            info['vms'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
