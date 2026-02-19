import copy
import sys
from lib import ip_helper
from lib.nexus import helper as nexus_helper
from lib.vc import vcenter
from lib.vc import helper as vc_helper


class VcHost():
    def __init__(self):
        self.vc_host = None
        self.vc_serials = None
        self.vc_serial_to_host = None
        self.vc_mac_to_pnic = None

    def load_pre_vc_host(self):
        self.vc_host = self.get_pre_cache('vcenter', 'host')
        if self.vc_host is None:
            return False

        self.prepare_vc_host_mappings()
        self.prepare_vc_serials()
        return True

    def set_post_vc_host(self):
        return self.set_post_cache('vcenter-host', self.vc_host)

    def load_post_vc_host(self):
        self.vc_host = self.get_post_cache('vcenter-host')
        if self.vc_host is None:
            return False

        self.prepare_vc_host_mappings()
        self.prepare_vc_serials()
        return True

    def get_vc_host_name_short(self, name):
        if name is None:
            return None

        # Reconsider
        return name

    def get_vc_host(self, vc):
        if vc in self.vc_host:
            info = copy.deepcopy(self.vc_host[vc])
            return info

        return None

    def get_vc_host_by_name(self, vc, hostname):
        for host in self.vc_host[vc]:
            if host['name'] == hostname:
                return host

        return None

    def get_vc_host_pnic_in_dvs(self, vc, hostname, dvsname):
        host = self.get_vc_host_by_name(vc, hostname)
        if host is None:
            return None

        if 'pnet' not in host:
            return None

        if 'dvswitch' not in host['pnet']:
            return None

        for dvs in host['pnet']['dvswitch']:
            if dvs['name'] == dvsname:
                return dvs['pnic']

        return None

    def get_vc_host_by_serial(self, serial):
        if serial.lower() not in self.vc_serial_to_host:
            return None
        return self.vc_serial_to_host[serial.lower()]

    def get_vc_pnic_by_mac(self, mac):
        for key in self.vc_mac_to_pnic:
            if ip_helper.is_mac_equal(key, mac):
                return self.vc_mac_to_pnic[key]
        return None

    def prepare_vc_host_mappings(self):
        self.vc_serial_to_host = {}
        self.vc_mac_to_pnic = {}
        for vc_instance in self.vc_host:
            for host in self.vc_host[vc_instance]:
                self.vc_serial_to_host[host['serial'].lower()] = host
                self.vc_serial_to_host[host['serial'].lower()]['vc_instance'] = vc_instance
                if host['pnet'] is not None:
                    if 'pnic' in host['pnet'] and host['pnet']['pnic'] is not None:
                        for pnic in host['pnet']['pnic']:
                            info = {}
                            info['vc'] = vc_instance
                            info['host'] = host['name']
                            info['device'] = pnic['device']
                            info['uplink'] = pnic['uplink']
                            self.vc_mac_to_pnic[pnic['mac']] = info

    def prepare_vc_serials(self):
        self.vc_serials = {}
        for vc_instance in self.vc_host:
            self.vc_serials[vc_instance] = []
            for host in self.vc_host[vc_instance]:
                self.vc_serials[vc_instance].append(
                    host['serial']
                )

    def prepare_vc_hosts(self, cache_enabled=True):
        vc_instances = self.get_vc_handlers()
        if vc_instances is None or len(vc_instances) == 0:
            return False

        self.vc_host = {}

        for vc_instance in vc_instances:
            self.my_output.debug('Vcenter hosts: %s' % (vc_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if vc_instance['name'] in self.vc_host:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('vcenter-%s-host' % (vc_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.vc_host[vc_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            vc_handler = vcenter.Vcenter(
                vc_instance['ip'],
                vc_instance['username'],
                vc_instance['password'],
                port=vc_instance['port'],
                log_id=self.log_id
            )

            self.vc_host[vc_instance['name']] = vc_handler.get_hosts_summary()
            if self.vc_host[vc_instance['name']] is None:
                return False

            for vc_host in self.vc_host[vc_instance['name']]:
                self.my_output.debug('- host %s' % (vc_host['name']))
                vc_host['pnet'] = None
                if vc_host['runtime']['connectionState'] =='connected':
                    vc_host['pnet'] = vc_handler.get_host_networking(
                        vc_handler.get_hosts_by_name(
                            vc_host['name']
                        )[0]
                    )

            self.set_cache(
                'vcenter-%s-host' % (vc_instance['name']),
                self.vc_host[vc_instance['name']]
            )

        self.prepare_vc_host_mappings()
        self.prepare_vc_serials()
        return True

    def is_vc_host_up(self, host):
        up = True
        if host['runtime']['powerState'] != 'poweredOn':
            up = False
        if host['runtime']['connectionState'] != 'connected':
            up = False
        return up

    def run_vc_host_base(self, vc, host):
        host['vcenter'] = vc
        host['_name'] = self.get_vc_host_name_short(host['name'])
        host['_hypervisor'] = vc_helper.get_hypervisor_version(host['hypervisor'], short=True)
        host['_uptime'] = vc_helper.get_uptime(host['stats']['uptime'])
        host['up'] = self.is_vc_host_up(host)
        host['_ready'] = True
        if host['runtime']['powerState'] != 'poweredOn':
            host['_ready'] = False
        if host['runtime']['connectionState'] != 'connected':
            host['_ready'] = False

        host['clusterName'] = None
        if host['name'] in self.vc_host_to_cluster:
            host['clusterName'] = self.vc_host_to_cluster[host['name']]

        if 'pnet' in host and host['pnet'] is not None:
            for pnic in host['pnet']['pnic']:
                pnic['_name'] = pnic['device']
                pnic['hash'] = ip_helper.get_string_md5(
                    '%s %s %s' % (
                        vc,
                        host['name'],
                        pnic['device']
                    )
                )

            for vnic in host['pnet']['vnic']:
                vnic['_name'] = vnic['device']
                vnic['hash'] = ip_helper.get_string_md5(
                    '%s %s %s' % (
                        vc,
                        host['name'],
                        vnic['device']
                    )
                )

            for vswitch in host['pnet']['vswitch']:
                vswitch['_name'] = vswitch['name']
                vswitch['hash'] = ip_helper.get_string_md5(
                    '%s %s %s' % (
                        vc,
                        host['name'],
                        vswitch['name']
                    )
                )

            for vswitch in host['pnet']['dvswitch']:
                vswitch['_name'] = vswitch['name']
                vswitch['hash'] = ip_helper.get_string_md5(
                    '%s %s %s' % (
                        vc,
                        host['name'],
                        vswitch['name']
                    )
                )

            # Step: Add vswitch info per pnic
            for pnic in host['pnet']['pnic']:
                pnic['vswitch'] = None
                pnic['vswitch_hash'] = None
                pnic['vswitch_type'] = None

                for vswitch in host['pnet']['vswitch']:
                    for vpnic in vswitch['pnic']:
                        if vpnic['key'] == pnic['key']:
                            if pnic['vswitch'] is not None:
                                print('Panic as switch should be part of single vswitch')
                                sys.exit(1)

                            pnic['vswitch'] = vswitch['name']
                            pnic['vswitch_hash'] = vswitch['hash']
                            pnic['vswitch_type'] = 'switch'

                for dvswitch in host['pnet']['dvswitch']:
                    for dvpnic in dvswitch['pnic']:
                        if dvpnic['device'] == pnic['key'].split('-')[-1]:
                            if pnic['vswitch'] is not None:
                                print('Panic')
                                sys.exit(1)

                            pnic['vswitch'] = dvswitch['name']
                            pnic['vswitch_hash'] = dvswitch['hash']
                            pnic['vswitch_type'] = 'dvs'

            # Step: Add pnic info per dvs
            for vswitch in host['pnet']['dvswitch']:
                vswitch['numUplinks'] = 0
                vswitch['numUplinksUp'] = 0
                for item in vswitch['pnic']:
                    for pnic in host['pnet']['pnic']:
                        if item['device'] == pnic['device']:
                            item['_info'] = pnic
                            vswitch['numUplinks'] += 1
                            if pnic['up']:
                                vswitch['numUplinksUp'] += 1

            # Step: Add pnic info per vswitch
            for vswitch in host['pnet']['vswitch']:
                vswitch['numUplinks'] = 0
                vswitch['numUplinksUp'] = 0
                for item in vswitch['pnic']:
                    for pnic in host['pnet']['pnic']:
                        if item['key'] == pnic['key']:
                            item['_info'] = pnic
                            vswitch['numUplinks'] += 1
                            if pnic['up']:
                                vswitch['numUplinksUp'] += 1

        host['hash'] = ip_helper.get_string_md5(
            '%s %s' % (
                vc,
                host['name']
            )
        )

        return host

    def run_vc_host_server(self, vc, host):
        host['ServerMoid'] = None
        host['ServerName'] = None
        host['ServerType'] = None
        host['ServerFabric'] = []
        for server in self.servers:
            if server['Serial'].lower() != host['serial'].lower():
                continue

            host['ServerMoid'] = server['Moid']
            host['ServerName'] = server['Name']
            host['ServerType'] = server['Type']

            keys = [
                'InterfaceDn',
                'InterfaceName',
                'MacAddress',
                'AdapterModel',
                'AdapterPciSlot',
                'intf'
            ]
            for fabric in server['Fabric']:
                finfo = {}

                for key in keys:
                    finfo[key] = fabric[key]

                finfo['vmnic'] = None
                if 'pnet' not in host or host['pnet'] is None:
                    continue

                for pnic in host['pnet']['pnic']:
                    if ip_helper.is_mac_equal(pnic['mac'], finfo['MacAddress']):
                        finfo['vmnic'] = pnic['device']
                        finfo['_name'] = pnic['device']
                        finfo['hash'] = ip_helper.get_string_md5(
                            '%s %s %s' % (
                                vc,
                                host['name'],
                                pnic['device']
                            )
                        )

                host['ServerFabric'].append(
                    finfo
                )

        if 'pnet' in host and host['pnet'] is not None:
            for pnic in host['pnet']['pnic']:
                pnic['server'] = None
                for server_mac in self.server_macs:
                    if ip_helper.is_mac_equal(pnic['mac'], server_mac['MacAddress']):
                        pnic['server'] = server_mac

        return host

    def run_vc_host_nexus(self, host):
        if 'pnet' not in host or host['pnet'] is None:
            return host

        # Step: Add nei switch info per pnic
        for pnic in host['pnet']['pnic']:
            keys = [
                'switch_system_name',
                'switch_port'
            ]
            for key in keys:
                if key not in pnic:
                    pnic[key] = None

            pnic['switch_fabric_type'] = None
            pnic['switch_port_hash'] = None
            pnic['switch_apic'] = None

            if pnic['switch_system_name'] is not None:
                # drop domain name
                pnic['switch_system_name'] = pnic['switch_system_name'].split('.')[0]

                if self.is_nexus_device_name(pnic['switch_system_name']):
                    pnic['switch_fabric_type'] = 'Nexus'
                    pnic['switch_port_hash'] = nexus_helper.get_nexus_interface_hash(
                        pnic['switch_system_name'],
                        pnic['switch_port']
                    )

                if self.is_aci_node_name(pnic['switch_system_name']):
                    node_info = self.get_aci_node_by_name(pnic['switch_system_name'])
                    pnic['switch_fabric_type'] = 'ACI'
                    pnic['switch_apic'] = node_info['apic']

        return host

    def run_vc_host_independent(self):
        for vc_instance in self.vc_host:
            for host in self.vc_host[vc_instance]:
                host = self.run_vc_host_base(vc_instance, host)
                host = self.run_vc_host_server(vc_instance, host)
                host = self.run_vc_host_nexus(host)

        return True

    def run_vc_host_vm(self, vc, host):
        host['vm_up'] = 0
        host['vm'] = []
        for vm in self.vc_vm[vc]:
            if vm['host'] == host['name']:
                host['vm'].append(
                    vm
                )
                if vm['up']:
                    host['vm_up'] += 1

        host['vm_count'] = len(host['vm'])
        host['vm_summary'] = '%s/%s' % (
            host['vm_up'],
            host['vm_count']
        )

        return host

    def run_vc_host_network(self, vc, host):
        host['network'] = []
        host['networkUpName'] = []
        for network in self.vc_network[vc]:
            if host['name'] in network['host']:
                host['network'].append(
                    network
                )
                if network['up']:
                    host['networkUpName'].append(
                        network['name']
                    )

        # Step: add per-host network vm names
        for network in host['network']:
            network['hostVmName'] = []
            network['hostVmUpName'] = []
            for vm_name in network['vm']:
                for vm in host['vm']:
                    if vm['name'] == vm_name:
                        network['hostVmName'].append(
                            vm['name']
                        )
                        if self.vc_vm_dict[vc][vm['name']]['up']:
                            network['hostVmUpName'].append(
                                vm['name']
                            )

        if 'pnet' in host and host['pnet'] is not None:
            # Step: Add network and vm info per dvs
            for vswitch in host['pnet']['dvswitch']:
                vswitch['networkName'] = []
                vswitch['networkUpName'] = []
                vswitch['vmName'] = []
                vswitch['vmUpName'] = []
                vswitch['networkVm'] = {}
                vswitch['networkVmUp'] = {}
                vswitch['networkNonEmptyName'] = []
                vswitch['networkNoneEmptyUpName'] = []
                for net in host['network']:
                    if net['type'] == 'dvs' and net['dvsName'] == vswitch['name']:
                        vswitch['networkName'].append(
                            net['name']
                        )
                        if net['name'] in host['networkUpName']:
                            vswitch['networkUpName'].append(
                                net['name']
                            )

                        vswitch['networkVm'][net['name']] = []
                        vswitch['networkVmUp'][net['name']] = []

                        for vm_name in net['hostVmName']:
                            if vm_name not in vswitch['vmName']:
                                vswitch['vmName'].append(
                                    vm_name
                                )

                        for vm_name in net['hostVmUpName']:
                            if vm_name not in vswitch['vmUpName']:
                                vswitch['vmUpName'].append(
                                    vm_name
                                )

                for vm_name in vswitch['vmName']:
                    for vm in self.vc_vm[vc]:
                        if vm['name'] == vm_name:
                            for nic in vm['nic']:
                                if nic['networkName'] in vswitch['networkName']:
                                    if vm['name'] not in vswitch['networkVm'][nic['networkName']]:
                                        vswitch['networkVm'][nic['networkName']].append(
                                            vm['name']
                                        )
                                    if vm['up'] and vm['name'] not in vswitch['networkVm'][nic['networkName']]:
                                        vswitch['networkVmUp'][nic['networkName']].append(
                                            vm['name']
                                        )

                for network_name in vswitch['networkVm']:
                    if len(vswitch['networkVm'][network_name]) > 0:
                        vswitch['networkNonEmptyName'].append(
                            network_name
                        )
                        if network_name in vswitch['networkUpName']:
                            vswitch['networkNoneEmptyUpName'].append(
                                network_name
                            )

        return host

    def run_vc_host_xd(self):
        for vc in self.vc_host:
            for host in self.vc_host[vc]:
                host = self.run_vc_host_vm(vc, host)
                host = self.run_vc_host_network(vc, host)

                if host['pnet'] is None:
                    continue

                # Step: Assess dvs up state
                for vswitch in host['pnet']['dvswitch']:
                    vswitch['up'] = True
                    if len(vswitch['pnic']) == 0:
                        vswitch['up'] = False
                    if len(vswitch['pnic']) > 0 and vswitch['numUplinksUp'] == 0:
                        vswitch['up'] = False

                # Step: Add network and vm info per vswitch
                for vswitch in host['pnet']['vswitch']:
                    vswitch['networkName'] = []
                    vswitch['networkUpName'] = []
                    vswitch['vmName'] = []
                    vswitch['vmUpName'] = []
                    vswitch['networkVm'] = {}
                    vswitch['networkVmUp'] = {}
                    # for net in host['network']:
                    #     if net['type'] == 'standard' and net['dvsName'] == vswitch['name']:
                    #         vswitch['networkName'].append(
                    #             net['name']
                    #         )
                    #         if net['name'] in host['networkUpName']:
                    #             vswitch['networkUpName'].append(
                    #                 net['name']
                    #             )

                    #         vswitch['networkVm'][net['name']] = []
                    #         vswitch['networkVmUp'][net['name']] = []

                    #         for vm_name in net['hostVmName']:
                    #             if vm_name not in vswitch['vmName']:
                    #                 vswitch['vmName'].append(
                    #                     vm_name
                    #                 )

                    #         for vm_name in net['hostVmUpName']:
                    #             if vm_name not in vswitch['vmUpName']:
                    #                 vswitch['vmUpName'].append(
                    #                     vm_name
                    #                 )

                    # for vm_name in vswitch['vmName']:
                    #     for vm in self.vc_vm[vc]:
                    #         if vm['name'] == vm_name:
                    #             for nic in vm['nic']:
                    #                 if nic['networkName'] in vswitch['networkName']:
                    #                     if vm['name'] not in vswitch['networkVm'][nic['networkName']]:
                    #                         vswitch['networkVm'][nic['networkName']].append(
                    #                             vm['name']
                    #                         )
                    #                     if vm['up'] and vm['name'] not in vswitch['networkVm'][nic['networkName']]:
                    #                         vswitch['networkVmUp'][nic['networkName']].append(
                    #                             vm['name']
                    #                         )

                # Step: Assess vswitch up state
                for vswitch in host['pnet']['vswitch']:
                    vswitch['up'] = True
                    if len(vswitch['pnic']) == 0:
                        vswitch['up'] = False
                    if len(vswitch['pnic']) > 0 and vswitch['numUplinksUp'] != len(vswitch['pnic']):
                        vswitch['up'] = False
                    if len(vswitch['networkName']) != len(vswitch['networkUpName']):
                        vswitch['up'] = False

                # Step: Assess vnic up state
                for vnic in host['pnet']['vnic']:
                    vnic['up'] = True

                # Sort

                host['pnet']['dvswitch'] = sorted(
                    host['pnet']['dvswitch'],
                    key=lambda i: i['name']
                )
                for switch in host['pnet']['dvswitch']:
                    switch['pnic'] = sorted(
                        switch['pnic'],
                        key=lambda i: i['uplinkId']
                    )
                    switch['vmName'] = sorted(
                        switch['vmName'],
                        key=lambda i: i.lower()
                    )
                    switch['networkName'] = sorted(
                        switch['networkName'],
                        key=lambda i: i.lower()
                    )

        if not self.set_post_vc_host():
            return False

        return True
