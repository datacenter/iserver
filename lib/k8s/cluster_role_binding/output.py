class K8sClusterRoleBindingOutput():
    def __init__(self):
        pass

    def print_cluster_role_bindings(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cluster Role Binding', 'name'],
                ['Role', 'role.name'],
                ['Subject', 'subject.description'],
                ['Age', 'age']
            ]
        )
