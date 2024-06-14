class ImcCliNtpOutput():
    def __init__(self):
        pass

    def print_imc_ntp(self, info):
        self.print_list_dict(
            info,
            'NTP',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
