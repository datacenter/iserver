class RedfishEndpointUcsRackTemplateBiosOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_bios_properties(self, info_dict, title=False):
        info = []
        for key in info_dict:
            if key not in ['__Output']:
                item = {}
                item['key'] = key
                item['value'] = info_dict[key]
                info.append(item)

        info = sorted(
            info,
            key=lambda i: i['key'].lower()
        )

        if title:
            self.my_output.default(
                'Bios [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')

        order = [
            'key',
            'value'
        ]

        headers = [
            'Key',
            'Value'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ucsc_bios_diff_properties(self, info, title=False):
        order = [
            'key'
        ]
        headers = [
            'Key'
        ]
        for server_ip in info:
            order.append(server_ip)
            headers.append(server_ip)

        bios_key = []
        for server_ip in info:
            for key in info[server_ip]:
                if key not in bios_key:
                    bios_key.append(key)

        bios_key = sorted(bios_key)

        bios_values = []
        for key in bios_key:
            item = {}
            item['key'] = key
            for server_ip in info:
                if key not in info[server_ip]:
                    item[server_ip] = '--'
                else:
                    item[server_ip] = info[server_ip][key]

            bios_values.append(
                item
            )

        if title:
            self.my_output.default(
                'Bios [#%s]' % (len(bios_values)),
                underline=True,
                before_newline=True
            )

        self.my_output.my_table(
            bios_values,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )
