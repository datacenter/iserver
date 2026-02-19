class ImcCliRedfishOutput():
    def __init__(self):
        pass

    def print_imc_redfish(self, info):
        self.print_list_table(
            info,
            title='Redfish',
            add_endpoint_ip=True,
            allow_order_subkeys=False
        )
