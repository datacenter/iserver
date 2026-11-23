class ImcCliFlexOutput():
    def __init__(self):
        pass

    def print_imc_flex(self, info):
        self.print_list_dict(
            info,
            'Flexutil Controller'
        )

    def print_imc_flex_compare(self, info):
        self.print_compare(
            info,
            'Flexutil Controller'
        )
