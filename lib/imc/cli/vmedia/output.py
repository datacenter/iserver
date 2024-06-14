class ImcCliVmediaOutput():
    def __init__(self):
        pass

    def print_imc_vmedia(self, info):
        self.print_list_dict(
            info,
            'vMedia',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
