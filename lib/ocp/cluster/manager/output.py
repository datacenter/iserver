class OcpClusterManagerOutput():
    def __init__(self):
        pass

    def print_ocp_cluster_manager(self, info):
        order = [
            'name',
            'installation',
            'release',
            'cni',
            'ssh.ip',
            'ssh.username',
            'ssh.password',
            'ssh.tick'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'IP',
            'Username',
            'Password',
            'SSH'
        ]

        self.my_output.dictionary(
            info,
            title='OCP Installer',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_ocp_clusters_manager(self, info):
        order = [
            'name',
            'installation',
            'release',
            'cni',
            'ssh.ip',
            'ssh.username',
            'ssh.password',
            'ssh.tick'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'IP',
            'Username',
            'Password',
            'Validated'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            table=True
        )
