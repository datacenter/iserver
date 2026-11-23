class K8sClusterRoleOutput():
    def __init__(self):
        pass

    def print_cluster_roles(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cluster Role', 'name'],
                ['Role', 'role.name'],
                ['Subject', 'subject.description'],
                ['Age', 'age']
            ]
        )
