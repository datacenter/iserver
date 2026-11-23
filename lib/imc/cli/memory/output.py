class ImcCliMemoryOutput():
    def __init__(self):
        pass

    def print_imc_memory(self, info):
        self.print_list_dict(
            info,
            'Memory'
        )

    def print_imc_memory_compare(self, info):
        self.print_compare(
            info,
            'Memory'
        )
