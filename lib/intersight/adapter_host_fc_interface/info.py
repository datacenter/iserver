class AdapterHostFcInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Type'] = 'HostFc'
        info['Dn'] = managed_object['Dn']
        info['AdapterUnitId'] = managed_object['AdapterUnit']['Moid']
        info['AdminState'] = managed_object['AdminState']
        info['HostFcInterfaceId'] = managed_object['HostFcInterfaceId']
        info['Name'] = managed_object['Name']
        info['OperState'] = managed_object['OperState']
        info['Operability'] = managed_object['Operability']
        info['Wwnn'] = managed_object['Wwnn']
        info['Wwpn'] = managed_object['Wwpn']

        return info
