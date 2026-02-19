from lib import ip_helper
from lib import log_helper
from lib.intersight import cache as intersight_cache
from lib.intersight.network_element_summary import main as network_element_summary
from lib.intersight.ethernet_physical_port import main as ethernet_physical_port
from lib.intersight.ethernet_port_channel import main as ethernet_port_channel


class FiExtraAttributes():
    """Class for fi object extra attributes
    """
    def __init__(self, iaccount, log_id=None):
        self.fi_info = {}
        self.fi_helper = {}

        self.log_handler = log_helper.Log(log_id=log_id)

        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )

        self.network_element_summary_handler = network_element_summary.NetworkElementSummary(iaccount, log_id=log_id)
        self.ethernet_physical_port_handler = ethernet_physical_port.EthernetPhysicalPort(iaccount, log_id=log_id)
        self.ethernet_port_channel_handler = ethernet_port_channel.EthernetPortChannel(iaccount, log_id=log_id)

    def add_summary_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'summary',
            subdirectory=self.fi_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_summary_info',
                'No cache:%s' % (self.fi_info['Moid'])
            )
            return

        summary_info = self.network_element_summary_handler.get_info(
            managed_objects
        )
        for key in summary_info:
            if key not in self.fi_info or self.fi_info[key] is None:
                self.fi_info[key] = summary_info[key]

    def add_eth_info(self):
        self.fi_info['Ethernet'] = []
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'eth',
            subdirectory=self.fi_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_eth_info',
                'No cache:%s' % (self.fi_info['Moid'])
            )
            return

        for managed_object in managed_objects:
            self.fi_info['Ethernet'].append(
                self.ethernet_physical_port_handler.get_info(
                    managed_object
                )
            )

        self.fi_info['Ethernet'] = sorted(
            self.fi_info['Ethernet'],
            key=lambda i: i['PortId']
        )

    def add_pc_info(self):
        self.fi_info['EthernetPortChannel'] = []
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'pc',
            subdirectory=self.fi_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_pc_info',
                'No cache:%s' % (self.fi_info['Moid'])
            )
            return

        for managed_object in managed_objects:
            pc_info = self.ethernet_port_channel_handler.get_info(
                managed_object
            )
            pc_info['MemberCount'] = 0
            pc_info['MemberUp'] = 0
            pc_info['Ethernet'] = []
            for ethernet_info in self.fi_info['Ethernet']:
                if ethernet_info['PortChannelId'] == pc_info['PortChannelId']:
                    pc_info['Ethernet'].append(
                        ethernet_info
                    )
                    pc_info['MemberCount'] += 1
                    if ethernet_info['OperState'] == 'up':
                        pc_info['MemberUp'] += 1

            pc_info['MemberSummary'] = '%s/%s' % (
                pc_info['MemberUp'],
                pc_info['MemberCount']
            )

            self.fi_info['EthernetPortChannel'].append(
                pc_info
            )

        self.fi_info['EthernetPortChannel'] = sorted(
            self.fi_info['EthernetPortChannel'],
            key=lambda i: i['PortChannelId']
        )

    def add_common_attributes(self, fi_mo):
        keys = [
            'Dn',
            'DeviceMoId',
            'ManagementMode',
            'Moid',
            'Model',
            'Name',
            'Operability',
            'OutOfBandIpAddress',
            'OutOfBandIpGateway',
            'OutOfBandIpMask',
            'OutOfBandIpv4Address',
            'OutOfBandIpv4Gateway',
            'OutOfBandIpv4Mask',
            'OutOfBandIpv6Address',
            'OutOfBandIpv6Gateway',
            'OutOfBandIpv6Prefix',
            'OutOfBandMac',
            'PartNumber',
            'Serial',
            'SwitchId',
            'SwitchType',
            'TotalMemory',
            'Vendor'
        ]

        for key in keys:
            if key not in fi_mo:
                self.fi_info[key] = None
                continue

            if isinstance(fi_mo[key], str):
                self.fi_info[key] = fi_mo[key].strip()
                continue

            self.fi_info[key] = fi_mo[key]

        self.fi_info['ManagementIp'] = '%s/%s' % (
            self.fi_info['OutOfBandIpAddress'],
            ip_helper.netmask_to_prefix(
                self.fi_info['OutOfBandIpMask']
            )
        )

        self.fi_info['AlarmSummary'] = {}
        self.fi_info['AlarmSummary']['__Output'] = {}
        self.fi_info['AlarmSummary']['__Output']['Critical'] = 'Red'
        self.fi_info['AlarmSummary']['__Output']['Warning'] = 'Yellow'
        self.fi_info['AlarmSummary']['__Output']['Info'] = 'Blue'
        self.fi_info['AlarmSummary']['__Output']['Cleared'] = 'Green'

        for key in ['Critical', 'Warning', 'Info', 'Cleared']:
            if key in fi_mo['AlarmSummary']:
                self.fi_info['AlarmSummary'][key] = fi_mo['AlarmSummary'][key]

        self.fi_info['Health'] = 'Healthy'
        self.fi_info['__Output']['Health'] = 'Green'

        if self.fi_info['AlarmSummary']['Warning'] == 0 and self.fi_info['AlarmSummary']['Critical'] == 0:
            if 'Info' in self.fi_info['AlarmSummary'] and self.fi_info['AlarmSummary']['Info'] > 0:
                self.fi_info['Health'] = 'Healthy (%s)' % (
                    self.fi_info['AlarmSummary']['Info']
                )
                self.fi_info['__Output']['Health'] = 'Blue'

        if self.fi_info['AlarmSummary']['Warning'] > 0 and self.fi_info['AlarmSummary']['Critical'] == 0:
            self.fi_info['Health'] = 'Warnings (%s)' % (
                self.fi_info['AlarmSummary']['Warning']
            )
            self.fi_info['__Output']['Health'] = 'Yellow'

        if self.fi_info['AlarmSummary']['Critical'] > 0:
            self.fi_info['Health'] = 'Critical (%s)' % (
                self.fi_info['AlarmSummary']['Critical']
            )
            self.fi_info['__Output']['Health'] = 'Red'

        if self.fi_info['Operability'] == '':
            self.fi_info['OperabilityTick'] = '--'
        else:
            if self.fi_info['Operability'].lower() in ['operable', 'online']:
                self.fi_info['OperabilityTick'] = '\u2713'
                self.fi_info['__Output']['OperabilityTick'] = 'Green'
            else:
                self.fi_info['OperabilityTick'] = '\u2717'
                self.fi_info['__Output']['OperabilityTick'] = 'Red'

        self.fi_info['CardCount'] = len(
            fi_mo['Cards']
        )

        self.fi_info['FanModuleCount'] = len(
            fi_mo['Fanmodules']
        )

        self.fi_info['PsuCount'] = len(
            fi_mo['Psus']
        )

        self.fi_info['StorageCount'] = len(
            fi_mo['StorageItems']
        )

    def add_fi_attributes(self, fi_mo, settings):
        self.fi_info = {}
        self.fi_info['__Output'] = {}

        self.add_common_attributes(fi_mo)

        if 'summary' in settings and settings['summary']:
            self.add_summary_info()

        if 'eth' in settings and settings['eth']:
            self.add_eth_info()

        if 'pc' in settings and settings['pc']:
            self.add_pc_info()

            self.fi_info['NumPcConfigured'] = 0
            self.fi_info['NumPcUp'] = 0

            for pc_info in self.fi_info['EthernetPortChannel']:
                self.fi_info['NumPcConfigured'] += 1
                if pc_info['OperState'] == 'up':
                    self.fi_info['NumPcUp'] += 1

            self.fi_info['NumPcSummary'] = '%s/%s' % (
                self.fi_info['NumPcUp'],
                self.fi_info['NumPcConfigured']
            )

        return self.fi_info
