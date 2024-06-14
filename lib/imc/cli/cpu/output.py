class ImcCliCpuOutput():
    def __init__(self):
        pass

    def print_imc_cpu(self, info):
        self.print_list_dict(
            info,
            'CPU',
            allow_order_subkeys=False
        )

    def print_imc_cpu_compare(self, info):
        self.print_compare(
            info,
            'CPU'
        )
