class ImcCliLedOutput():
    def __init__(self):
        pass

    def print_imc_led(self, info):
        self.print_list_dict(
            info,
            'LED',
            add_endpoint_ip=False,
            underline=False,
            allow_order_subkeys=False
        )
