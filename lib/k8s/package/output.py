from lib import filter_helper


class K8sPackageOutput():
    def __init__(self):
        pass

    def print_packages(self, info, title=False, description=False):
        if title:
            self.my_output.default(
                'Package [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        if description:
            for item in info:
                item['description'] = []
                if item['info']['description'] is not None:
                    item['description'] = filter_helper.get_string_chunks(
                        item['info']['description'],
                        40,
                        fixup_newline=True
                    )
        
        for item in info:
            item['installedT'] = False
            if 'installed' in item['info']:
                if item['info']['installed']:
                    item['installedT'] = '\u2713'
                    item['__Output']['installedT'] = 'Green'
                else:
                    item['installedT'] = '\u2717'
                    item['__Output']['installedT'] = 'Red'

        order = [
            'name',
            'installedT',
            'label.provider',
            'info.channel',
            'info.version'
        ]

        headers = [
            'Package',
            'Installed',
            'Provider',
            'Channel',
            'Version'
        ]

        if description:
            order.append('description')
            headers.append('Description')
            
            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['description']
                ),
                order=order,
                headers=headers,
                row_separator=True,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

        if not description:
            self.my_output.my_table(
                info,
                order=order,
                headers=headers,
                row_separator=False,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )
