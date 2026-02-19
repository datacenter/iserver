class ImcCliIpmiOutput():
    def __init__(self):
        pass

    def print_imc_ipmi(self, info):
        self.print_list_table(
            info,
            title='IPMI',
            add_endpoint_ip=True,
            allow_order_subkeys=False
        )
