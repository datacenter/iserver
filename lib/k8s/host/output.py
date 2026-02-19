class K8sHostOutput():
    def __init__(self):
        pass

    def print_hosts(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Host', 'namespace_nameT']
            ]
        )