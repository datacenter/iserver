class K8sAuthenticationOutput():
    def __init__(self):
        pass

    def print_authentications_state(self, info, table=True):
        if table:
            self.my_output.my_table_ng(
                info,
                [
                    ['Authentication Operator', 'name'],
                    ['Log Level', 'logLevel'],
                    ['Error Conditions', 'error_conditions']
                ]
            )
            return
        
        self.my_output.dictionary_ng(
            'Authentication Operator',
            info,
            [
                ['Name', 'name'],
                ['Log Level', 'logLevel'],
                ['Error Conditions', 'error_conditionsT']
            ]
        )
