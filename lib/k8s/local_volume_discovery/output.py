class K8sLocalVolumeDiscoveryOutput():
    def __init__(self):
        pass

    def print_local_volume_discoveries(self, info, title=False):
        if title:
            self.my_output.default(
                'Local Volume Discovery [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'availableT',
            'phase'
        ]

        headers = [
            'Local Volume Discovery',
            'Available',
            'Phase'
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
