class AdapterHostEthInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Type'] = 'HostEth'
        info['Dn'] = managed_object['Dn']
        info['AdapterUnitId'] = managed_object['AdapterUnit']['Moid']
        info['AdminState'] = managed_object['AdminState']
        info['HostEthInterfaceId'] = managed_object['HostEthInterfaceId']
        info['InterfaceType'] = managed_object['InterfaceType']
        info['MacAddress'] = managed_object['MacAddress']
        info['Name'] = managed_object['Name']
        info['OperState'] = managed_object['OperState']
        info['Operability'] = managed_object['Operability']
        info['PciAddr'] = managed_object['PciAddr']
        info['PeerDn'] = managed_object['PeerDn']
        info['PeerInterface'] = managed_object['PeerInterface']

        return info
