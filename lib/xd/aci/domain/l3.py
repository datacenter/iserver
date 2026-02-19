import copy
from lib import ip_helper
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciDomainL3():
    def __init__(self):
        self.aci_domain_l3 = None

    def load_pre_aci_domain_l3(self):
        self.aci_domain_l3 = self.get_pre_cache('aci', 'dl3')
        if self.aci_domain_l3 is None:
            return False
        return True

    def set_post_aci_domain_l3(self):
        return self.set_post_cache('aci-dl3', self.aci_domain_l3)

    def load_post_aci_domain_l3(self):
        self.aci_domain_l3 = self.get_post_cache('aci-dl3')
        if self.aci_domain_l3 is None:
            return False
        return True

    def get_aci_domain_l3(self):
        info = copy.deepcopy(self.aci_domain_l3)
        return info

    def prepare_aci_domain_l3(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_domain_l3 = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci domain l3: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_domain_l3:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-dl3' % (aci_controller['name']))
                if cache is not None:
                    self.aci_domain_l3[aci_controller['name']] = cache
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

            apic_domains_l3 = apic_handler.get_domains_l3(
                vlan_info=True,
                vlan_usage_info=True,
                node_info=True,
                intf_vlan_info=True
            )
            if apic_domains_l3 is None:
                continue

            self.aci_domain_l3[aci_controller['name']] = []
            for item in apic_domains_l3:
                item['apic'] = aci_controller['name']
                self.aci_domain_l3[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-dl3' % (aci_controller['name']),
                self.aci_domain_l3[aci_controller['name']]
            )

        return True

    def run_aci_domain_l3(self):
        for key in self.aci_domain_l3:
            for item in self.aci_domain_l3[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item,
                    extra=self.get_aci_domain_type(
                        item['dn']
                    )
                )

                item['aae_hash'] = {}
                for aae_name in item['aaep_names']:
                    item['aae_hash'][aae_name] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            aae_name
                        )
                    )
                item['nodeCount'] = len(item['node'])
                item['interfaceCount'] = len(item['interface'])

                item['interfacePhy'] = []
                for interface_info in item['interface']:
                    if aci_helper.get_aci_interface_type(interface_info['intf_name']) == 'eth':
                        for node_interface in self.aci_phy[item['apic']][interface_info['node_id']]:
                            if aci_helper.is_aci_interface_equal(interface_info['intf_name'], node_interface['id']):
                                item['interfacePhy'].append(
                                    filter_helper.get_json_root_attributes(
                                        node_interface,
                                        exceptions=['stats']
                                    )
                                )

                item['l3out'] = []
                for reln in item['reln']:
                    if reln['tCl'] == 'l3extOut':
                        l3out = {}
                        l3out['name'] = reln['name']
                        l3out['hash'] = ip_helper.get_string_md5(
                            '%s %s' % (
                                item['apic'],
                                reln['name']
                            )
                        )
                        item['l3out'].append(
                            l3out
                        )

        if not self.set_post_aci_domain_l3():
            return False

        return True
