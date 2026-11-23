from lib import filter_helper
from lib import ip_helper


class AdapterExtEthInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = filter_helper.get(managed_object, 'Moid')
        info['Dn'] = filter_helper.get(managed_object, 'Dn')
        info['AdapterUnitId'] = filter_helper.get(managed_object, 'AdapterUnit:Moid')
        info['AdminState'] = filter_helper.get(managed_object, 'AdminState')
        info['InterfaceId'] = filter_helper.get(managed_object, 'ExtEthInterfaceId')
        info['MacAddress'] = ip_helper.reformat_mac(
            filter_helper.get(managed_object, 'MacAddress')
        )
        info['SwitchId'] = filter_helper.get(managed_object, 'SwitchId')
        info['PeerAggrPortId'] = filter_helper.get(managed_object, 'PeerAggrPortId')
        info['PeerDn'] = filter_helper.get(managed_object, 'PeerDn')
        info['PeerPortId'] = filter_helper.get(managed_object, 'PeerPortId')
        info['PeerSlotId'] = filter_helper.get(managed_object, 'PeerSlotId')

        info['PeerHostPortId'] = None
        if managed_object['AcknowledgedPeerInterface'] is not None:
            if managed_object['AcknowledgedPeerInterface']['ObjectType'] == 'ether.HostPort':
                info['PeerHostPortId'] = filter_helper.get(managed_object, 'AcknowledgedPeerInterface:Moid')

        return info