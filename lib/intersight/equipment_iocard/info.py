from lib import ip_helper


class EquipmentIoCardInfo():
    def __init__(self):
        pass

    def is_iocard_on(self, item):
        if item is None:
            return False

        if item['Presence'] == 'equipped' and item['OperState'] == 'OK':
            return True

        return False

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['Model'] = managed_object['Model']
        info['ConnectionPath'] = managed_object['ConnectionPath']
        info['ConnectionStatus'] = managed_object['ConnectionStatus']
        info['Description'] = managed_object['Description']
        info['ManagementIp'] = None
        info['ManagementSubnet'] = None
        info['ManagementPrefix'] = None
        info['ManagementCidr'] = None
        info['ManagementGateway'] = None
        info['ManagementVlan'] = None

        if managed_object['Presence'] == 'equipped' and managed_object['OperState'].lower() in  ['ok', 'operable']:
            info['On'] = True
            info['OperTick'] = '\u2713'
            info['__Output']['OperTick'] = 'Green'
        else:
            info['On'] = False
            info['OperTick'] = '\u2717'
            info['__Output']['OperTick'] = 'Red'

        if managed_object['InbandIpAddresses'] is not None:
            for inband in managed_object['InbandIpAddresses']:
                if inband['ClassId'] == 'compute.IpAddress':
                    info['ManagementIp'] = inband['Address']
                    info['ManagementSubnet'] = inband['Subnet']
                    info['ManagementPrefix'] = ip_helper.netmask_to_prefix(
                        info['ManagementSubnet']
                    )
                    info['ManagementCidr'] = '%s/%s' % (
                        info['ManagementIp'],
                        info['ManagementPrefix']
                    )
                    info['ManagementGateway'] = inband['DefaultGateway']
                    info['ManagementVlan'] = inband['KvmVlan']

        info['FanMoids'] = []
        for fan in managed_object['FanModules']:
            info['FanMoids'].append(fan['Moid'])
        info['FansCount'] = len(
            info['FanMoids']
        )

        info['HostPorts'] = []
        for port in managed_object['HostPorts']:
            info['HostPorts'].append(port['Moid'])
        info['HostPortsCount'] = len(
            info['HostPorts']
        )

        info['NetworkPorts'] = []
        for port in managed_object['NetworkPorts']:
            info['NetworkPorts'].append(port['Moid'])
        info['NetworkPortsCount'] = len(
            info['NetworkPorts']
        )

        info['Name'] = 'I/O #%s (%s)' % (
            managed_object['ModuleId'],
            managed_object['Side'].lower()
        )

        info['ModuleId'] = managed_object['ModuleId']
        info['OperState'] = managed_object['OperState']
        info['PartNumber'] = managed_object['PartNumber'].strip()
        info['Pid'] = managed_object['Pid']
        if info['Pid'] is None or len(info['Pid']) == 0:
            info['Pid'] = info['Model']

        info['Presence'] = managed_object['Presence']
        if info['Presence'] == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        info['ProductName'] = managed_object['ProductName']
        info['Serial'] = managed_object['Serial']
        info['Side'] = managed_object['Side']
        info['Version'] = managed_object['Version']
        info['Vendor'] = managed_object['Vendor']

        return info
