import copy
from lib.aci import apic
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper


class AciPhy():
    def __init__(self):
        self.aci_phy = None

    def load_pre_aci_phy(self):
        self.aci_phy = self.get_pre_cache('aci', 'phy')
        if self.aci_phy is None:
            return False
        return True

    def set_post_aci_phy(self):
        return self.set_post_cache('aci-phy', self.aci_phy)

    def load_post_aci_phy(self):
        self.aci_phy = self.get_post_cache('aci-phy')
        if self.aci_phy is None:
            return False
        return True

    def map_aci_interface_reason(self, reason):
        if reason.lower() == 'connected':
            return None

        if reason.lower() == 'sfp-missing':
            return 'No SFP'

        if reason.lower() == 'link-not-connected':
            return 'No link'

        return reason

    def get_aci_phy(self, controller, node_id):
        info = copy.deepcopy(self.aci_phy[controller][node_id])
        return info

    def prepare_aci_phy(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_phy = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci intf phy: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_phy:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-phy' % (aci_controller['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.aci_phy[aci_controller['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=self.log_id
            )

            nodes = apic_handler.get_nodes(
                node_filter=['role:!controller']
            )
            if nodes is None:
                self.log.error(
                    'prepare_aci_phy',
                    'Failed to get nodes: %s' % (aci_controller['name'])
                )
                continue

            self.aci_phy[aci_controller['name']] = {}
            for node in nodes:
                interfaces = apic_handler.get_interfaces_phy(
                    node['podId'],
                    node['id'],
                    fc_stats_info=True,
                    epg_stats_info=True,
                    cdp_info=True,
                    lldp_info=True,
                    policy_info=True,
                    pc_info=True
                )
                self.aci_phy[aci_controller['name']][node['id']] = []
                if interfaces is not None:
                    for item in interfaces:
                        item['apic'] = aci_controller['name']
                        item['node_id'] = node['id']
                        self.aci_phy[aci_controller['name']][node['id']].append(
                            item
                        )

            self.set_cache(
                'aci-%s-phy' % (aci_controller['name']),
                self.aci_phy[aci_controller['name']]
            )

        return True

    def run_aci_phy(self):
        # https://www.networklife.net/images/sheets/Networklife_CheatSheet_ACI_02_Fabric_access_policies.pdf
        for controller_name in self.aci_phy:
            for node_id in self.aci_phy[controller_name]:
                for item in self.aci_phy[controller_name][node_id]:
                    item['hash'] = aci_helper.get_aci_interface_hash(
                        controller_name,
                        node_id,
                        item['id']
                    )

                    item['_index'] = aci_helper.get_aci_interface_id(
                        item['id']
                    )

                    item['up'] = False
                    if item['stats'] is not None:
                        if item['stats']['operSt'] == 'up':
                            item['up'] = True
                        item['stats']['_reason'] = None
                        if item['stats']['operStQual'] is not None:
                            item['stats']['_reason'] = self.map_aci_interface_reason(
                                item['stats']['operStQual']
                            )

                    if item['epg_stats'] is not None:
                        item['epg_stats'] = sorted(
                            item['epg_stats'],
                            key=lambda i: i['nameApTenant'].lower()
                        )
                        for epg in item['epg_stats']:
                            epg['hash'] = aci_helper.get_aci_object_hash(
                                controller_name,
                                epg
                            )

                    item['nei_device_type'] = None
                    item['nei_apic_name'] = None
                    item['nei_device_name'] = None
                    item['nei_device_id'] = None
                    item['nei_interface_name'] = None
                    item['nei_interface_hash'] = None
                    item['nei_index'] = 0
                    item['nei_is_vmware'] = False
                    item['nei_is_ocp'] = False
                    item['cdp_hash'] = None
                    item['lldp_hash'] = None
                    item['xd'] = None

                    for lldp_controller_name in self.aci_lldp:
                        for lldp_nei in self.aci_lldp[lldp_controller_name]:
                            if lldp_nei['node_id'] != node_id:
                                continue

                            if not aci_helper.is_aci_interface_equal(item['id'], lldp_nei['interface_id']):
                                continue

                            item['lldp_hash'] = lldp_nei['hash']
                            item['xd'] = lldp_nei['xd']

                            if lldp_nei['xd']['DeviceType'] is None:
                                if item['nei_device_name'] is None:
                                    item['nei_device_name'] = self.get_short_name(lldp_nei['sysName'])
                                    if item['nei_device_name'] is None:
                                        if lldp_nei['sysDesc'] is not None:
                                            item['nei_device_name'] = ' '.join(lldp_nei['sysDesc'].split(' ')[:2])

                            if lldp_nei['xd']['DeviceType'] is not None and lldp_nei['xd']['DeviceType'] == 'Server':
                                item['nei_device_type'] = 'Server'
                                item['nei_device_name'] = lldp_nei['xd']['ServerName']
                                item['nei_device_id'] = lldp_nei['xd']['ServerMoid']
                                item['nei_interface_name'] = nei_server_info['ServerInterface']
                                if self.get_server_vc_by_moid(item['nei_device_id']) is not None:
                                    item['nei_is_vmware'] = True

                            if lldp_nei['xd']['DeviceType'] is not None and lldp_nei['xd']['DeviceType'] == 'ACI':
                                item['nei_device_type'] = 'ACI'
                                item['nei_apic_name'] = lldp_nei['xd']['AciApicName']
                                item['nei_device_name'] = lldp_nei['xd']['AciNodeName']
                                if item['nei_device_name'] is None:
                                    item['nei_device_name'] = self.get_short_name(lldp_nei['sysName'])
                                    if item['nei_device_name'] is None:
                                        if lldp_nei['sysDesc'] is not None:
                                            item['nei_device_name'] = ' '.join(lldp_nei['sysDesc'].split(' ')[:2])
                                else:
                                    item['nei_interface_name'] = lldp_nei['portId']
                                    item['nei_interface_hash'] = aci_helper.get_aci_interface_hash(
                                        lldp_nei['xd']['AciApicName'],
                                        lldp_nei['xd']['AciNodeId'],
                                        lldp_nei['portIdV']
                                    )

                            if lldp_nei['xd']['DeviceType'] is not None and lldp_nei['xd']['DeviceType'] == 'Nexus':
                                item['nei_device_type'] = 'Nexus'
                                item['nei_device_name'] = lldp_nei['xd']['NexusDevice']
                                item['nei_interface_name'] = lldp_nei['portId']
                                if item['nei_device_name'] is None:
                                    item['nei_device_name'] = self.get_short_name(lldp_nei['sysName'])
                                    if item['nei_device_name'] is None:
                                        if lldp_nei['sysDesc'] is not None:
                                            item['nei_device_name'] = ' '.join(lldp_nei['sysDesc'].split(' ')[:2])
                                else:
                                    item['nei_interface_hash'] = nexus_helper.get_nexus_interface_hash(
                                        item['nei_device_name'],
                                        item['nei_interface_name']
                                    )

                            if lldp_nei['xd']['DeviceType'] is not None and lldp_nei['xd']['DeviceType'] == 'FI':
                                item['nei_device_type'] = 'FI'
                                item['nei_device_name'] = lldp_nei['xd']['FI']
                                item['nei_interface_name'] = lldp_nei['portId']
                                item['nei_interface_hash'] = self.get_fi_interface_hash(
                                    item['nei_device_name'],
                                    item['nei_interface_name']
                                )
                                if item['nei_interface_hash'] is None:
                                    self.log.error(
                                        'run_aci_phy',
                                        'Unexpected no fi intf hash for %s %s' % (item['nei_device_name'], item['nei_interface_name'])
                                    )

                    for cdp_controller_name in self.aci_cdp:
                        for cdp_nei in self.aci_cdp[cdp_controller_name]:
                            if cdp_nei['node_id'] != node_id:
                                continue

                            if not aci_helper.is_aci_interface_equal(item['id'], cdp_nei['interfaceId']):
                                continue

                            item['cdp_hash'] = cdp_nei['hash']
                            item['xd'] = cdp_nei['xd']

                            if cdp_nei['xd']['DeviceType'] is None:
                                continue

                            if cdp_nei['xd']['DeviceType'] == 'ACI':
                                item['nei_device_type'] = 'ACI'
                                item['nei_apic_name'] = cdp_nei['xd']['AciApicName']
                                item['nei_device_name'] = cdp_nei['xd']['AciNodeName']
                                if item['nei_device_name'] is None:
                                    item['nei_device_name'] = self.get_short_name(cdp_nei['sysName'])

                            if cdp_nei['xd']['DeviceType'] == 'Nexus':
                                item['nei_device_type'] = 'Nexus'
                                item['nei_device_name'] = cdp_nei['xd']['NexusDevice']
                                if item['nei_device_name'] is None:
                                    item['nei_device_name'] = self.get_short_name(cdp_nei['sysName'])

                            if cdp_nei['xd']['DeviceType'] == 'FI':
                                item['nei_device_type'] = 'FI'
                                item['nei_device_name'] = cdp_nei['xd']['FI']

                    for nei_server_info in self.aci_node_servers[item['apic']][item['nodeName']]:
                        if item['id'] == nei_server_info['InterfaceId']:
                            if item['nei_device_type'] is None:
                                item['nei_device_type'] = 'Server'
                                item['nei_device_name'] = nei_server_info['ServerName']
                                item['nei_device_id'] = nei_server_info['ServerMoid']
                                item['nei_interface_name'] = nei_server_info['ServerInterface']

                    item['pi_vlans'] = None
                    pi_vlans = None
                    if 'stats' in item and item['stats'] is not None:
                        if len(item['stats']['operVlans']) > 0:
                            pi_vlans = item['stats']['operVlans']
                            item['pi_vlans'] = item['stats']['operVlans'].split(',')

                    item['encap_vlans'] = None
                    item['encap_vlan_ids'] = None
                    if item['pi_vlans'] is not None:
                        vlans = self.aci_node_cmd[controller_name][node_id]['vlan']['parsed']
                        if vlans is not None:
                            item['encap_vlans'] = []
                            item['encap_vlan_ids'] = []
                            for vlan_id in filter_helper.get_values_from_range(pi_vlans):
                                for vlan in vlans:
                                    if vlan_id == vlan['id']:
                                        for encap in vlan['encap']:
                                            if len(encap.split('vlan-')) == 2:
                                                encap_vlan_id = encap.split('vlan-')[1]
                                                item['encap_vlan_ids'].append(
                                                    encap_vlan_id
                                                )
                                                encap_vlan_info = {}
                                                encap_vlan_info['id'] = int(encap_vlan_id)
                                                encap_vlan_info['pi'] = vlan_id
                                                encap_vlan_info['name'] = vlan['name']
                                                encap_vlan_info['is_epg'] = False
                                                encap_vlan_info['epg_hash'] = None
                                                encap_vlan_info['is_l3out'] = False
                                                encap_vlan_info['l3out_hash'] = None

                                                for epg in self.aci_epg[controller_name]:
                                                    if epg['nameApTenant'] == vlan['name'].replace(':', '/'):
                                                        encap_vlan_info['is_epg'] = True
                                                        encap_vlan_info['epg_hash'] = aci_helper.get_aci_object_hash(
                                                            controller_name,
                                                            epg
                                                        )

                                                if not encap_vlan_info['is_epg'] and len(vlan['name'].split(':')) == 4:
                                                    l3out_name = vlan['name'].split(':')[2][6:]
                                                    vrf_name_tenant = '%s/%s' % (
                                                        vlan['name'].split(':')[0],
                                                        vlan['name'].split(':')[1]
                                                    )
                                                    for l3out in self.aci_l3out[controller_name]:
                                                        if l3out['name'] != l3out_name:
                                                            continue

                                                        if l3out['l3extRsEctx'] is None:
                                                            continue

                                                        if l3out['l3extRsEctx']['nameTenant'] != vrf_name_tenant:
                                                            continue

                                                        encap_vlan_info['is_l3out'] = True
                                                        encap_vlan_info['l3out_hash'] = aci_helper.get_aci_object_hash(
                                                            controller_name,
                                                            name_tenant=l3out['nameTenant']
                                                        )

                                                item['encap_vlans'].append(
                                                    encap_vlan_info
                                                )

                            item['encap_vlan_ids'] = sorted(item['encap_vlan_ids'])
                            item['encap_vlans'] = sorted(
                                item['encap_vlans'],
                                key=lambda i: i['id']
                            )

                    if item['policy_selector'] is not None:
                        item['policy_selector']['leafPolicy'] = None
                        for accportprof in self.aci_accportprof[controller_name]:
                            if accportprof['name'] == item['policy_selector']['profile']:
                                for reln in accportprof['reln']:
                                    if reln['tCl'] == 'infraNodeP':
                                        item['policy_selector']['leafPolicy'] = reln['tDn'].split('/')[2][6:]

        if not self.set_post_aci_phy():
            return False

        return True
