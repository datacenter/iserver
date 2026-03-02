class K8sLocalVolumeSetOutput():
    def __init__(self):
        pass

    def print_local_volume_sets(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Local Volume Set', 'namespace_nameT'],
                ['Storage Class', 'storage_class'],
                ['Volume Mode', 'volume_mode'],
                ['Available', 'availableT'],
                ['Disk Maker', 'dm_availableT'],
                ['# Devices', 'device_count']
            ]
        )
