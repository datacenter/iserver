class K8sAuthOutput():
    def __init__(self):
        pass

    def print_auths(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Auth', 'name'],
                ['Admin Groups', 'admin'],
                ['Allowed Groups', 'allowed'],
                ['Ready', 'readyTick']
            ]
        )