class K8sCniOutput():
    def __init__(self):
        pass

    def print_cnis(self, info, title=False):
        if title:
            self.my_output.default(
                'K8s Cluster CNI [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'cni',
            'cluster.cidr',
            'cluster.hostPrefix',
            'service'
        ]

        headers = [
            'Network Type',
            'Cluster CIDR',
            'Cluster Host Prefix',
            'Service CIDR'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['cluster', 'service']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
