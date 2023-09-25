class K8sVersionOutput():
    def __init__(self):
        pass

    def print_versions(self, info, title=False):
        if title:
            self.my_output.default(
                'K8s Cluster Version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'version',
            'platform',
            'build_date',
            'ocp'
        ]

        headers = [
            'Version',
            'Platform',
            'Build Date',
            'Openshift'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
