import copy
from lib import file_helper
from lib import ip_helper
from lib.vc import vcenter


class VcVm():
    def __init__(self):
        self.vc_vm = None
        self.vc_vm_dict = None

    def load_pre_vc_vm(self):
        self.vc_vm = self.get_pre_cache('vcenter', 'vm')
        if self.vc_vm is None:
            return False

        return True

    def set_post_vc_vm(self):
        return self.set_post_cache('vcenter-vm', self.vc_vm)

    def load_post_vc_vm(self):
        self.vc_vm = self.get_post_cache('vcenter-vm')
        if self.vc_vm is None:
            return False

        self.prepare_vc_vm_mappings()
        return True

    def get_vc_vm(self, vc):
        if vc in self.vc_vm:
            info = copy.deepcopy(self.vc_vm[vc])
            return info

        return None

    def prepare_vc_vms(self, cache_enabled=True):
        vc_instances = self.get_vc_handlers()
        if vc_instances is None or len(vc_instances) == 0:
            return False

        self.vc_vm = {}

        for vc_instance in vc_instances:
            self.my_output.debug('Vcenter vms: %s' % (vc_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if vc_instance['name'] in self.vc_vm:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('vcenter-%s-vm' % (vc_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.vc_vm[vc_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            vc_handler = vcenter.Vcenter(
                vc_instance['ip'],
                vc_instance['username'],
                vc_instance['password'],
                port=vc_instance['port'],
                log_id=self.log_id
            )

            self.vc_vm[vc_instance['name']] = vc_handler.get_vms()

            self.set_cache(
                'vcenter-%s-vm' % (vc_instance['name']),
                self.vc_vm[vc_instance['name']]
            )

        return True

    def is_vc_vm_up(self, vm):
        if vm['powerState'] == 'poweredOn' and vm['connectionState'] == 'connected':
            return True
        return False

    def prepare_vc_vm_mappings(self):
        self.vc_vm_dict = {}
        for vc in self.vc_host:
            if vc not in self.vc_vm_dict:
                self.vc_vm_dict[vc] = {}

            for vm in self.vc_vm[vc]:
                self.vc_vm_dict[vc][vm['name']] = vm

    def run_vc_vm(self):
        for vc in self.vc_vm:
            for vm in self.vc_vm[vc]:
                vm['_name'] = vm['name']
                vm['vcenter'] = vc
                vm['clusterName'] = None
                vm['_host'] = self.get_vc_host_name_short(vm['host'])

                vm['Server'] = {}
                vm['Server']['Name'] = None
                vm['Server']['Moid'] = None
                vm['Server']['Type'] = None

                for host in self.vc_host[vc]:
                    if host['name'] == vm['host']:
                        vm['Server']['Name'] = host['ServerName']
                        vm['Server']['Moid'] = host['ServerMoid']
                        vm['Server']['Type'] = host['ServerType']

                vm['host_hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        vc,
                        vm['name']
                    )
                )

                vm['cluster_hash'] = None
                if vm['host'] in self.vc_host_to_cluster:
                    vm['clusterName'] = self.vc_host_to_cluster[vm['host']]
                    for cluster in self.vc_cluster[vc]:
                        if cluster['name'] == vm['clusterName']:
                            vm['cluster_hash'] = ip_helper.get_string_md5(
                                '%s %s' % (
                                    vc,
                                    cluster['name']
                                )
                            )

                vm['up'] = self.is_vc_vm_up(vm)

                vm['host_hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        vc,
                        vm['host']
                    )
                )
                vm['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        vc,
                        vm['name']
                    )
                )

                if 'disk' not in vm or vm['disk'] is None:
                    vm['disk'] = []

                if 'nic' not in vm or vm['nic'] is None:
                    vm['nic'] = []

                for nic in vm['nic']:
                    nic['hash'] = ip_helper.get_string_md5(
                        '%s %s %s' % (
                            vc,
                            vm['name'],
                            nic['label']
                        )
                    )

                    nic['fabric'] = self.run_vc_vm_fabric(
                        vc,
                        vm,
                        nic
                    )

        self.prepare_vc_vm_mappings()
        if not self.set_post_vc_vm():
            return False

        return True

    def add_vc_vmware_error(self, info, reason, vm):
        info['collected'] = False
        info['reason'] = reason
        self.log.error(
            'run_vc_vm_fabric',
            '%s (vm:%s)' % (reason, vm['name'])
        )
        return info

    def add_vc_vm_vmware_info(self, info, vc, vm, nic):
        info['vmware'] = {}
        info['vmware']['host'] = vm['host']

        if nic['networkName'] is None:
            return self.add_vc_vmware_error(info, 'No network name defined', vm)

        network = self.get_vc_network_by_name(
            vc,
            nic['networkName']
        )
        if network is None:
            return self.add_vc_vmware_error(info, 'Network %s not found' % (nic['networkName']), vm)

        if network['type'] not in ['dvs', 'standard']:
            return self.add_vc_vmware_error(info, 'Unknown network type: %s' % (network['type']), vm)

        if network['type'] == 'dvs':
            info['vmware']['vswitchType'] = 'dvs'
            info['vmware']['vswitchName'] = network['dvsName']
            info['vmware']['trunk'] = network['trunk']
            info['vmware']['vlans'] = network['vlans']
            pnics = self.get_vc_host_pnic_in_dvs(vc, vm['host'], network['dvsName'])
            if pnics is None or len(pnics) == 0:
                return self.add_vc_vmware_error(info, 'Unexpected network no connectivity: %s on %s' % (network['dvsName'], vm['host']), vm)

            info['vmware']['pnic'] = []
            for pnic in pnics:
                pnic_info = {}
                pnic_info['device'] = pnic['device']
                pnic_info['mac'] = pnic['_info']['mac']
                info['vmware']['pnic'].append(
                    pnic_info
                )

        if network['type'] == 'standard':
            return self.add_vc_vmware_error(info, 'Unsupported network type: standard', vm)

        return info

    def add_vc_vm_server_info(self, info, vm):
        info['server'] = {}
        info['server']['name'] = vm['Server']['Name']
        info['server']['moid'] = vm['Server']['Moid']
        info['server']['type'] = vm['Server']['Type']
        info['server']['adapter'] = []

        server_info = self.get_server_by_moid(
            vm['Server']['Moid']
        )
        if server_info is None:
            return self.add_vc_vmware_error(info, 'Server %s not found' % (vm['Server']['Moid']), vm)

        info['server']['serial'] = server_info['Serial']
        if server_info['ManagementMode'] not in ['UCSM', 'IntersightStandalone']:
            return self.add_vc_vmware_error(info, 'Unsupported server management mode %s' % (vm['Server']['Moid']), vm)

        info['server']['management'] = server_info['ManagementMode']
        info['server']['ucsm'] = None
        if info['server']['management'] == 'UCSM':
            info['server']['ucsm'] = self.get_server_ucsm_name(
                info['server']['serial']
            )
            if info['server']['ucsm'] is None:
                return self.add_vc_vmware_error(info, 'UCSM managed server not found in any ucsm %s' % (vm['Server']['Moid']), vm)

        for pnic in info['vmware']['pnic']:
            for mac_info in server_info['MacAddressInfo']:
                if ip_helper.is_mac_equal(pnic['mac'], mac_info['MacAddress']):
                    pnic['interfaceDn'] = mac_info['InterfaceDn']

                    keys = [
                        'InterfaceDn',
                        'InterfaceName',
                        'MacAddress',
                        'AdapterModel',
                        'AdapterPciSlot'
                    ]
                    server_mac_info = {}
                    for key in keys:
                        server_mac_info[key] = mac_info[key]

                    info['server']['adapter'].append(
                        server_mac_info
                    )

        if len(info['server']['adapter']) != len(info['vmware']['pnic']):
            return self.add_vc_vmware_error(info, 'Not all vmware pnic found on server level', vm)

        return info

    def add_vc_vm_ucsm_blade_info(self, info, vm):
        for adapter in info['server']['adapter']:
            adapter['vnic'] = self.get_ucsm_blade_eth_if_by_mac(adapter['MacAddress'], incl_vifs=True)
            if adapter['vnic'] is None:
                return self.add_vc_vmware_error(info, 'Adapter mac not found in ucsm: %s' % (adapter['MacAddress']), vm)

            adapter['iom_backplane'] = self.get_ucsm_chassis_eth_object_by_dn(
                adapter['vnic']['peer_dn']
            )
            if adapter['iom_backplane'] is None:
                return self.add_vc_vmware_error(info, 'vNIC peer not found in ucsm: %s' % (adapter['MacAddress']), vm)

            adapter['dce'] = self.get_ucsm_ext_eth_if_by_dn(
                adapter['iom_backplane']['peer_dn']
            )
            if adapter['dce'] is None:
                return self.add_vc_vmware_error(info, 'vNIC dce not found in ucsm: %s' % (adapter['iom_backplane']['peer_dn']), vm)

            adapter['vic'] = self.get_ucsm_vic_by_dn(
                adapter['dce']['adaptor_dn'],
                incl_dce=True
            )
            if adapter['vic'] is None:
                return self.add_vc_vmware_error(info, 'vic not found in ucsm: %s' % (adapter['dce']['adaptor_dn']), vm)

            for dce in adapter['vic']['dce']:
                dce['used_by_vnic'] = False
                if ip_helper.is_mac_equal(dce['mac'], adapter['dce']['mac']):
                    dce['used_by_vnic'] = True

            adapter['iom_backplane_pc'] = self.get_ucsm_chassis_eth_object_by_dn(
                adapter['iom_backplane']['ep_dn']
            )
            if adapter['iom_backplane_pc'] is None:
                return self.add_vc_vmware_error(info, 'I/O backplane not found in ucsm: %s' % (adapter['iom_backplane']['ep_dn']), vm)

            adapter['iom_fi'] = self.get_ucsm_chassis_fabric_port_by_module(
                adapter['vnic']['chassis_id'],
                adapter['iom_backplane']['iom_id']
            )
            if adapter['iom_fi'] is None or len(adapter['iom_fi']) == 0:
                return self.add_vc_vmware_error(info, 'I/O fabric not found in ucsm for module %s' % (adapter['iom_backplane']['iom_id']), vm)

            adapter['fi_iom'] = []
            for iom_eth in adapter['iom_fi']:
                fi_eth = self.get_ucsm_switch_eth_port_by_dn(
                    iom_eth['peer_dn']
                )
                if fi_eth is None:
                    return self.add_vc_vmware_error(info, 'Eth port not found in ucsm %s' % (iom_eth['peer_dn']), vm)

                adapter['fi_iom'].append(
                    fi_eth
                )

            adapter['fi'] = {}
            for fi in self.ucsm_fi[info['server']['ucsm']]:
                if fi['id'] == adapter['vnic']['switch_id']:
                    keys = [
                        'id',
                        'model',
                        'serial',
                        'operability',
                        'thermal'
                    ]
                    for key in keys:
                        adapter['fi'][key] = fi[key]

            adapter['vlan'] = {}
            for vlan in info['vmware']['vlans']:
                try:
                    vlan_int = int(vlan)
                except BaseException:
                    return self.add_vc_vmware_error(info, 'Unrecongnized vlan value %s' % (vlan), vm)

                adapter['vlan'][vlan] = {}
                adapter['vlan'][vlan]['vlan'] = self.get_ucsm_fabric_vlan_by_id(
                    vlan
                )
                if adapter['vlan'][vlan]['vlan'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric vlan not found %s' % (vlan), vm)

                adapter['vlan'][vlan]['pooledVlan'] = self.get_ucsm_fabric_pooled_vlan_by_name(
                    adapter['vlan'][vlan]['vlan']['name']
                )
                if adapter['vlan'][vlan]['pooledVlan'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric pooled vlan not found %s' % (adapter['vlan'][vlan]['vlan']['name']), vm)

                adapter['vlan'][vlan]['netGroup'] = self.get_ucsm_fabric_net_group_by_rn(
                    adapter['vlan'][vlan]['pooledVlan']['net_group_rn']
                )
                if adapter['vlan'][vlan]['netGroup'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric netGroup not found %s' % (adapter['vlan'][vlan]['pooledVlan']['net_group_rn']), vm)

                adapter['vlan'][vlan]['pc'] = self.get_ucsm_fabric_vlan_pc_by_net_group_rn(
                    adapter['vnic']['switch_id'],
                    adapter['vlan'][vlan]['pooledVlan']['net_group_rn']
                )
                if adapter['vlan'][vlan]['pc'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric vlan pc not found %s' % (adapter['vlan'][vlan]['pooledVlan']['net_group_rn']), vm)

                adapter['vlan'][vlan]['lan'] = self.get_ucsm_fabric_lan_pc_by_name(
                    adapter['vnic']['switch_id'],
                    adapter['vlan'][vlan]['pc']['name']
                )
                if adapter['vlan'][vlan]['lan'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric lan pc not found %s' % (adapter['vlan'][vlan]['pc']['name']), vm)

                adapter['vlan'][vlan]['ep'] = self.get_ucsm_fabric_lan_pc_ep_by_pc_dn(
                    adapter['vnic']['switch_id'],
                    adapter['vlan'][vlan]['lan']['dn']
                )
                if adapter['vlan'][vlan]['ep'] is None or len(adapter['vlan'][vlan]['ep']) == 0:
                    return self.add_vc_vmware_error(info, 'Fabric lan pc ep not found %s' % (adapter['vlan'][vlan]['lan']['dn']), vm)

                for ep in adapter['vlan'][vlan]['ep']:
                    ep['eth'] = self.get_ucsm_switch_eth_port_by_dn(
                        ep['ep_dn']
                    )
                    if ep['eth'] is None:
                        return self.add_vc_vmware_error(info, 'Fabric lan pc ep not found in fi %s' % (ep['ep_dn']), vm)

                    ep['fabric_type'] = None
                    ep['fabric_switch'] = None
                    ep['fabric_interface'] = None
                    for fi in self.fis:
                        if fi['Serial'] == adapter['fi']['serial']:
                            for eth in fi['Ethernet']:
                                if eth['SlotId'] == int(ep['slot_id']) and eth['PortId'] == int(ep['port_id']):
                                    if eth['ACI'] is None and eth['Nexus'] is None:
                                        continue

                                    if eth['ACI'] is not None:
                                        ep['fabric_type'] = 'ACI'
                                        ep['fabric_switch'] = eth['ACI']['node_name']
                                        ep['fabric_interface'] = eth['ACI']['interface_id']

                                    if eth['Nexus'] is not None:
                                        ep['fabric_type'] = 'Nexus'
                                        ep['fabric_switch'] = eth['Nexus']['device_name']
                                        ep['fabric_interface'] = eth['Nexus']['interface_id']

                                    link_id = '%s:%s:%s' % (
                                        ep['fabric_type'],
                                        ep['fabric_switch'],
                                        ep['fabric_interface']
                                    )
                                    if link_id not in info['links']:
                                        info['links'].append(
                                            link_id
                                        )

        return info

    def add_vc_vm_ucsm_rack_info(self, info, vm):
        for adapter in info['server']['adapter']:
            adapter['vnic'] = self.get_ucsm_rack_eth_if_by_mac(adapter['MacAddress'], incl_vifs=True)
            if adapter['vnic'] is None:
                return self.add_vc_vmware_error(info, 'Adapter mac not found in ucsm: %s' % (adapter['MacAddress']), vm)

            adapter['fi_vic'] = []
            fi_eth = self.get_ucsm_switch_eth_port_by_dn(
                adapter['vnic']['peer_dn']
            )
            if fi_eth is None:
                return self.add_vc_vmware_error(info, 'Eth port not found in ucsm %s' % (adapter['vnic']['peer_dn']), vm)

            adapter['fi_vic'].append(
                fi_eth
            )

            adapter['fi'] = {}
            for fi in self.ucsm_fi[info['server']['ucsm']]:
                if fi['id'] == adapter['vnic']['switch_id']:
                    keys = [
                        'id',
                        'model',
                        'serial',
                        'operability',
                        'thermal'
                    ]
                    for key in keys:
                        adapter['fi'][key] = fi[key]

            adapter['vlan'] = {}
            for vlan in info['vmware']['vlans']:
                try:
                    vlan_int = int(vlan)
                except BaseException:
                    return self.add_vc_vmware_error(info, 'Unrecongnized vlan value %s' % (vlan), vm)

                adapter['vlan'][vlan] = {}
                adapter['vlan'][vlan]['vlan'] = self.get_ucsm_fabric_vlan_by_id(
                    vlan
                )
                if adapter['vlan'][vlan]['vlan'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric vlan not found %s' % (vlan), vm)

                adapter['vlan'][vlan]['pooledVlan'] = self.get_ucsm_fabric_pooled_vlan_by_name(
                    adapter['vlan'][vlan]['vlan']['name']
                )
                if adapter['vlan'][vlan]['pooledVlan'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric pooled vlan not found %s' % (adapter['vlan'][vlan]['vlan']['name']), vm)

                adapter['vlan'][vlan]['netGroup'] = self.get_ucsm_fabric_net_group_by_rn(
                    adapter['vlan'][vlan]['pooledVlan']['net_group_rn']
                )
                if adapter['vlan'][vlan]['netGroup'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric netGroup not found %s' % (adapter['vlan'][vlan]['pooledVlan']['net_group_rn']), vm)

                adapter['vlan'][vlan]['pc'] = self.get_ucsm_fabric_vlan_pc_by_net_group_rn(
                    adapter['vnic']['switch_id'],
                    adapter['vlan'][vlan]['pooledVlan']['net_group_rn']
                )
                if adapter['vlan'][vlan]['pc'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric vlan pc not found %s' % (adapter['vlan'][vlan]['pooledVlan']['net_group_rn']), vm)

                adapter['vlan'][vlan]['lan'] = self.get_ucsm_fabric_lan_pc_by_name(
                    adapter['vnic']['switch_id'],
                    adapter['vlan'][vlan]['pc']['name']
                )
                if adapter['vlan'][vlan]['lan'] is None:
                    return self.add_vc_vmware_error(info, 'Fabric lan pc not found %s' % (adapter['vlan'][vlan]['pc']['name']), vm)

                adapter['vlan'][vlan]['ep'] = self.get_ucsm_fabric_lan_pc_ep_by_pc_dn(
                    adapter['vnic']['switch_id'],
                    adapter['vlan'][vlan]['lan']['dn']
                )
                if adapter['vlan'][vlan]['ep'] is None or len(adapter['vlan'][vlan]['ep']) == 0:
                    return self.add_vc_vmware_error(info, 'Fabric lan pc ep not found %s' % (adapter['vlan'][vlan]['lan']['dn']), vm)

                for ep in adapter['vlan'][vlan]['ep']:
                    ep['eth'] = self.get_ucsm_switch_eth_port_by_dn(
                        ep['ep_dn']
                    )
                    if ep['eth'] is None:
                        return self.add_vc_vmware_error(info, 'Fabric lan pc ep not found in fi %s' % (ep['ep_dn']), vm)

                    ep['fabric_type'] = None
                    ep['fabric_switch'] = None
                    ep['fabric_interface'] = None
                    for fi in self.fis:
                        if fi['Serial'] == adapter['fi']['serial']:
                            for eth in fi['Ethernet']:
                                if eth['SlotId'] == int(ep['slot_id']) and eth['PortId'] == int(ep['port_id']):
                                    if eth['ACI'] is None and eth['Nexus'] is None:
                                        continue

                                    if eth['ACI'] is not None:
                                        ep['fabric_type'] = 'ACI'
                                        ep['fabric_switch'] = eth['ACI']['node_name']
                                        ep['fabric_interface'] = eth['ACI']['interface_id']

                                    if eth['Nexus'] is not None:
                                        ep['fabric_type'] = 'Nexus'
                                        ep['fabric_switch'] = eth['Nexus']['device_name']
                                        ep['fabric_interface'] = eth['Nexus']['interface_id']

                                    link_id = '%s:%s:%s' % (
                                        ep['fabric_type'],
                                        ep['fabric_switch'],
                                        ep['fabric_interface']
                                    )
                                    if link_id not in info['links']:
                                        info['links'].append(
                                            link_id
                                        )

        return info

    # def add_vc_vm_imm_rack_info(self, info, vm):
    #     for adapter in info['server']['adapter']:
    #         adapter['vnic'] = self.get_ucsm_rack_eth_if_by_mac(adapter['MacAddress'], incl_vifs=True)
    #         if adapter['vnic'] is None:
    #             return self.add_vc_vmware_error(info, 'Adapter mac not found in ucsm: %s' % (adapter['MacAddress']), vm)

    #         adapter['fi_vic'] = []
    #         fi_eth = self.get_ucsm_switch_eth_port_by_dn(
    #             adapter['vnic']['peer_dn']
    #         )
    #         if fi_eth is None:
    #             return self.add_vc_vmware_error(info, 'Eth port not found in ucsm %s' % (adapter['vnic']['peer_dn']), vm)

    #         adapter['fi_vic'].append(
    #             fi_eth
    #         )

    #         adapter['fi'] = {}
    #         for fi in self.ucsm_fi[info['server']['ucsm']]:
    #             if fi['id'] == adapter['vnic']['switch_id']:
    #                 keys = [
    #                     'id',
    #                     'model',
    #                     'serial',
    #                     'operability',
    #                     'thermal'
    #                 ]
    #                 for key in keys:
    #                     adapter['fi'][key] = fi[key]

    #         adapter['vlan'] = {}
    #         for vlan in info['vmware']['vlans']:
    #             try:
    #                 vlan_int = int(vlan)
    #             except BaseException:
    #                 return self.add_vc_vmware_error(info, 'Unrecongnized vlan value %s' % (vlan), vm)

    #             adapter['vlan'][vlan] = {}
    #             adapter['vlan'][vlan]['vlan'] = self.get_ucsm_fabric_vlan_by_id(
    #                 vlan
    #             )
    #             if adapter['vlan'][vlan]['vlan'] is None:
    #                 return self.add_vc_vmware_error(info, 'Fabric vlan not found %s' % (vlan), vm)

    #             adapter['vlan'][vlan]['pooledVlan'] = self.get_ucsm_fabric_pooled_vlan_by_name(
    #                 adapter['vlan'][vlan]['vlan']['name']
    #             )
    #             if adapter['vlan'][vlan]['pooledVlan'] is None:
    #                 return self.add_vc_vmware_error(info, 'Fabric pooled vlan not found %s' % (adapter['vlan'][vlan]['vlan']['name']), vm)

    #             adapter['vlan'][vlan]['netGroup'] = self.get_ucsm_fabric_net_group_by_rn(
    #                 adapter['vlan'][vlan]['pooledVlan']['net_group_rn']
    #             )
    #             if adapter['vlan'][vlan]['netGroup'] is None:
    #                 return self.add_vc_vmware_error(info, 'Fabric netGroup not found %s' % (adapter['vlan'][vlan]['pooledVlan']['net_group_rn']), vm)

    #             adapter['vlan'][vlan]['pc'] = self.get_ucsm_fabric_vlan_pc_by_net_group_rn(
    #                 adapter['vnic']['switch_id'],
    #                 adapter['vlan'][vlan]['pooledVlan']['net_group_rn']
    #             )
    #             if adapter['vlan'][vlan]['pc'] is None:
    #                 return self.add_vc_vmware_error(info, 'Fabric vlan pc not found %s' % (adapter['vlan'][vlan]['pooledVlan']['net_group_rn']), vm)

    #             adapter['vlan'][vlan]['lan'] = self.get_ucsm_fabric_lan_pc_by_name(
    #                 adapter['vnic']['switch_id'],
    #                 adapter['vlan'][vlan]['pc']['name']
    #             )
    #             if adapter['vlan'][vlan]['lan'] is None:
    #                 return self.add_vc_vmware_error(info, 'Fabric lan pc not found %s' % (adapter['vlan'][vlan]['pc']['name']), vm)

    #             adapter['vlan'][vlan]['ep'] = self.get_ucsm_fabric_lan_pc_ep_by_pc_dn(
    #                 adapter['vnic']['switch_id'],
    #                 adapter['vlan'][vlan]['lan']['dn']
    #             )
    #             if adapter['vlan'][vlan]['ep'] is None or len(adapter['vlan'][vlan]['ep']) == 0:
    #                 return self.add_vc_vmware_error(info, 'Fabric lan pc ep not found %s' % (adapter['vlan'][vlan]['lan']['dn']), vm)

    #             for ep in adapter['vlan'][vlan]['ep']:
    #                 ep['eth'] = self.get_ucsm_switch_eth_port_by_dn(
    #                     ep['ep_dn']
    #                 )
    #                 if ep['eth'] is None:
    #                     return self.add_vc_vmware_error(info, 'Fabric lan pc ep not found in fi %s' % (ep['ep_dn']), vm)

    #                 ep['fabric_type'] = None
    #                 ep['fabric_switch'] = None
    #                 ep['fabric_interface'] = None
    #                 for fi in self.fis:
    #                     if fi['Serial'] == adapter['fi']['serial']:
    #                         for eth in fi['Ethernet']:
    #                             if eth['SlotId'] == int(ep['slot_id']) and eth['PortId'] == int(ep['port_id']):
    #                                 if eth['ACI'] is None and eth['Nexus'] is None:
    #                                     continue

    #                                 if eth['ACI'] is not None:
    #                                     ep['fabric_type'] = 'ACI'
    #                                     ep['fabric_switch'] = eth['ACI']['node_name']
    #                                     ep['fabric_interface'] = eth['ACI']['interface_id']

    #                                 if eth['Nexus'] is not None:
    #                                     ep['fabric_type'] = 'Nexus'
    #                                     ep['fabric_switch'] = eth['Nexus']['device_name']
    #                                     ep['fabric_interface'] = eth['Nexus']['interface_id']

    #                                 link_id = '%s:%s:%s' % (
    #                                     ep['fabric_type'],
    #                                     ep['fabric_switch'],
    #                                     ep['fabric_interface']
    #                                 )
    #                                 if link_id not in info['links']:
    #                                     info['links'].append(
    #                                         link_id
    #                                     )

    #     return info

    def run_vc_vm_fabric(self, vc, vm, nic):
        info = {}
        info['collected'] = True
        info['reason'] = None
        info['links'] = []

        info = self.add_vc_vm_vmware_info(info, vc, vm, nic)
        if not info['collected']:
            return info

        info = self.add_vc_vm_server_info(info, vm)
        if not info['collected']:
            return info

        if info['server']['management'] == 'IntersightStandalone':
            if info['server']['type'] == 'Rack':
                return self.add_vc_vmware_error(info, 'Unsupported imm rack: %s' % (info['server']['moid']), vm)
                # info = self.add_vc_vm_imm_rack_info(info, vm)
                # if not info['collected']:
                #     return info

            if info['server']['type'] == 'Blade':
                return self.add_vc_vmware_error(info, 'Unsupported imm blade: %s' % (info['server']['moid']), vm)

        if info['server']['management'] == 'UCSM':
            if info['server']['type'] == 'Rack':
                info = self.add_vc_vm_ucsm_rack_info(info, vm)
                if not info['collected']:
                    return info

            if info['server']['type'] == 'Blade':
                info = self.add_vc_vm_ucsm_blade_info(info, vm)
                if not info['collected']:
                    return info

        return info
