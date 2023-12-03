class K8sClusterRoleBindingOutput():
    def __init__(self):
        pass

    def print_cluster_role_bindings(self, info, title=False):
        if title:
            self.my_output.default(
                'Cluster Role Binding [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'role.name',
            'subject.description',
            'age'
        ]

        headers = [
            'Name',
            'Role',
            'Subject',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['subject']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
