class OcpClusterConsoleOutput():
    def __init__(self):
        pass

    def print_ocp_cluster_console(self, info):
        order = [
            'name',
            'consoleUrl',
            'consoleIp',
            'consoleDns',
            'authFqdn',
            'authIp',
            'authDns',
            'consoleUsername',
            'consolePassword'
        ]

        headers = [
            'Name',
            'Console URL',
            'Expected Resolved IP',
            'DNS Resolved IP',
            'Authentication FQDN',
            'Expected Resolved IP',
            'DNS Resolved IP',
            'Username',
            'Password'
        ]

        self.my_output.dictionary(
            info,
            title='OCP Console',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_ocp_clusters_console(self, info):
        order = [
            'name',
            'consoleUrl',
            'consoleIp',
            'consoleDns',
            'authFqdn',
            'authIp',
            'authDns',
            'consoleUsername',
            'consolePassword'
        ]

        headers = [
            'Name',
            'Console URL',
            'Expected Resolved IP',
            'DNS Resolved IP',
            'Authentication FQDN',
            'Expected Resolved IP',
            'DNS Resolved IP',
            'Username',
            'Password'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
