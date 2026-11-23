import copy
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciPoolVlan():
    def __init__(self):
        self.aci_pool_vlan = None

    def load_pre_aci_pool_vlan(self):
        self.aci_pool_vlan = self.get_pre_cache('aci', 'pvlan')
        if self.aci_pool_vlan is None:
            return False
        return True

    def set_post_aci_pool_vlan(self):
        return self.set_post_cache('aci-pvlan', self.aci_pool_vlan)

    def load_post_aci_pool_vlan(self):
        self.aci_pool_vlan = self.get_post_cache('aci-pvlan')
        if self.aci_pool_vlan is None:
            return False
        return True

    def get_aci_pool_vlan(self):
        info = copy.deepcopy(self.aci_pool_vlan)
        return info

    def prepare_aci_pool_vlan(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_pool_vlan = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci pool vlan: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_pool_vlan:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-pvlan' % (aci_controller['name']))
                if cache is not None:
                    self.aci_pool_vlan[aci_controller['name']] = cache
                    self.my_output.debug('L3 Cache hit')
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

            apic_pools_vlan = apic_handler.get_pool_vlans(
                vlan_usage_info=True,
                node_info=True
            )
            if apic_pools_vlan is None:
                continue

            self.aci_pool_vlan[aci_controller['name']] = []
            for item in apic_pools_vlan:
                item['apic'] = aci_controller['name']
                self.aci_pool_vlan[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-pvlan' % (aci_controller['name']),
                self.aci_pool_vlan[aci_controller['name']]
            )

        return True

    def run_aci_pool_vlan(self):
        for key in self.aci_pool_vlan:
            for item in self.aci_pool_vlan[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item,
                    extra='vlan'
                )

                if item['VlanNsToInterface'] is None:
                    item['VlanNsToInterface'] = []
                if item['VlanNsToVirtualMachines'] is None:
                    item['VlanNsToVirtualMachines'] = []
                if item['VlanNsToVmmPortGroups'] is None:
                    item['VlanNsToVmmPortGroups'] = []

                item['interfacePhy'] = []
                node_ids = []
                for interface_info in item['VlanNsToInterface']:
                    if interface_info['ctxClass'] == 'l1PhysIf':
                        if interface_info['nodeId'] not in node_ids:
                            node_ids.append(
                                interface_info['nodeId']
                            )
                        for node_interface in self.aci_phy[item['apic']][interface_info['nodeId']]:
                            if aci_helper.is_aci_interface_equal(interface_info['interface_name'], node_interface['id']):
                                item['interfacePhy'].append(
                                    filter_helper.get_json_root_attributes(
                                        node_interface,
                                        exceptions=['stats']
                                    )
                                )

                item['nodeCount'] = len(node_ids)
                item['interfaceCount'] = len(item['interfacePhy'])
                item['vmCount'] = len(item['VlanNsToVirtualMachines'])
                item['pgCount'] = len(item['VlanNsToVmmPortGroups'])

        if not self.set_post_aci_pool_vlan():
            return False

        return True
