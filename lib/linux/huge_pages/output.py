class LinuxHugePagesOutput():
    def __init__(self):
        pass

    def print_linux_huge_pages(self, info, title=False):
        if title:
            self.my_output.default(
                'Huge Pages',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        items = []
        for server_info in info:
            item = {}
            item['server'] = server_info['name']
            item['name'] = 'Node 0'
            item['2mf'] = server_info['hp']['node0']['2M']['free']
            item['2mt'] = server_info['hp']['node0']['2M']['total']
            item['1gf'] = server_info['hp']['node0']['1G']['free']
            item['1gt'] = server_info['hp']['node0']['1G']['total']
            items.append(item)

            item = {}
            item['server'] = server_info['name']
            item['name'] = 'Node 1'
            item['2mf'] = server_info['hp']['node1']['2M']['free']
            item['2mt'] = server_info['hp']['node1']['2M']['total']
            item['1gf'] = server_info['hp']['node1']['1G']['free']
            item['1gt'] = server_info['hp']['node1']['1G']['total']
            items.append(item)

        order = [
            'server',
            'name',
            '2mf',
            '2mt',
            '1gf',
            '1gt'
        ]

        headers = [
            'Server',
            'Node',
            '2M Free',
            '2M Total',
            '1G Free',
            '1G Total'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            table=True
        )
