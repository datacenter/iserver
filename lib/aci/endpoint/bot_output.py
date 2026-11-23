class EndpointBotOutput():
    def __init__(self):
        pass

    def print_endpoints(self, endpoints, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Endpoint [#%s]' % (len(endpoints)),
                underline=True,
                before_newline=True
            )

        if len(endpoints) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'apic',
            'flags',
            'mac',
            'fvIp.addr',
            'epgNameApTenant',
            'encapT',
            'bdNameTenant',
            'vrfNameTenant',
            'fabric.ep'
        ]

        headers = [
            'APIC',
            'SF',
            'MAC Address',
            'IP Address',
            'EPG',
            'Encap',
            'BD',
            'VRF',
            'Fabric'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                endpoints,
                order,
                ['fvIp', 'fabric']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            endpoints,
            order,
            headers,
            title='Endpoint'
        )

        html_output = self.my_output.get_output()

        return output, html_output