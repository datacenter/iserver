class NodeOutput():
    def __init__(self):
        pass

    def print_nodes(self, nodes, title=False):
        if title:
            self.my_output.default(
                'Node - State [#%s]' % (len(nodes)),
                underline=True,
                before_newline=True
            )

        if len(nodes) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'name',
            'type',
            'sn',
            'ip',
            'software',
            'reachableTick',
            'syncTick'
        ]

        headers = [
            'Name',
            'Type',
            'SN',
            'IP',
            'Version',
            'Reachable',
            'Sync'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
