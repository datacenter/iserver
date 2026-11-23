class K8sUserOutput():
    def __init__(self):
        pass

    def print_users_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['User', 'name'],
                ['Full Name', 'full_name'],
                ['Group', 'groups'],
                ['Identity', 'identities'],
                ['Provider Name', 'identityT.provider_name'],
                ['Provider User', 'identityT.provider_username']
            ]
        )
