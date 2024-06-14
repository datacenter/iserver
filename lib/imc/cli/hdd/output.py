class ImcCliHddOutput():
    def __init__(self):
        pass

    def print_imc_hdd(self, info):
        self.print_list_dict(
            info,
            'HDD',
            allow_order_subkeys=False
        )
