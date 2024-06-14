class ImcCliAdapterOutput():
    def __init__(self):
        pass

    def print_imc_adapter(self, info):
        self.print_list_dict(
            info,
            'Adapter'
        )

    def print_imc_adapter_compare(self, info):
        self.print_compare(
            info,
            'Adapter'
        )
