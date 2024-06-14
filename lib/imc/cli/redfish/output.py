class ImcCliRedfishOutput():
    def __init__(self):
        pass

    def print_imc_redfish(self, info):
        self.print_list_dict(
            info,
            'Redfish',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
