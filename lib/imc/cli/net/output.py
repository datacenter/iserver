class ImcCliNetOutput():
    def __init__(self):
        pass

    def print_imc_net(self, info):
        self.print_list_dict(
            info,
            'Network Adapter',
            allow_order_subkeys=False
        )
