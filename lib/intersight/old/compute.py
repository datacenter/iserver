import time

from lib import ip_helper
from lib import log_helper

from lib.intersight import cache as intersight_cache
from lib.intersight.compute_extra_attributes import ComputeExtraAttributes
from lib.intersight import compute_rack
from lib.intersight import compute_blade


class Compute(ComputeExtraAttributes):
    def __init__(self, iaccount, log_id=None):
        ComputeExtraAttributes.__init__(self, iaccount, log_id=log_id)
        self.log_handler = log_helper.Log(log_id=log_id)
        self.rack_handler = compute_rack.ComputeRack(iaccount, log_id=log_id)
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )
        self.iaccount = iaccount

    def get_management_ip(self, server_mo):
        if 'KvmIpAddresses' in server_mo:
            for kvm_ip in server_mo['KvmIpAddresses']:
                if kvm_ip['ClassId'] == 'compute.IpAddress':
                    return kvm_ip['Address']
        return None

    def get_mo(self, match_rules=None, include_rack=False, include_blade=False, cache_ttl=None):
        servers_mo = []

        if include_rack:
            rack_servers = None
            if cache_ttl is not None:
                rack_servers = self.cache_handler.get_intersight_cache_entry(
                    'inventory.rack.%s' % (self.iaccount),
                    cache_ttl=cache_ttl
                )

            if rack_servers is None:
                rack_servers = self.rack_handler.get_all()
                self.cache_handler.set_intersight_cache_entry(
                    'inventory.rack.%s' % (self.iaccount),
                    rack_servers
                )

            if rack_servers is not None:
                servers_mo = servers_mo + rack_servers

        if include_blade:
            blade_servers = None
            if cache_ttl is not None:
                blade_servers = self.cache_handler.get_intersight_cache_entry(
                    'inventory.blade.%s' % (self.iaccount),
                    cache_ttl=cache_ttl
                )

            if blade_servers is None:
                blade_servers = self.blade_handler.get_all()
                self.cache_handler.set_intersight_cache_entry(
                    'inventory.blade.%s' % (self.iaccount),
                    blade_servers
                )

            if blade_servers is not None:
                servers_mo = servers_mo + blade_servers

        selected_servers_mo = []
        for server_mo in servers_mo:
            server_mo['ManagementIp'] = self.get_management_ip(server_mo)
            if self.match_server(server_mo, match_rules):
                selected_servers_mo.append(server_mo)

        return selected_servers_mo

    def set_cache(self, servers_mo, cache_settings, cache_ttl, parallel=False):
        start_time = int(time.time() * 1000)
        self.log.debug(
            'compute.set_cache',
            'Start cache population'
        )

        moids = []
        serial = {}
        device_moids = {}
        registration_moids = {}
        board_moids = {}
        adapter_moids = {}
        boot_moids = {}

        for server_mo in servers_mo:
            moids.append(server_mo['Moid'])
            serial[server_mo['Moid']] = server_mo['Serial']
            device_moids[server_mo['Moid']] = server_mo['DeviceMoId']
            registration_moids[server_mo['Moid']] = server_mo['RegisteredDevice']['Moid']
            board_moids[server_mo['Moid']] = server_mo['Board']['Moid']

            adapter_moids[server_mo['Moid']] = []
            for adapter_mo in server_mo['Adapters']:
                adapter_moids[server_mo['Moid']].append(
                    adapter_mo['Moid']
                )

            boot_moids[server_mo['Moid']] = {}

            boot_moids[server_mo['Moid']]['cdd'] = []
            for item in server_mo['BootCddDevices']:
                boot_moids[server_mo['Moid']]['cdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['cdd'] = []
            for item in server_mo['BootCddDevices']:
                boot_moids[server_mo['Moid']]['cdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['cdd'] = []
            for item in server_mo['BootCddDevices']:
                boot_moids[server_mo['Moid']]['cdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['hdd'] = []
            for item in server_mo['BootHddDevices']:
                boot_moids[server_mo['Moid']]['hdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['iscsi'] = []
            for item in server_mo['BootIscsiDevices']:
                boot_moids[server_mo['Moid']]['iscsi'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['nvme'] = []
            for item in server_mo['BootNvmeDevices']:
                boot_moids[server_mo['Moid']]['nvme'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['pxe'] = []
            for item in server_mo['BootPxeDevices']:
                boot_moids[server_mo['Moid']]['pxe'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['san'] = []
            for item in server_mo['BootSanDevices']:
                boot_moids[server_mo['Moid']]['san'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['sd'] = []
            for item in server_mo['BootSdDevices']:
                boot_moids[server_mo['Moid']]['sd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['uefi'] = []
            for item in server_mo['BootUefiShellDevices']:
                boot_moids[server_mo['Moid']]['uefi'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['usb'] = []
            for item in server_mo['BootUsbDevices']:
                boot_moids[server_mo['Moid']]['usb'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['vmedia'] = []
            for item in server_mo['BootVmediaDevices']:
                boot_moids[server_mo['Moid']]['vmedia'].append(
                    item['Moid']
                )

        keys = []

        if cache_settings['board']:
            keys.append('board')

        if cache_settings['cpu']:
            keys.append('cpu')

        if cache_settings['gpu']:
            keys.append('gpu')

        if cache_settings['fan']:
            keys.append('fanmodule')

        if cache_settings['memory']:
            keys.append('memory')

        if cache_settings['pci']:
            keys.append('pci')

        if cache_settings['net']:
            keys.append('adapter')
            keys.append('adapter_ext_eth_interface')
            keys.append('adapter_host_eth_interface')
            keys.append('adapter_host_fc_interface')

        if cache_settings['psu']:
            keys.append('psu')

        if cache_settings['storage']:
            keys.append('storage_controller')
            keys.append('virtual_drive')
            keys.append('physical_disk')

        if cache_settings['fw']:
            keys.append('firmware')

        if cache_settings['boot']:
            keys.append('boot_bios')
            keys.append('boot_mode')
            keys.append('boot_security')
            keys.append('boot_hdd')
            keys.append('boot_cdd')
            keys.append('boot_iscsi')
            keys.append('boot_nvme')
            keys.append('boot_pxe')
            keys.append('boot_san')
            keys.append('boot_sd')
            keys.append('boot_uefi')
            keys.append('boot_usb')
            keys.append('boot_vmedia')

        if cache_settings['advisory']:
            keys.append('advisory')
            self.set_intersight_cache(
                'advisories',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if cache_settings['alarm']:
            keys.append('alarm')

        if cache_settings['connector']:
            keys.append('connector')

        if cache_settings['contract']:
            keys.append('contract')

        if cache_settings['hcl']:
            keys.append('hcl')

        if cache_settings['profile']:
            keys.append('profile')

        # if cache_settings['locator']:
        #     keys.append('locator_led')

        if cache_settings['workflow'] is not None:
            keys.append('workflow')
            self.set_intersight_cache(
                'workflows',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if len(keys) > 0:
            for key in keys:
                self.set_intersight_cache(
                    key,
                    moids,
                    device_moids,
                    registration_moids,
                    board_moids,
                    adapter_moids,
                    boot_moids,
                    serial,
                    cache_settings['workflow'],
                    cache_ttl=cache_ttl
                )

        if cache_settings['hcl']:
            self.set_intersight_cache(
                'hcl_detail',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if cache_settings['storage']:
            self.set_intersight_cache(
                'physical_disk_usage',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if cache_settings['tpm']:
            self.set_intersight_cache(
                'tpm',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        for server_mo in servers_mo:
            if cache_settings['power']:
                if server_mo['ManagementMode'] == 'UCSM':
                    if self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(server_mo['Serial']):
                        server_serial = {}
                        server_serial[server_mo['Moid']] = server_mo['Serial']
                        self.set_redfish_cache(
                            'power-ucsm',
                            moids,
                            server_serial,
                            cache_ttl=cache_ttl
                        )

                if server_mo['ManagementMode'] != 'UCSM':
                    if self.redfish_endpoint_settings_handler.is_redfish_endpoint(server_mo['Serial']):
                        server_serial = {}
                        server_serial[server_mo['Moid']] = server_mo['Serial']
                        self.set_redfish_cache(
                            'power',
                            moids,
                            server_serial,
                            cache_ttl=cache_ttl
                        )

            if cache_settings['thermal']:
                if server_mo['OperPowerState'] == 'on':
                    if server_mo['ManagementMode'] == 'UCSM':
                        if self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(server_mo['Serial']):
                            server_serial = {}
                            server_serial[server_mo['Moid']] = server_mo['Serial']
                            self.set_redfish_cache(
                                'thernal-ucsm',
                                moids,
                                server_serial,
                                cache_ttl=cache_ttl
                            )

                    if server_mo['ManagementMode'] != 'UCSM':
                        if self.redfish_endpoint_settings_handler.is_redfish_endpoint(server_mo['Serial']):
                            server_serial = {}
                            server_serial[server_mo['Moid']] = server_mo['Serial']
                            self.set_redfish_cache(
                                'thermal',
                                moids,
                                server_serial,
                                cache_ttl=cache_ttl
                            )

        duration = int(time.time() * 1000) - start_time
        self.log.debug(
            'compute.set_cache',
            'Cache populated in %s ms' % (duration)
        )

    # def get_threaded(self, base_servers, match_rules, cache_enabled, include_object=False):
    #     start_time = int(time.time() * 1000)
    #     servers = []

    #     self.log.debug(
    #         'computes_info.get_threaded',
    #         'Start %s threads' % (len(base_servers))
    #     )

    #     with ProcessPoolExecutor() as executor:
    #         pool = [executor.submit(self.get_server_info, server, log_id=self.log_id, cache_enabled=cache_enabled, include_object=include_object) for server in base_servers]
    #         result = concurrent.futures.wait(
    #             pool,
    #             timeout=120,
    #             return_when=concurrent.futures.ALL_COMPLETED
    #         )
    #         executor.shutdown(
    #             wait=False,
    #             cancel_futures=True
    #         )

    #     self.log.debug(
    #         'computes_info.get',
    #         'Completed: %s/%s/%s' % (
    #             len(result[0]),
    #             len(result[1]),
    #             len(base_servers)
    #         )
    #     )

    #     for server in base_servers:
    #         server_info = self.log.get_log(
    #             'server_info.%s' % (server['Moid']),
    #             json_conversion=True
    #         )

    #         if server_info is None:
    #             self.log.error(
    #                 'computes_info.get_server_info',
    #                 'No server info: %s' % (server['Moid'])
    #             )

    #         if server_info is not None:
    #             if self.match_server(server_info, match_rules, base_match=False):
    #                 servers.append(server_info)

    #     duration = int(time.time() * 1000) - start_time
    #     self.log.debug(
    #         'computes_info.get_threaded',
    #         'Finished: %s ms' % (duration)
    #     )

    #     return servers

    def get_sequential(self, servers_mo, settings):
        start_time = int(time.time() * 1000)
        servers_info = []

        self.log.debug(
            'compute.get_sequential',
            'Start'
        )

        for server_mo in servers_mo:
            server_start_time = int(time.time() * 1000)
            server_info = self.get_server_info(
                server_mo,
                settings
            )
            if server_info is None:
                continue

            servers_info.append(
                server_info
            )
            duration = int(time.time() * 1000) - server_start_time
            self.log.debug(
                'compute.get_sequential',
                'Server %s: %s ms' % (
                    server_mo['Moid'],
                    duration
                )
            )

        duration = int(time.time() * 1000) - start_time
        self.log.debug(
            'compute.get_sequential',
            'Finished: %s ms' % (duration)
        )

        return servers_info

    def get_info(self, servers_mo, settings, cache_ttl, parallel=False):
        self.set_cache(servers_mo, settings, cache_ttl, parallel=parallel)

        servers = None

        # if parallel:
        #     servers = self.get_threaded(
        #         base_servers,
        #         match_rules,
        #         cache_enabled,
        #         include_object=include_object
        #     )

        if not parallel:
            servers = self.get_sequential(
                servers_mo,
                settings
            )

        return servers
