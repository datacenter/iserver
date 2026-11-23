import copy
from lib import ip_helper
from lib import filter_helper
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciAae():
    def __init__(self):
        self.aci_aae = None

    def load_pre_aci_aae(self):
        self.aci_aae = self.get_pre_cache('aci', 'aae')
        if self.aci_aae is None:
            return False
        return True

    def set_post_aci_aae(self):
        return self.set_post_cache('aci-aae', self.aci_aae)

    def load_post_aci_aae(self):
        self.aci_aae = self.get_post_cache('aci-aae')
        if self.aci_aae is None:
            return False
        return True

    def get_aci_aae(self):
        info = copy.deepcopy(self.aci_aae)
        return info

    def prepare_aci_aae(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_aae = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci ap: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_aae:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-aae' % (aci_controller['name']))
                if cache is not None:
                    self.aci_aae[aci_controller['name']] = cache
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

            apic_aaes = apic_handler.get_policy_global_aaes(
                domain_info=True,
                node_info=True,
                pg_info=True,
                vm_info=True
            )
            if apic_aaes is None:
                continue

            self.aci_aae[aci_controller['name']] = []
            for item in apic_aaes:
                item['apic'] = aci_controller['name']
                self.aci_aae[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-aae' % (aci_controller['name']),
                self.aci_aae[aci_controller['name']]
            )

        return True

    def run_aci_aae(self):
        for key in self.aci_aae:
            for item in self.aci_aae[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['name']
                    )
                )

                item['policyGroups'] = []
                for pg_info in item['infraRtAttEntP']:
                    item['policyGroups'].append(
                        pg_info['name']
                    )

                item['interfacePhy'] = []
                node_ids = []
                for interface_info in item['interface']:
                    if aci_helper.get_aci_interface_type(interface_info['intf_name']) == 'eth':
                        if interface_info['node_id'] not in node_ids:
                            node_ids.append(interface_info['node_id'])
                        for node_interface in self.aci_phy[item['apic']][interface_info['node_id']]:
                            if aci_helper.is_aci_interface_equal(interface_info['intf_name'], node_interface['id']):
                                item['interfacePhy'].append(
                                    filter_helper.get_json_root_attributes(
                                        node_interface,
                                        exceptions=['stats']
                                    )
                                )

                # Domain

                for domain in item['infraRsDomP']:
                    domain['hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        name=domain['domainName'],
                        extra=self.get_aci_domain_type(
                            domain['tDn']
                        )
                    )

                item['infraRsDomP'] = sorted(
                    item['infraRsDomP'],
                    key=lambda i: (
                        i['domainName'].lower(),
                        i['domainType'].lower()
                    )
                )
                item['domainCount'] = len(item['infraRsDomP'])

                item['policyGroupCount'] = len(item['infraRtAttEntP'])
                item['vmCount'] = len(item['vm'])
                item['portGroupCount'] = len(item['pg'])
                item['nodeCount'] = len(node_ids)
                item['interfaceCount'] = len(item['interfacePhy'])

                # EPG

                for epg in item['infraRsFuncToEpg']:
                    epg['tenant'] = epg['epgName'].split('/')[0]
                    epg['application_profile'] = epg['epgName'].split('/')[1]
                    epg['name'] = epg['epgName'].split('/')[2]
                    epg['hash'] = aci_helper.get_aci_object_hash(
                        controller_name=item['apic'],
                        name_ap_tenant=epg['epgName']
                    )

                item['infraRsFuncToEpg'] = sorted(
                    item['infraRsFuncToEpg'],
                    key=lambda i: (
                        i['tenant'].lower(),
                        i['application_profile'].lower(),
                        i['name'].lower()
                    )
                )
                item['epgCount'] = len(item['infraRsFuncToEpg'])

        if not self.set_post_aci_aae():
            return False

        return True
