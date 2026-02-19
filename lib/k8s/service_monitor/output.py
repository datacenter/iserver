class K8sServiceMonitorOutput():
    def __init__(self):
        pass

    def print_service_monitors(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Service Monitor', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Endpoint', 'endpointT'],
                ['POD', 'podT'],
                ['Target', 'targetTick']
            ]
        )

