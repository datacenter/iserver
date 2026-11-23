class ImcCliChassisOutput():
    def __init__(self):
        pass

    def print_imc_chassis(self, info):
        self.print_list_dict(
            info,
            'Chassis'
        )

    def print_imc_chassis_compare(self, info):
        self.print_compare(
            info,
            'Chassis'
        )
