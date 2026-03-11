class K8sOAuthOutput():
    def __init__(self):
        pass

    def print_oauths(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['OAuth', 'name']
            ]
        )

    def print_oauths_htpasswd(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['OAuth', 'oauth'],
                ['Provider', 'name'],
                ['Secret', 'secret'],
                ['Is Secret', 'isSecret'],
                ['User', 'usersT']
            ]
        )

    def print_oauths_ldap(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['OAuth', 'oauth'],
                ['Provider', 'name'],
                ['LDAP', 'ldapT'],
                ['Attribute', 'attributeT'],
                ['Usage', 'usageT']
            ]
        )
