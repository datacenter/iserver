class ImcCliXmlOutput():
    def __init__(self):
        pass

    def print_imc_xml(self, info):
        self.print_list_dict(
            info,
            'XML API',
            add_endpoint_ip=True,
            underline=False,
            allow_order_subkeys=False
        )
