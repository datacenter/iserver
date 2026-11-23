class ImcCliHardwareOutput():
    def __init__(self):
        pass

    def print_imc_hardware(self, info):
        for item in info:
            self.my_output.default(
                'Endpoint: %s' % (item['endpoint_ip']),
                before_newline=True,
                underline=True
            )

            if 'cpu' in item:
                self.print_imc_cpu(item['cpu'])

            if 'memory' in item:
                self.print_imc_memory(item['memory'])

            if 'dimm' in item:
                self.print_imc_dimm(item['dimm'])

            if 'sc' in item:
                self.print_imc_storage_adapter(item['sc'])

            if 'bbu' in item:
                self.print_imc_bbu(item['bbu'])

            if 'hdd' in item:
                self.print_imc_hdd(item['hdd'])

            if 'flex' in item:
                self.print_imc_flex(item['flex'])

            if 'pci' in item:
                self.print_imc_pci(item['pci'])

            if 'net' in item:
                self.print_imc_net(item['net'])

            if 'vic' in item:
                self.print_imc_adapter(item['vic'])

            if 'tpm' in item:
                self.print_imc_tpm(item['tpm'])

            if 'psu' in item:
                self.print_imc_psu(item['psu'])
