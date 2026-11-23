class ImcCliPsuOutput():
    def __init__(self):
        pass

    def print_imc_psu(self, info):
        self.print_list_dict(
            info,
            'PSU',
            allow_order_subkeys=False
        )

    def print_imc_psu_compare(self, info):
        self.print_compare(
            info,
            'PSU'
        )
