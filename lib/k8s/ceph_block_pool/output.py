class K8sCephBlockPoolOutput():
    def __init__(self):
        pass

    def print_ceph_block_pools(self, info, title=False):
        if title:
            self.my_output.default(
                'Ceph Block Pool [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'phase',
            'readyTick',
            'pool_id',
            'failure_domain',
            'type'
        ]

        headers = [
            'Ceph Block Pool',
            'Phase',
            'Ready',
            'Pool ID',
            'Failure Domain',
            'Type'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
