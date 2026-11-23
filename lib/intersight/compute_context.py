class ComputeContext():
    def __init__(self):
        pass

    def get_context_ip(self, servers_info):
        ips = []
        for server_info in servers_info:
            if 'ManagementIp' in server_info and server_info['ManagementIp'] is not None:
                ips.append(
                    server_info['ManagementIp']
                )

        return ips

    def get_context_mac(self, servers_info):
        mac = []

        for server_info in servers_info:
            if 'HostEthInfo' in server_info and server_info['HostEthInfo'] is not None:
                for item in server_info['HostEthInfo']:
                    if '__show' not in item or item['__show']:
                        if item['MacAddress'] not in mac:
                            mac.append(item['MacAddress'])

            if 'ExtEthInfo' in server_info and server_info['ExtEthInfo'] is not None:
                for item in server_info['ExtEthInfo']:
                    if '__show' not in item or item['__show']:
                        if item['MacAddress'] not in mac:
                            mac.append(item['MacAddress'])


            if 'CimcInfo' in server_info and server_info['CimcInfo'] is not None:
                for item in server_info['CimcInfo']:
                    if '__show' not in item or item['__show']:
                        if item['MacAddress'] not in mac:
                            mac.append(item['MacAddress'])

        return mac
