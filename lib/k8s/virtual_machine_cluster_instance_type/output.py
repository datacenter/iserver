class K8sVirtualMachineClusterInstanceTypeOutput():
    def __init__(self):
        pass

    def print_virtual_machine_cluster_instance_types(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Virtual Machine Cluster Instance Type', 'name'],
                ['Size', 'size'],
                ['CPU', 'cpu'],
                ['Numa', 'numa'],
                ['Memory', 'memory'],
                ['Huge Pages', 'hugepages']
            ]
        )
