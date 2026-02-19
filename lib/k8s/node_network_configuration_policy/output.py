class K8sNodeNetworkConfigurationPolicyOutput():
    def __init__(self):
        pass

    def print_node_network_configuration_policy(self, info, title=False):
        if title:
            self.my_output.default(
                'Node Network Configuration Policy [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'status',
            'reason'
        ]

        headers = [
            'NNCP',
            'Status',
            'Reason'
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
