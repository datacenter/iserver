from lib import ip_helper
from lib import filter_helper


class AdapterUnitInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = filter_helper.get(managed_object, 'Moid')
        info['Dn'] = filter_helper.get(managed_object, 'Dn')
        info['AdapterId'] = filter_helper.get(managed_object, 'AdapterId')
        info['Name'] = filter_helper.get(managed_object, 'Name', on_error='', on_none='')
        info['BaseMacAddress'] = ip_helper.reformat_mac(
            filter_helper.get(managed_object, 'BaseMacAddress')
        )
        info['ComputeNodeMoid'] = None
        if managed_object['ComputeBlade'] is not None:
            info['ComputeNodeMoid'] = filter_helper.get(managed_object, 'ComputeBlade:Moid')
        if managed_object['ComputeRackUnit'] is not None:
            info['ComputeNodeMoid'] = filter_helper.get(managed_object, 'ComputeRackUnit:Moid')

        info['ExtEthIfsIds'] = []
        for interface in filter_helper.get(managed_object, 'ExtEthIfs', on_error=[], on_none=[]):
            info['ExtEthIfsIds'].append(interface['Moid'])
        info['ExtEthIfsCount'] = len(info['ExtEthIfsIds'])

        info['HostEthIfsIds'] = []
        for interface in filter_helper.get(managed_object, 'HostEthIfs', on_error=[], on_none=[]):
            info['HostEthIfsIds'].append(interface['Moid'])
        info['HostEthIfsCount'] = len(info['HostEthIfsIds'])

        info['HostFcIfsIds'] = []
        for interface in filter_helper.get(managed_object, 'HostFcIfs', on_error=[], on_none=[]):
            info['HostFcIfsIds'].append(interface['Moid'])
        info['HostFcIfsCount'] = len(info['HostFcIfsIds'])

        info['HostIscsiIfsIds'] = []
        for interface in filter_helper.get(managed_object, 'HostIscsiIfs', on_error=[], on_none=[]):
            info['HostIscsiIfsIds'].append(interface['Moid'])
        info['HostIscsiIfsCount'] = len(info['HostIscsiIfsIds'])

        info['Model'] = filter_helper.get(managed_object, 'Model')
        info['OperState'] = filter_helper.get(managed_object, 'OperState')
        info['PartNumber'] = filter_helper.get(managed_object, 'PartNumber')
        info['Presence'] = filter_helper.get(managed_object, 'Presence')
        info['Healthy'] = False
        if info['Presence'] == 'equipped' and info['OperState'] == 'OK':
            info['Healthy'] = True

        info['PciSlot'] = filter_helper.get(managed_object, 'PciSlot')
        info['Thermal'] = filter_helper.get(managed_object, 'Thermal')
        info['Serial'] = filter_helper.get(managed_object, 'Serial')
        info['Vendor'] = filter_helper.get(managed_object, 'Vendor')

        return info
