class ImcCliTlsOutput():
    def __init__(self):
        pass

    def print_imc_tls(self, info):
        self.print_list_table(
            info,
            title='TLS',
            add_endpoint_ip=True,
            allow_order_subkeys=False,
            exclude=['TLS Version 1.2 Cipher List', 'TLS Version 1.3 Cipher Suite'],
            expand=['TLS 1.2 Cipher List', 'TLS 1.3 Cipher Suite'],
            row_separator=True
        )
