class ImcCliSmtpOutput():
    def __init__(self):
        pass

    def print_imc_smtp(self, info):
        self.print_list_table(
            info,
            title='SMTP',
            add_endpoint_ip=True,
            allow_order_subkeys=False,
            exclude=['Recipient'],
            expand=['Recipients']
        )
