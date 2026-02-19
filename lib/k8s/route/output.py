class K8sRouteOutput():
    def __init__(self):
        pass

    def print_routes(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Route', 'namespace_nameT'],
                ['Ready', 'readyTick'],
                ['Route', 'route'],
                ['Service', 'service']
            ]
        )
        