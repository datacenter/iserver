class K8sHookOutput():
    def __init__(self):
        pass

    def print_hooks(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Hook', 'namespace_nameT']
            ]
        )