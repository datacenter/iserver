from lib import filter_helper


class AdapterHostFcInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = filter_helper.get(managed_object, 'Moid')
        info['Dn'] = filter_helper.get(managed_object, 'Dn')
        info['Type'] = 'HostFc'
        info['AdapterUnitId'] = filter_helper.get(managed_object, 'AdapterUnitId:Moid')
        info['AdminState'] = filter_helper.get(managed_object, 'AdminState')
        info['HostFcInterfaceId'] = filter_helper.get(managed_object, 'HostFcInterfaceId')
        info['Name'] = filter_helper.get(managed_object, 'Name', on_error='', on_none='')
        info['OperState'] = filter_helper.get(managed_object, 'OperState')
        info['Operability'] = filter_helper.get(managed_object, 'Operability')
        info['Wwnn'] = filter_helper.get(managed_object, 'Wwnn')
        info['Wwpn'] = filter_helper.get(managed_object, 'Wwpn')

        return info
