class K8sIssuerOutput():
    def __init__(self):
        pass

    def print_issuers_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Issuer', 'namespace_nameT'],
                ['Secret', 'secretT'],
                ['Certificate', 'crtT'],
                ['Ready', 'readyT']
            ]
        )