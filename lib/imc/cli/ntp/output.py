class ImcCliNtpOutput():
    def __init__(self):
        pass

    def print_imc_ntp(self, info):
        self.print_list_table(
            info,
            title='NTP',
            add_endpoint_ip=True,
            allow_order_subkeys=False,
            expand=['Server']
        )
