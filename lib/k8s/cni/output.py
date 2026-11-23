class K8sCniOutput():
    def __init__(self):
        pass

    def print_cnis(self, info):
        order = [
            'cni',
            'cluster.cidr',
            'cluster.hostPrefix',
            'service'
        ]

        headers = [
            'CNI Network Type',
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
