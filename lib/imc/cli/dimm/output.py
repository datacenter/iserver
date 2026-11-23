class ImcCliDimmOutput():
    def __init__(self):
        pass

    def print_imc_dimm(self, info):
        self.print_list_dict(
            info,
            'DIMM',
            allow_order_subkeys=False
        )
