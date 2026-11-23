import time
import random

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

from lib.intersight.compute_cache import ComputeCache
from lib.intersight.compute_filter import ComputeFilter
from lib.intersight.computes_worfklow import ComputesWorkflow

from lib.intersight import compute_extra_attributes


class ComputeInfo(ComputeCache, ComputeFilter, ComputesWorkflow):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self):
        ComputeCache.__init__(self)
        ComputeFilter.__init__(self)
        ComputesWorkflow.__init__(self)

    def get_server_info(self, server_mo, settings, log_id=None):
        server_info_handler = compute_extra_attributes.ComputeExtraAttributes(
            self.iaccount,
            log_id=log_id
        )
        server_info = server_info_handler.get_server_info(
            server_mo,
            settings
        )
        return server_info

    def get_threaded(self, servers_mo, settings):
        start_time = int(time.time() * 1000)
        servers_info = []

        self.log_handler.debug(
            'computes_info.get_threaded',
            'Start %s threads' % (len(servers_mo))
        )

        with ProcessPoolExecutor() as executor:
            pool = [executor.submit(self.get_server_info, server_mo, settings, log_id=self.log_id) for server_mo in servers_mo]
            result = concurrent.futures.wait(
                pool,
                timeout=120,
                return_when=concurrent.futures.ALL_COMPLETED
            )
            executor.shutdown(
                wait=False,
                cancel_futures=True
            )

        self.log_handler.debug(
            'computes_info.get',
            'Completed: %s/%s/%s' % (
                len(result[0]),
                len(result[1]),
                len(servers_mo)
            )
        )

        for server_mo in servers_mo:
            server_info = self.log_handler.get_log(
                'server_info.%s' % (server_mo['Moid']),
                json_conversion=True
            )

            if server_info is None:
                self.log_handler.error(
                    'computes_info.get_server_info',
                    'No server info: %s' % (server_mo['Moid'])
                )
                continue

            servers_info.append(
                server_info
            )

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'computes_info.get_threaded',
            'Finished: %s ms' % (duration)
        )

        return servers_info

    def get_sequential(self, servers_mo, settings, bar_handler=None):
        start_time = int(time.time() * 1000)
        servers_info = []

        self.log_handler.debug(
            'compute_info.get_sequential',
            'Start'
        )

        for server_mo in servers_mo:
            server_start_time = int(time.time() * 1000)
            server_info = self.get_server_info(
                server_mo,
                settings,
                log_id=self.log_id
            )
            if server_info is None:
                self.log_handler.error(
                    'compute_info.get_sequential',
                    'No server info: %s' % (server_mo['Moid'])
                )
                continue

            servers_info.append(server_info)

            duration = int(time.time() * 1000) - server_start_time
            self.log_handler.debug(
                'computes_info.get_sequential',
                'Server %s: %s ms' % (
                    server_mo['Serial'],
                    duration
                )
            )

            if bar_handler is not None:
                bar_handler.next()

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'computes_info.get_sequential',
            'Finished: %s ms' % (duration)
        )

        return servers_info

    def get_info(self, servers_mo, settings, match_rules, cache_ttl, prepare_cache=True, parallel=False, bar_handler=None):
        if prepare_cache:
            self.set_cache(servers_mo, settings, cache_ttl)

        start_time = int(time.time() * 1000)

        if parallel:
            all_servers_info = self.get_threaded(
                servers_mo,
                settings
            )

        if not parallel:
            all_servers_info = self.get_sequential(
                servers_mo,
                settings,
                bar_handler=bar_handler
            )

        self.log_handler.debug(
            'compute_info.get_info',
            'Match rules: %s' % (match_rules)
        )

        servers_info = []
        for server_info in all_servers_info:
            matching_server_info = self.match_server(server_info, match_rules)
            if matching_server_info is not None:
                servers_info.append(
                    matching_server_info
                )

        servers_info = sorted(
            servers_info,
            key=lambda i: i['Name'].lower()
        )

        end_time = int(time.time() * 1000)
        duration = end_time - start_time

        self.log_handler.debug(
            'compute_info.get_info',
            'Selected %s/%s/%s servers in %s ms' % (len(servers_info), len(all_servers_info), len(servers_mo), duration)
        )

        return servers_info

    def anonymize_server_info(self, server_info):
        server_info['Name'] = 'Server%s' % (random.randint(100, 999))
        server_info['Moid'] = 'Moid-value'

        new_tags = []
        for tag in server_info['Tags']:
            if tag['Key'] == 'Intersight.LicenseTier':
                new_tags.append(tag)
        server_info['Tags'] = new_tags

        server_info['Serial'] = 'SN-%s' % (random.randint(10, 99))
        server_info['ManagementIp'] = '10.%s.%s.%s' % (
            random.randint(1, 254),
            random.randint(1, 254),
            random.randint(1, 254)
        )

        if 'AdaptersInfo' in server_info:
            for item in server_info['AdaptersInfo']:
                item['BaseMacAddress'] = 'aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )
                item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'AlarmInfo' in server_info:
            for item in server_info['AlarmInfo']:
                item['Description'] = '--- Anonymized ---'
                item['AffectedName'] = '--- Anonymized ---'

        if 'CimcInfo' in server_info:
            for item in server_info['CimcInfo']:
                item['IpAddress'] = '10.1.1.%s' % (random.randint(1, 253))
                item['Ipv4Address'] = item['IpAddress']
                item['HostName'] = 'hostname'
                item['Gateway'] = '10.1.1.254'
                item['Ipv4Gateway'] = item['Gateway']
                item['Mask'] = '255.255.255.0'
                item['Ipv4Mask'] = item['Mask']
                item['MacAddress'] = 'aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )

        if 'ConnectorInfo' in server_info:
            server_info['ConnectorInfo']['ClaimedByUserName'] = 'user@domain.com'
            server_info['ConnectorInfo']['ConnectorVersion'] = 'Version-Number'
            server_info['ConnectorInfo']['DeviceExternalIpAddress'] = '66.%s.%s.%s' % (
                random.randint(1, 254),
                random.randint(1, 254),
                random.randint(1, 254)
            )
            server_info['ConnectorInfo']['ClaimedTime'] = '2024-01-01T00:00:00.000Z'
            server_info['ConnectorInfo']['ConnectionStatusLastChangeTime'] = '2025-01-01T00:00:00.000Z'

        if 'ContractInfo' in server_info:
            server_info['ContractInfo']['PurchaseOrderNumber'] = 'PO%s' % (random.randint(1, 254))
            server_info['ContractInfo']['SalesOrderNumber'] = 'SO%s' % (random.randint(1, 254))
            server_info['ContractInfo']['ContractUpdatedTime'] = '2025-01-01T00:00:00.000Z'

        if 'CpuInfo' in server_info:
            for item in server_info['CpuInfo']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'ExtEthInfo' in server_info:
            for item in server_info['ExtEthInfo']:
                item['MacAddress'] = 'aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )

        if 'FanInfo' in server_info:
            for item in server_info['FanInfo']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))

        if 'FirmwarewComponents' in server_info:
            for item in server_info['FirmwarewComponents']:
                item['PackageVersion'] = '1.0(1a)'
                item['Version'] = '1.0(1a)'

        if 'FirmwareVersion' in server_info:
            server_info['FirmwareVersion'] = '1.0(1a)'

        if 'HclInfo' in server_info:
            server_info['HclInfo']['HclFirmwareVersion'] = '1.0(1a)'
            server_info['HclInfo']['HclOsVersion'] = '1.0(1a)'
            server_info['HclInfo']['HclOsVendor'] = 'OS Vendor'
            if 'Details' in server_info['HclInfo']:
                for item in server_info['HclInfo']['Details']:
                    item['HclCimcVersion'] = '1.0(1a)'
                    item['HclDriverVersion'] = '1.0(1a)'
                    item['HclDriverName'] = 'driver-name'
                    item['HclFirmwareVersion'] = '1.0(1a)'

        if 'HostEthInfo' in server_info:
            for item in server_info['HostEthInfo']:
                item['Name'] = 'Name-%s' % (random.randint(10, 99))
                item['MacAddress'] = 'aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )

        if 'HostFcInfo' in server_info:
            for item in server_info['HostFcInfo']:
                item['Wwnn'] = '10:10:aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )
                item['Wwpn'] = '20:20:aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )

        if 'Inventory' in server_info:
            for item in server_info['Inventory']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['Model'] = '--- Anonymized ---'
                item['ServerSerial'] = 'SN-%s' % (random.randint(10, 99))

        if 'KvmInfo' in server_info:
            server_info['KvmInfo']['KvmVendor'] = 'Vendor'
            if 'KvmIpAddresses' in server_info['KvmInfo']:
                for item in server_info['KvmInfo']['KvmIpAddresses']:
                    item['Address'] = '10.1.1.%s' % (random.randint(1, 253))
                    item['DefaultGateway'] = '10.1.1.254'
                    item['Subnet'] = '255.255.255.0'

        if 'MacAddressInfo' in server_info:
            for item in server_info['MacAddressInfo']:
                item['MacAddress'] = 'aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )

        if 'MemoryInfo' in server_info:
            for item in server_info['MemoryInfo']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['Model'] = 'Model-%s' % (random.randint(10, 99))

        if 'PciDevicesInfo' in server_info:
            for item in server_info['PciDevicesInfo']:
                item['FirmwareVersion'] = '1.0(1a)'
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'PhysicalDiskInfo' in server_info:
            for item in server_info['PhysicalDiskInfo']:
                item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['Pid'] = 'PID-%s' % (random.randint(10, 99))
                item['Model'] = 'Model-XYZ'
                item['DriveFirmware'] = '1.0(1a)'

        if 'Power' in server_info:
            if 'Data' in server_info['Power']:
                if 'PowerSupply' in server_info['Power']['Data']:
                    for item in server_info['Power']['Data']['PowerSupply']:
                        item['SerialNumber'] = 'SN-%s' % (random.randint(10, 99))
                        item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
                        item['PartSparePartNumberNumber'] = 'SPN-%s' % (random.randint(10, 99))
                        item['FirmwareVersion'] = 'Version-%s' % (random.randint(10, 99))

        if 'ProfileInfo' in server_info and server_info['ProfileInfo'] is not None:
            server_info['ProfileInfo']['Name'] = 'profile'
            server_info['ProfileInfo']['ModTime'] = '2025-01-01T00:00:00.000Z'
            if 'Policies' in server_info['ProfileInfo']:
                for item in server_info['ProfileInfo']['Policies']:
                    item['Name'] = 'Name-%s' % (random.randint(10, 99))
                    item['ModTime'] = '2025-01-01T00:00:00.000Z'

        if 'PsuInfo' in server_info:
            for item in server_info['PsuInfo']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'StorageControllerInfo' in server_info:
            for item in server_info['StorageControllerInfo']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'TpmInfo' in server_info:
            for item in server_info['TpmInfo']:
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['FirmwareVersion'] = 'Version-%s' % (random.randint(10, 99))
                item['Version'] = 'Version-%s' % (random.randint(10, 99))

        return server_info
