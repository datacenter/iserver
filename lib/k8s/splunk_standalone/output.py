class K8sSplunkStandaloneOutput():
    def __init__(self):
        pass

    def print_standalones(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Standalone', 'namespace_nameT'],
                ['Ready', 'readyTick'],
                ['Pod', 'podTick'],
                ['PVC', 'pvcTick'],
                ['Service', 'serviceTick'],
                ['Route', 'routeTick'],
                ['URL', 'urlT']
            ]
        )