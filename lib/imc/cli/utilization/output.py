class ImcCliUtilizationOutput():
    def __init__(self):
        pass

    def print_imc_utilization(self, info):
        self.print_list_dict(
            info,
            'Utilization'
        )

    def print_imc_utilization_compare(self, info):
        self.print_compare(
            info,
            'Utilization'
        )
