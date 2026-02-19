class MdSerialOutput():
    def __init__(self):
        pass

    def print_serial(self):
        self.print_page_header(
            'Inventory - Serial Numbers'
        )
        self.my_output.print_stream('[Back](./README.md)', 'output')

        order = [
            'Serial',
            'Parent',
            'Scope',
            'Type',
            'Description'
        ]
        self.print_table_header(order)

        for item in self.xd_handler.get_serials():
            line = ''
            line = self.add_column(line, item['serial'])
            if item['parent'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['parent'])
            line = self.add_column(line, item['scope'])
            line = self.add_column(line, item['type'])
            line = self.add_column(line, item['description'])
            self.my_output.print_stream(line, 'output')

        self.save_output('serial')
