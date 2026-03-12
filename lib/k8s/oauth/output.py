class K8sOAuthOutput():
    def __init__(self):
        pass

    def print_oauths(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['OAuth', 'name'],
                ['Identity Provider', 'idp.name'],
                ['Identity Type', 'idp.type'],
                ['Identity Users', 'idp.userCount']
            ]
        )

    def print_oauths_htpasswd(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['OAuth', 'oauth'],
                ['Htpasswd Provider', 'name'],
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
                ['LDAP Provider', 'name'],
                ['LDAP', 'ldapT'],
                ['Attribute', 'attributeT'],
                ['Usage', 'usageT']
            ]
        )
