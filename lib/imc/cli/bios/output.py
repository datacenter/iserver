class ImcCliBiosOutput():
    def __init__(self):
        pass

    def print_imc_bios(self, info):
        items = []
        for item in info:
            items.append(
                item['state']
            )

        self.print_list_dict(
            items,
            'BIOS State'
        )

    def print_imc_bios_compare(self, info):
        items = []
        for item in info:
            items.append(
                item['state']
            )

        self.print_compare(
            items,
            'BIOS State'
        )

    def print_imc_bios_params(self, info):
        items = []
        for item in info:
            items.append(
                item['params']
            )

        for item in items:
            for key in item:
                self.print_list_dict(
                    [item[key]],
                    'BIOS Parameters: %s' % (key),
                    allow_order_subkeys=False
                )

    def print_imc_bios_params_compare(self, info):
        param_types = []
        for item in info:
            for key in item['params']:
                if key not in param_types:
                    param_types.append(key)

        for param_type in param_types:
            items = []
            for item in info:
                for key in item['params']:
                    if key == param_type:
                        items.append(
                            item['params'][key]
                        )

            self.print_compare(
                items,
                'BIOS Parameters: %s' % (param_type)
            )
