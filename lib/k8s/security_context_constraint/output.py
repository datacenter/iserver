class K8sSecurityContextConstraintOutput():
    def __init__(self):
        pass

    def print_security_context_constraints(self, info, title=False):
        if title:
            self.my_output.default(
                'Security Context Constraint [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        info = self.my_output.prepare_list(
            info,
            empty=['allowedCapabilities', 'priority', 'volumes']
        )

        order = [
            'name',
            'allowPrivilegeEscalation',
            'allowPrivilegedContainer',
            'allowedCapabilities',
            'priority',
            'seLinuxContext',
            'runAsUser',
            'fsGroup',
            'supplementalGroups',
            'readOnlyRootFilesystem',
            'volumes',
            'age'
        ]

        headers = [
            'Name',
            'Priv Esc',
            'Priv Cont',
            'Caps',
            'Priority',
            'SELinux',
            'RunAsUser',
            'FsGroup',
            'SupGroup',
            'RO RootFs',
            'Volumes',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['allowedCapabilities', 'volumes']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
