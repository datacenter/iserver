import copy
from lib import ip_helper
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciEpg():
    def __init__(self):
        self.aci_epg = None

    def load_pre_aci_epg(self):
        self.aci_epg = self.get_pre_cache('aci', 'epg')
        if self.aci_epg is None:
            return False
        return True

    def set_post_aci_epg(self):
        return self.set_post_cache('aci-epg', self.aci_epg)

    def load_post_aci_epg(self):
        self.aci_epg = self.get_post_cache('aci-epg')
        if self.aci_epg is None:
            return False
        return True

    def get_aci_epg(self):
        info = copy.deepcopy(self.aci_epg)
        return info

    def prepare_aci_epg(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_epg = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci epg: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_epg:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-epg' % (aci_controller['name']))
                if cache is not None:
                    self.aci_epg[aci_controller['name']] = cache
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

            apic_epgs = apic_handler.get_epgs(
                bd_info=True,
                locale_info=True,
                ifconn_info=True,
                endpoint_info=True,
                endpoint_vm_info=True,
                endpoint_fabric_info=True,
                contract_info=True,
                vrf_info=True,
                l3out_info=True,
                node_info=True
            )
            if apic_epgs is None:
                continue

            self.aci_epg[aci_controller['name']] = []
            for item in apic_epgs:
                item['apic'] = aci_controller['name']
                self.aci_epg[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-epg' % (aci_controller['name']),
                self.aci_epg[aci_controller['name']]
            )

        return True

    def run_aci_epg(self):
        for key in self.aci_epg:
            for item in self.aci_epg[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item
                )

                if item['tenant'] == item['bd_tenant_name']:
                    item['bdTenantName'] = item['bd_name']
                else:
                    item['bdTenantName'] = '%s/%s' % (
                        item['bd_tenant_name'],
                        item['bd_name']
                    )

                item['bd_hash'] = ip_helper.get_string_md5(
                    '%s %s/%s' % (
                        item['apic'],
                        item['bd_tenant_name'],
                        item['bd_name']
                    )
                )

                for contract in item['contractConsumed']:
                    contract['hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        contract,
                        extra='standard'
                    )

                for contract in item['contractProvided']:
                    contract['hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        contract,
                        extra='standard'
                    )

                for contract in item['contractTaboo']:
                    contract['hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        contract,
                        extra='taboo'
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

            self.aci_epg[key] = sorted(
                self.aci_epg[key],
                key=lambda i: (
                    i['tenant'].lower(),
                    i['application_profile'].lower(),
                    i['name'].lower()
                )
            )

        if not self.set_post_aci_epg():
            return False

        return True
