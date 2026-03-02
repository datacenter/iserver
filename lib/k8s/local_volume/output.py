class K8sLocalVolumeOutput():
    def __init__(self):
        pass

    def print_local_volumes(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Local Volume', 'namespace_nameT'],
                ['Node', 'node'],
                ['Device', 'device.path'],
                ['Storage Class', 'device.sc'],
                ['Mode', 'device.mode']
            ]
        )
