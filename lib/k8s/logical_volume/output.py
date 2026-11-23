class K8sLogicalVolumeOutput():
    def __init__(self):
        pass

    def print_logical_volumes_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Logical Volume', 'name'],
                ['Node', 'node_name'],
                ['Device Class', 'device_class'],
                ['Req Size', 'requested_size'],
                ['Curr Size', 'current_size'],
                ['Volume', 'volume_id']
            ]
        )