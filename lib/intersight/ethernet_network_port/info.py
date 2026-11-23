class EthernetNetworkPortInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['Name'] = '%s/%s' % (
            managed_object['SlotId'],
            managed_object['PortId']
        )

        info['IoModuleId'] = managed_object['EquipmentIoCardBase']['Moid']
        info['ModuleId'] = managed_object['ModuleId']
        info['OperState'] = managed_object['OperState']
        info['Up'] = False
        if info['OperState'] == 'up':
            info['Up'] = True
        info['PeerDn'] = managed_object['PeerDn']
        info['PeerInterfaceId'] = None
        info['PeerInterfaceType'] = None
        if managed_object['PeerInterface'] is not None:
            info['PeerInterfaceId'] = managed_object['PeerInterface']['Moid']
            info['PeerInterfaceType'] = managed_object['PeerInterface']['ObjectType']
        info['PortId'] = managed_object['PortId']
        info['SlotId'] = managed_object['SlotId']
        info['Speed'] = managed_object['Speed']
        info['SwitchId'] = managed_object['SwitchId']

        return info
