import json


class K8sIpAddressPoolOutput():
    def __init__(self):
        pass

    def print_ip_address_pools(self, info):
        for item in info:
            item['statusT'] = json.dumps(item['status'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['IP Address Pool', 'namespace_nameT'],
                ['Address', 'addr'],
                ['Status', 'statusT']
            ]
        )