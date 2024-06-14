class ImcCliVersionOutput():
    def __init__(self):
        pass

    def print_imc_version(self, info):
        self.print_list_dict(
            info,
            'Version'
        )

    def print_imc_version_compare(self, info):
        self.print_compare(
            info,
            'Version'
        )
