from lib import ip_helper
from lib import filter_helper


class AdapterHostEthInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = filter_helper.get(managed_object, 'Moid')
        info['Dn'] = filter_helper.get(managed_object, 'Dn')
        info['Type'] = 'HostEth'
        info['AdapterUnitId'] = filter_helper.get(managed_object, 'AdapterUnitId:Moid')
        info['AdminState'] = filter_helper.get(managed_object, 'AdminState')
        info['HostEthInterfaceId'] = filter_helper.get(managed_object, 'HostEthInterfaceId')
        info['InterfaceType'] = filter_helper.get(managed_object, 'InterfaceType')
        info['MacAddress'] = ip_helper.reformat_mac(
            filter_helper.get(managed_object, 'MacAddress')
        )
        info['Name'] = filter_helper.get(managed_object, 'Name', on_error='', on_none='')
        info['OperState'] = filter_helper.get(managed_object, 'OperState')
        info['Operability'] = filter_helper.get(managed_object, 'Operability')
        info['PciAddr'] = filter_helper.get(managed_object, 'PciAddr')
        info['PeerDn'] = filter_helper.get(managed_object, 'PeerDn')
        info['PeerInterface'] = filter_helper.get(managed_object, 'PeerInterface')

        return info
