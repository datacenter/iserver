class FilterOutput():
    def __init__(self):
        pass

    def print_filters(self, info):
        self.my_output.default(
            'Contract Filters',
            underline=True,
            before_newline=True
        )

        order = [
            'nameTenant',
            'vzEntry.name',
            'vzEntry.etherT',
            'vzEntry.arpOpc',
            'vzEntry.prot',
            'vzEntry.applyToFrag',
            'vzEntry.stateful',
            'vzEntry.source',
            'vzEntry.destination',
            'vzEntry.tcpRules'
        ]

        headers = [
            'Filter',
            'Entry',
            'Ether',
            'ARP Flag',
            'Proto',
            'Fragments',
            'Stateful',
            'Source',
            'Destination',
            'Rules'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vzEntry']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

    def print_filters_usage(self, info):
        self.my_output.default(
            'Contract Filters Usage',
            underline=True,
            before_newline=True
        )

        order = [
            'nameTenant',
            'contract.nameTenant',
            'taboo.nameTenant'
        ]

        headers = [
            'Filter',
            'Contract',
            'Taboo'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['contract', 'taboo']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )
