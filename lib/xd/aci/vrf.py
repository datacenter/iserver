import copy
from lib import ip_helper
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciVrf():
    def __init__(self):
        self.aci_vrf = None

    def load_pre_aci_vrf(self):
        self.aci_vrf = self.get_pre_cache('aci', 'vrf')
        if self.aci_vrf is None:
            return False
        return True

    def set_post_aci_vrf(self):
        return self.set_post_cache('aci-vrf', self.aci_vrf)

    def load_post_aci_vrf(self):
        self.aci_vrf = self.get_post_cache('aci-vrf')
        if self.aci_vrf is None:
            return False
        return True

    def get_aci_vrf(self):
        info = copy.deepcopy(self.aci_vrf)
        return info

    def prepare_aci_vrf(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_vrf = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci vrf: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_vrf:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-vrf' % (aci_controller['name']))
                if cache is not None:
                    self.aci_vrf[aci_controller['name']] = cache
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

            apic_vrfs = apic_handler.get_vrfs(
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=True,
                node_info=True
            )
            if apic_vrfs is None:
                continue

            self.aci_vrf[aci_controller['name']] = []
            for item in apic_vrfs:
                item['apic'] = aci_controller['name']
                self.aci_vrf[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-vrf' % (aci_controller['name']),
                self.aci_vrf[aci_controller['name']]
            )

        return True

    def run_aci_vrf(self):
        for key in self.aci_vrf:
            for item in self.aci_vrf[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['nameTenant']
                    )
                )

                for sub in item['fvBD']:
                    sub['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            sub['nameTenant']
                        )
                    )

                for sub in item['fvAEPg']:
                    sub['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            sub['nameApTenant']
                        )
                    )

                for sub in item['l3out']:
                    sub['hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            sub['nameTenant']
                        )
                    )

                item['bdCount'] = len(item['fvBD'])
                item['subnetCount'] = len(item['fvSubnet'])
                item['epgCount'] = len(item['fvAEPg'])
                item['l3outCount'] = len(item['l3out'])
                item['nodeCount'] = len(item['node'])
                item['routeCount'] = len(item['v4route'])

                item['interfacePhy'] = []
                for interface_info in item['interface']:
                    if aci_helper.get_aci_interface_type(interface_info['intf_name']) == 'eth':
                        for node_interface in self.aci_phy[item['apic']][interface_info['node_id']]:
                            if aci_helper.is_aci_interface_equal(interface_info['intf_name'], node_interface['id']):
                                item['interfacePhy'].append(
                                    filter_helper.get_json_root_attributes(
                                        node_interface
                                    )
                                )

        if not self.set_post_aci_vrf():
            return False

        return True
