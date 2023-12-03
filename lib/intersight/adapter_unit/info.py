class AdapterUnitInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['AdapterId'] = managed_object['AdapterId']
        info['Name'] = 'Adapter %s' % (info['AdapterId'])
        info['BaseMacAddress'] = managed_object['BaseMacAddress']
        if managed_object['ComputeBlade'] is not None:
            info['ComputeNodeMoid'] = managed_object['ComputeBlade']['Moid']
        if managed_object['ComputeRackUnit'] is not None:
            info['ComputeNodeMoid'] = managed_object['ComputeRackUnit']['Moid']

        info['ExtEthIfsIds'] = []
        for interface in managed_object['ExtEthIfs']:
            info['ExtEthIfsIds'].append(interface['Moid'])
        info['ExtEthIfsCount'] = len(info['ExtEthIfsIds'])

        info['HostEthIfsIds'] = []
        for interface in managed_object['HostEthIfs']:
            info['HostEthIfsIds'].append(interface['Moid'])
        info['HostEthIfsCount'] = len(info['HostEthIfsIds'])

        info['HostFcIfsIds'] = []
        for interface in managed_object['HostFcIfs']:
            info['HostFcIfsIds'].append(interface['Moid'])
        info['HostFcIfsCount'] = len(info['HostFcIfsIds'])

        info['HostIscsiIfsIds'] = []
        for interface in managed_object['HostIscsiIfs']:
            info['HostIscsiIfsIds'].append(interface['Moid'])
        info['HostIscsiIfsCount'] = len(info['HostIscsiIfsIds'])

        info['Model'] = managed_object['Model']
        info['OperState'] = managed_object['OperState']
        info['PartNumber'] = managed_object['PartNumber']
        info['Presence'] = managed_object['Presence']
        info['Healthy'] = False
        if info['Presence'] == 'equipped' and info['OperState'] == 'OK':
            info['Healthy'] = True
        info['PciSlot'] = managed_object['PciSlot']
        info['Thermal'] = managed_object['Thermal']
        info['Serial'] = managed_object['Serial']
        info['Vendor'] = managed_object['Vendor']

        return info
