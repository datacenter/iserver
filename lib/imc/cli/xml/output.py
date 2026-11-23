class ImcCliXmlOutput():
    def __init__(self):
        pass

    def print_imc_xml(self, info):
        self.print_list_table(
            info,
            title='XML API',
            add_endpoint_ip=True,
            allow_order_subkeys=False
        )
