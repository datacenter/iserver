class K8sNodeNetworkConfigurationEnactmentOutput():
    def __init__(self):
        pass

    def print_node_network_configuration_enactment(self, info, title=False):
        if title:
            self.my_output.default(
                'Node Network Configuration Enactment [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return
        
        order = [
            'name',
            'status'
        ]

        headers = [
            'NNCE',
            'Status'
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
