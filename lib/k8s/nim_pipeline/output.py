class K8sNimPipelineOutput():
    def __init__(self):
        pass

    def print_nim_pipelines(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Nim Pipeline', 'namespace_nameT']
            ]
        )