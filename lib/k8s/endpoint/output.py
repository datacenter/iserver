class K8sEndpointOutput():
    def __init__(self):
        pass

    def print_endpoints(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Endpoint', 'namespace_nameT'],
                ['Headless', 'headlessTick'],
                ['Pod', 'podT'],
                ['Address', 'addressT'],
                ['Port', 'portT']
            ]
        )
