class K8sNetworkMapOutput():
    def __init__(self):
        pass

    def print_network_maps(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Network Map', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Source', 'source_provider'],
                ['Network', 'map.source'],
                ['Destination', 'destination_provider'],
                ['Network', 'map.destination'],
                ['Status', 'status'],
                ['Plan', 'plan']
            ]
        )