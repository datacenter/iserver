class K8sNimServiceOutput():
    def __init__(self):
        pass

    def print_nim_services(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Nim Service', 'namespace_nameT']
            ]
        )