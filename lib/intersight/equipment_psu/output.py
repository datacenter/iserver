class ComputePsuOutput():
    def __init__(self):
        pass

    def print_psu(self, servers, title=False):
        info = []
        for server in servers:
            if 'PsuInfo' in server:
                for item in server['PsuInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.default(
                'PSU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'StateTick',
            'PresenceTick',
            'Voltage',
            'Model',
            'Serial',
            'Vendor'
        ]

        headers = [
            'Server',
            'Name',
            'State',
            'Present',
            'Voltage',
            'Model',
            'Serial',
            'Vendor'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
