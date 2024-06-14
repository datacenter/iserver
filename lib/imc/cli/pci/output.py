class ImcCliPciOutput():
    def __init__(self):
        pass

    def print_imc_pci(self, info):
        self.print_list_dict(
            info,
            'PCI',
            allow_order_subkeys=False
        )
