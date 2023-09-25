class K8sClusterServiceVersionOutput():
    def __init__(self):
        pass

    def print_cluster_service_versions(self, info, title=False):
        if title:
            self.my_output.default(
                'Cluster Service Version - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'provider_name',
            'display_name',
            'version',
            'maturityT',
            'phase',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Provider',
            'Type',
            'Version',
            'Maturity',
            'Phase',
            'Age'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
