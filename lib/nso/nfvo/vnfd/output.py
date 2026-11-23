class NfvoVnfdOutput():
    def __init__(self):
        pass

    def print_vnfds(self, info):
        order = [
            'id',
            'provider',
            'product-name',
            'software-version',
            'product-info-name',
            'product-info-description'
        ]

        headers = [
            'VNFD ID',
            'Provider',
            'Product Name',
            'Software Version',
            'Info Name',
            'Info Description'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
