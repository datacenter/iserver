class ImcCliFwOutput():
    def __init__(self):
        pass

    def print_imc_fw(self, info):
        self.print_list_dict(
            info,
            'Firmware'
        )

    def print_imc_fw_compare(self, info):
        self.print_compare(
            info,
            'Firmware'
        )
