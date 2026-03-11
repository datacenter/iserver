class K8sIdentityOutput():
    def __init__(self):
        pass

    def print_identities(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Identity', 'name'],
                ['Provider Name', 'providerName'],
                ['Provider Username', 'providerUserName']
            ]
        )
