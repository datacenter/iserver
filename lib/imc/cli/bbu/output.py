class ImcCliBbuOutput():
    def __init__(self):
        pass

    def print_imc_bbu(self, info):
        self.print_list_dict(
            info,
            'Battery Backup Unit'
        )

    def print_imc_bbu_compare(self, info):
        self.print_compare(
            info,
            'Battery Backup Unit'
        )
