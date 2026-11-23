class K8sNemoEvaluatorOutput():
    def __init__(self):
        pass

    def print_nemo_evaluators(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Nim Build', 'namespace_nameT']
            ]
        )