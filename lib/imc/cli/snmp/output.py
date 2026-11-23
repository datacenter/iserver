class ImcCliSnmpOutput():
    def __init__(self):
        pass

    def print_imc_snmp(self, info):
        self.print_list_table(
            info,
            title='SNMP',
            add_endpoint_ip=True,
            allow_order_subkeys=False,
            exclude=['Server', 'User', 'SNMP EngineID', 'User EngineID']
        )

    def print_imc_snmp_server(self, info):
        servers = []
        for item in info:
            for server in item['Server']:
                server['__IP'] = item['__IP']
                servers.append(
                    server
                )

        self.print_list_table(
            servers,
            title='SNMP Trap Destination',
            add_endpoint_ip=True,
            allow_order_subkeys=False,
            exclude=['Enabled']
        )

    def print_imc_snmp_user(self, info):
        users = []
        for item in info:
            for user in item['User']:
                user['__IP'] = item['__IP']
                users.append(
                    user
                )

        self.print_list_table(
            users,
            title='SNMPv3 Users',
            add_endpoint_ip=True,
            allow_order_subkeys=False
        )
