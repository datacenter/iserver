import copy
from lib import ip_helper
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciBd():
    def __init__(self):
        self.aci_bd = None

    def load_pre_aci_bd(self):
        self.aci_bd = self.get_pre_cache('aci', 'bd')
        if self.aci_bd is None:
            return False
        return True

    def set_post_aci_bd(self):
        return self.set_post_cache('aci-bd', self.aci_bd)

    def load_post_aci_bd(self):
        self.aci_bd = self.get_post_cache('aci-bd')
        if self.aci_bd is None:
            return False
        return True

    def get_aci_bd(self):
        info = copy.deepcopy(self.aci_bd)
        return info

    def prepare_aci_bd(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_bd = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci bd: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_bd:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-bd' % (aci_controller['name']))
                if cache is not None:
                    self.aci_bd[aci_controller['name']] = cache
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

            apic_bridge_domains = apic_handler.get_bridge_domains(
                endpoint_info=True,
                endpoint_vm_info=True,
                endpoint_fabric_info=True,
                snoop_info=True,
                vrf_info=True,
                epg_info=True,
                node_info=True
            )
            if apic_bridge_domains is None:
                continue

            self.aci_bd[aci_controller['name']] = []
            for item in apic_bridge_domains:
                item['apic'] = aci_controller['name']
                self.aci_bd[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-bd' % (aci_controller['name']),
                self.aci_bd[aci_controller['name']]
            )

        return True

    def run_aci_bd(self):
        for key in self.aci_bd:
            for item in self.aci_bd[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['nameTenant']
                    )
                )

                item['fvCtx']['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['fvCtx']['nameTenant']
                    )
                )

                for epg in item['fvAEPg']:
                    epg['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            epg['nameApTenant']
                        )
                    )

                item['l3Out'] = []
                for l3 in item['fvRsBDToOut']:
                    l3['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            l3['nameTenant']
                        )
                    )
                    item['l3Out'].append(
                        l3['nameTenant']
                    )

                item['nodeCount'] = len(
                    item['node']
                )

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

        if not self.set_post_aci_bd():
            return False

        return True
