import copy
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciAp():
    def __init__(self):
        self.aci_ap = None

    def load_pre_aci_ap(self):
        self.aci_ap = self.get_pre_cache('aci', 'ap')
        if self.aci_ap is None:
            return False
        return True

    def set_post_aci_ap(self):
        return self.set_post_cache('aci-ap', self.aci_ap)

    def load_post_aci_ap(self):
        self.aci_ap = self.get_post_cache('aci-ap')
        if self.aci_ap is None:
            return False
        return True

    def get_aci_ap(self):
        info = copy.deepcopy(self.aci_ap)
        return info

    def prepare_aci_ap(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_ap = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci ap: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_ap:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-ap' % (aci_controller['name']))
                if cache is not None:
                    self.aci_ap[aci_controller['name']] = cache
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

            apic_application_profiles = apic_handler.get_application_profiles(
                epg_info=True,
                node_info=True
            )
            if apic_application_profiles is None:
                continue

            self.aci_ap[aci_controller['name']] = []
            for item in apic_application_profiles:
                item['apic'] = aci_controller['name']
                self.aci_ap[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-ap' % (aci_controller['name']),
                self.aci_ap[aci_controller['name']]
            )

        return True

    def run_aci_ap(self):
        for key in self.aci_ap:
            for item in self.aci_ap[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item
                )

                item['domainCount'] = {}
                for domain_type in self.get_aci_domain_types():
                    item['domainCount'][domain_type] = 0

                for epg in item['epgs']:
                    epg['hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        epg
                    )
                    epg['bd_hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        name_tenant='%s/%s' % (
                            epg['bd_tenant_name'],
                            epg['bd_name']
                        )
                    )
                    for contract in epg['contractConsumed']:
                        contract['hash'] = aci_helper.get_aci_object_hash(
                            item['apic'],
                            contract,
                            extra='standard'
                        )
                    for contract in epg['contractProvided']:
                        contract['hash'] = aci_helper.get_aci_object_hash(
                            item['apic'],
                            contract,
                            extra='standard'
                        )
                    for contract in epg['contractTaboo']:
                        contract['hash'] = aci_helper.get_aci_object_hash(
                            item['apic'],
                            contract,
                            extra='taboo'
                        )

                    for domain in epg['domain']:
                        domain_type = self.get_aci_domain_type(
                            domain['tDn']
                        )
                        domain['hash'] = aci_helper.get_aci_object_hash(
                            item['apic'],
                            domain,
                            extra=domain_type
                        )
                        item['domainCount'][domain_type] += 1

                item['contracts'] = []
                for epg in item['epgs']:
                    for contract_type in ['Consumed', 'Provided', 'Taboo']:
                        for consumed in epg['contract%s' % (contract_type)]:
                            contract = {}
                            contract['epg'] = epg['nameTenant']
                            contract['epg_hash'] = epg['hash']
                            contract['contract'] = consumed['nameTenant']
                            contract['contract_hash'] = consumed['hash']
                            contract['type'] = contract_type
                            item['contracts'].append(
                                contract
                            )

                item['contractRelations'] = 0
                for epg in item['epgs']:
                    item['contractRelations'] += epg['contractCount']

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

        if not self.set_post_aci_ap():
            return False

        return True
