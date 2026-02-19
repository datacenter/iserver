class K8sProviderOutput():
    def __init__(self):
        pass

    def print_providers(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Provider', 'name'],
                ['Type', 'provider_type'],
                ['Status', 'phase'],
                ['Endpoint', 'endpoint'],
                ['Network Map', 'network_map_summary'],
                ['Storage Map', 'storage_map_summary'],
                ['Plan', 'plan_summary']
            ]
        )