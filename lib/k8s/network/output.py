class K8sNetworkOutput():
    def __init__(self):
        pass

    def print_networks(self, info, title=False):
        if title:
            self.my_output.default(
                'Network [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'network_type',
            'cluster_network',
            'host_prefix',
            'service_network'
        ]

        headers = [
            'Network',
            'Network Type',
            'Cluster Network',
            'Host Prefix',
            'Service Network'
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

    def print_network(self, info):
        order = [
            'name',
            'network_type',
            'cluster_network',
            'host_prefix',
            'service_network'
        ]

        headers = [
            'Name',
            'Network Type',
            'Cluster Network',
            'Host Prefix',
            'Service Network'
        ]

        self.my_output.dictionary(
            info,
            keys=order,
            title_keys=headers,
            title='OpenShift Network',
            justify=True,
            prefix='- '
        )
