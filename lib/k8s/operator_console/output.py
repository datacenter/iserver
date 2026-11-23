class K8sOperatorConsoleOutput():
    def __init__(self):
        pass

    def print_operator_consoles_state(self, info):
        self.my_output.dictionary_ng(
            'Operator Console',
            info, 
            [
                ['Operator Console', 'name'],
                ['Management state', 'management'],
                ['Plugin', 'pluginT'],
                ['Age', 'age']
            ]
        )

        self.my_output.my_table_ng(
            info['condition'],
            [
                ['Condition Type', 'type'],
                ['Status', 'status'],
                ['lastTransitionTime', 'lastTransitionTime']        
            ]
        )