class ImcCliSelOutput():
    def __init__(self):
        pass

    def print_imc_sel(self, info):
        self.print_list_dict(
            info,
            'SEL',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
