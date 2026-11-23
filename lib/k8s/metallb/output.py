class K8sMetalLbOutput():
    def __init__(self):
        pass

    def print_metallbs(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['MetalLb', 'namespace_nameT']
            ]
        )