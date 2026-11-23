class DomainAaaOutput():
    def __init__(self):
        pass

    def print_domains_aaa(self, domain_aaa):
        if len(domain_aaa) == 0:
            self.my_output.default('No aaa domain found')
            return

        order = [
            'faults',
            'name'
        ]

        headers = [
            'Faults',
            'AAA Domain Name'
        ]

        self.my_output.my_table(
            domain_aaa,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
