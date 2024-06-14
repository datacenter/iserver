class ImcCliHttpOutput():
    def __init__(self):
        pass

    def print_imc_http(self, info):
        self.print_list_dict(
            info,
            'HTTP',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
