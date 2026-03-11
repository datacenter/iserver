class K8sGroupOutput():
    def __init__(self):
        pass

    def print_groups_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Group', 'name'],
                ['User', 'usersT'],
                ['LDAP Sync', 'ldapT']
            ]
        )
