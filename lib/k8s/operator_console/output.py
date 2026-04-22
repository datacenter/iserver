class K8sOperatorConsoleOutput():
    def __init__(self):
        pass

    def print_operator_consoles_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Operator Console', 'name'],
                ['Age', 'age']
            ]
        )
