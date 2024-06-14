class ImcCliIpmiOutput():
    def __init__(self):
        pass

    def print_imc_ipmi(self, info):
        self.print_list_dict(
            info,
            'IPMI',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
