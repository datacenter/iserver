class ImcCliStorageAdapterOutput():
    def __init__(self):
        pass

    def print_imc_storage_adapter(self, info):
        self.print_list_dict(
            info,
            'Storage Adapter'
        )

    def print_imc_storage_adapter_compare(self, info):
        self.print_compare(
            info,
            'Storage Adapter',
            expand=['Product Name']
        )
