class ImcCliAdapterOutput():
    def __init__(self):
        pass

    def print_imc_adapter(self, info):
        self.print_list_dict(
            info,
            'Adapter'
        )

    def print_imc_adapter_compare(self, info):
        self.print_compare(
            info,
            'Adapter'
        )

    def print_imc_adapter_ext(self, info):
        self.print_list_dict(
            info,
            'External Ethernet interface',
            allow_order_subkeys=False
        )

    def print_imc_adapter_host(self, info):
        self.print_list_dict(
            info,
            'Host Ethernet interface',
            allow_order_subkeys=False
        )

    def print_imc_adapter_fc(self, info):
        self.print_list_dict(
            info,
            'Host Fibre Channel interface',
            allow_order_subkeys=False
        )
