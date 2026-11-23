class ImcCliSshOutput():
    def __init__(self):
        pass

    def print_imc_ssh(self, info):
        self.print_list_table(
            info,
            title='SSH',
            add_endpoint_ip=True,
            allow_order_subkeys=False
        )
