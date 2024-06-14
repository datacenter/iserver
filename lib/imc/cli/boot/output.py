from lib import filter_helper


class ImcCliBootOutput():
    def __init__(self):
        pass

    def print_imc_boot(self, info):
        self.print_list_table(
            info,
            title='Boot Order'
        )

    def print_imc_boot_device(self, info):
        self.print_list_table(
            info,
            title='Boot Device'
        )
