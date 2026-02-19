class ImcCliHttpOutput():
    def __init__(self):
        pass

    def print_imc_http(self, info, add_title_endpoint_ip=True):
        self.print_list_table(
            info,
            title='HTTP',
            add_title_endpoint_ip=add_title_endpoint_ip,
            allow_order_subkeys=False
        )
