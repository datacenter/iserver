class ImcCliSshOutput():
    def __init__(self):
        pass

    def print_imc_ssh(self, info):
        self.print_list_dict(
            info,
            'SSH',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
