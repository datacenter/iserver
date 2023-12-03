class AdapterExtEthInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['AdapterUnitId'] = managed_object['AdapterUnit']['Moid']
        info['AdminState'] = managed_object['AdminState']
        info['InterfaceId'] = managed_object['ExtEthInterfaceId']
        info['MacAddress'] = managed_object['MacAddress'].lower()
        info['SwitchId'] = managed_object['SwitchId']

        info['PeerHostPortId'] = None
        if managed_object['AcknowledgedPeerInterface'] is not None:
            if managed_object['AcknowledgedPeerInterface']['ObjectType'] == 'ether.HostPort':
                info['PeerHostPortId'] = managed_object['AcknowledgedPeerInterface']['Moid']
        info['PeerAggrPortId'] = managed_object['PeerAggrPortId']
        info['PeerDn'] = managed_object['PeerDn']
        info['PeerPortId'] = managed_object['PeerPortId']
        info['PeerSlotId'] = managed_object['PeerSlotId']

        return info
