class K8sNimBuildOutput():
    def __init__(self):
        pass

    def print_nim_builds(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Nim Build', 'namespace_nameT']
            ]
        )