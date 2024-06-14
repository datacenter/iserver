class ImcCliSolOutput():
    def __init__(self):
        pass

    def print_imc_sol(self, info):
        self.print_list_dict(
            info,
            'Serial over LAN',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
