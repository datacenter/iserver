class K8sSecretOutput():
    def __init__(self):
        pass

    def print_secrets(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Secret', 'namespace_nameT'],
                ['Owner', 'ownerT']
            ]
        )
