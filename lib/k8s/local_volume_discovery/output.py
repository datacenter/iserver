class K8sLocalVolumeDiscoveryOutput():
    def __init__(self):
        pass

    def print_local_volume_discoveries(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Local Volume Discovery', 'namespace_nameT'],
                ['Available', 'availableT'],
                ['Phase', 'phase']
            ]
        )
