class ImcCliIpOutput():
    def __init__(self):
        pass

    def print_imc_ip_network(self, info):
        self.print_list_dict(
            info,
            'IMC - Network'
        )

    def print_imc_ip_icmp(self, info):
        self.print_list_dict(
            info,
            'IMC - ICMP'
        )

    def print_imc_ip_blocking(self, info):
        self.print_list_dict(
            info,
            'IMC - IP Blocking'
        )

    def print_imc_ip_filtering(self, info):
        self.print_list_dict(
            info,
            'IMC - IP Filtering'
        )

    def print_imc_ip(self, info):
        for item in info:
            if 'network' in item:
                self.print_imc_ip_network(item['network'])
            if 'icmp' in item:
                self.print_imc_ip_icmp(item['icmp'])
            if 'blocking' in item:
                self.print_imc_ip_blocking(item['blocking'])
            if 'filtering' in item:
                self.print_imc_ip_filtering(item['filtering'])
