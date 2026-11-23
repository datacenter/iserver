class K8sBuildConfigOutput():
    def __init__(self):
        pass

    def print_build_configs(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Build Config', 'namespace_name'],
                ['Type', 'type'],
                ['Ref', 'ref'],
                ['URI', 'uri']
            ]
        )