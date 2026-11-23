import time
import copy
import json

from lib import filter_helper
from lib import ip_helper


class EpgInfo():
    def __init__(self):
        self.epg = None

    def init_epg(self):
        self.epg = None

    def get_epg_count(self, tenant_name=None, cache_enabled=True):
        epg_filter = None
        if tenant_name is not None:
            epg_filter = ['tenant:%s' % (tenant_name)]

        aepgs = self.get_epgs(
            epg_filter=epg_filter,
            cache_enabled=cache_enabled
        )
        return len(aepgs)

    def get_epg_dn(
            self,
            epg_distinguished_name,
            bd_info=False,
            locale_info=False,
            ifconn_info=False,
            endpoint_info=False,
            endpoint_vm_info=False,
            endpoint_fabric_info=False,
            contract_info=False,
            vrf_info=False,
            l3out_info=False,
            node_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None,
            cache_enabled=True
            ):
        epg_filter = ['dn:%s' % (epg_distinguished_name)]
        aepgs = self.get_epgs(
            epg_filter=epg_filter,
            bd_info=bd_info,
            locale_info=locale_info,
            ifconn_info=ifconn_info,
            endpoint_info=endpoint_info,
            endpoint_vm_info=endpoint_vm_info,
            endpoint_fabric_info=endpoint_fabric_info,
            contract_info=contract_info,
            vrf_info=vrf_info,
            l3out_info=l3out_info,
            node_info=node_info,
            fault_info=fault_info,
            hfault_info=hfault_info,
            event_info=event_info,
            audit_info=audit_info,
            hfault_filter=hfault_filter,
            event_filter=event_filter,
            audit_filter=audit_filter,
            cache_enabled=True
        )

        if len(aepgs) == 1:
            return aepgs[0]

        return None

    def get_epg(
            self,
            tenant_name,
            ap_name,
            epg_name,
            bd_info=False,
            locale_info=False,
            ifconn_info=False,
            endpoint_info=False,
            endpoint_vm_info=False,
            endpoint_fabric_info=False,
            contract_info=False,
            vrf_info=False,
            l3out_info=False,
            node_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None,
            cache_enabled=True
            ):
        epg_filter = []
        epg_filter.append('tenant:%s' % (tenant_name))
        epg_filter.append('profile:%s' % (ap_name))
        epg_filter.append('name:%s' % (epg_name))

        aepgs = self.get_epgs(
            epg_filter=epg_filter,
            bd_info=bd_info,
            locale_info=locale_info,
            ifconn_info=ifconn_info,
            endpoint_info=endpoint_info,
            endpoint_vm_info=endpoint_vm_info,
            endpoint_fabric_info=endpoint_fabric_info,
            contract_info=contract_info,
            vrf_info=vrf_info,
            l3out_info=l3out_info,
            node_info=node_info,
            fault_info=fault_info,
            hfault_info=hfault_info,
            event_info=event_info,
            audit_info=audit_info,
            hfault_filter=hfault_filter,
            event_filter=event_filter,
            audit_filter=audit_filter,
            cache_enabled=cache_enabled
        )

        if len(aepgs) == 1:
            return aepgs[0]

        return None

    def is_epg(self, tenant_name, ap_name, epg_name, cache_enabled=True):
        if self.get_epg(tenant_name, ap_name, epg_name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_epg_contract_info(self, managed_object, info):
        info['contractConsumed'] = []
        for item in managed_object['fvRsCons']:
            if item['tCl'] == 'vzBrCP':
                if item['state'] == 'formed':
                    contract = {}
                    contract['dn'] = item['tDn']
                    contract['tenant'] = item['tDn'].split('/')[1][3:]
                    contract['name'] = item['tDn'].split('/')[2][4:]
                    contract['nameTenant'] = '%s/%s' % (
                        contract['tenant'],
                        contract['name']
                    )
                    info['contractConsumed'].append(contract)

                if item['state'] != 'formed':
                    contract = {}
                    contract['__Output'] = {}
                    contract['__Output']['nameTenant'] = 'Red'
                    contract['dn'] = item['tDn']
                    contract['tenant'] = None
                    contract['name'] = item['tnVzBrCPName']
                    contract['nameTenant'] = item['tnVzBrCPName']
                    info['contractConsumed'].append(contract)

        info['contractProvided'] = []
        for item in managed_object['fvRsProv']:
            if item['tCl'] == 'vzBrCP':
                if item['state'] == 'formed':
                    contract = {}
                    contract['dn'] = item['tDn']
                    contract['tenant'] = item['tDn'].split('/')[1][3:]
                    contract['name'] = item['tDn'].split('/')[2][4:]
                    contract['nameTenant'] = '%s/%s' % (
                        contract['tenant'],
                        contract['name']
                    )
                    info['contractProvided'].append(contract)

                if item['state'] != 'formed':
                    contract = {}
                    contract['__Output'] = {}
                    contract['__Output']['nameTenant'] = 'Red'
                    contract['dn'] = item['tDn']
                    contract['tenant'] = None
                    contract['name'] = item['tnVzBrCPName']
                    contract['nameTenant'] = item['tnVzBrCPName']
                    info['contractProvided'].append(contract)

        info['contractTaboo'] = []
        for item in managed_object['fvRsProtBy']:
            if item['tCl'] == 'vzTaboo':
                if item['state'] == 'formed':
                    contract = {}
                    contract['dn'] = item['tDn']
                    contract['tenant'] = item['tDn'].split('/')[1][3:]
                    contract['name'] = item['tDn'].split('/')[2][6:]
                    contract['nameTenant'] = '%s/%s' % (
                        contract['tenant'],
                        contract['name']
                    )
                    info['contractTaboo'].append(contract)

                if item['state'] != 'formed':
                    contract = {}
                    contract['__Output'] = {}
                    contract['__Output']['nameTenant'] = 'Red'
                    contract['dn'] = item['tDn']
                    contract['tenant'] = None
                    contract['name'] = item['tnVzTabooName']
                    contract['nameTenant'] = item['tnVzTabooName']
                    info['contractTaboo'].append(contract)

        info['contractCount'] = len(info['contractConsumed']) + len(info['contractProvided']) + len(info['contractTaboo'])
        info['contractTick'] = ''
        if info['contractCount'] > 0:
            info['contractTick'] = '\u2713'
            info['__Output']['contractTick'] = 'Green'

        return info

    def get_epg_bd_info(self, managed_object, info):
        if len(managed_object['fvBD']) != 1:
            self.log.error(
                'get_epg_bd_info',
                'Unexpected fvBD count: %s' % (managed_object)
            )
            return None

        bd_mo = managed_object['fvBD'][0]
        if bd_mo['state'] == 'formed':
            info['bd_tenant_name'] = managed_object['fvBD'][0]['tDn'].split('/')[1][3:]
            info['bd_name'] = managed_object['fvBD'][0]['tDn'].split('/')[2][3:]
            info['bd_state'] = bd_mo['state']

        if bd_mo['state'] != 'formed':
            info['bd_tenant_name'] = bd_mo['tnFvBDName']
            info['bd_name'] = bd_mo['tnFvBDName']
            info['bd_state'] = bd_mo['state']
            info['__Output']['bd_tenant_name'] = 'Red'

        return info

    def get_epg_static_ports_info(self, managed_object, info):
        info['staticPort'] = []

        for item in managed_object['fvRsPathAtt']:
            keys = [
                'encap',
                'forceResolve',
                'instrImedcy',
                'mode',
                'primaryEncap',
                'state',
                'rn',
                'tCl',
                'tDn'
            ]
            port_info = {}
            port_info['__Output'] = {}

            for key in keys:
                port_info[key] = None
                if key in item:
                    port_info[key] = item[key]

            port_info['modeT'] = port_info['mode']
            if port_info['mode'] == 'regular':
                port_info['modeT'] = 'Trunk'

            if port_info['tCl'] != 'fabricPathEp':
                self.log.error(
                    'get_epg_static_ports_info',
                    'Unsupported tCl: %s' % (port_info['tCl'])
                )

            port_info['pathNode'] = ''
            port_info['pathNodeName'] = []
            port_info['pathType'] = ''
            port_info['pathEp'] = ''
            if port_info['tCl'] == 'fabricPathEp':
                if port_info['tDn'].split('/')[2].startswith('protpaths-'):
                    port_info['pathType'] = 'PG'
                    port_info['podId'] = port_info['tDn'].split('/')[1][4:]
                    port_info['pathNode'] = port_info['tDn'].split('/')[2][10:]
                    port_info['pathNodeT'] = 'node-%s' % (port_info['pathNode'])
                    for node_id in port_info['pathNode'].split('-'):
                        port_info['pathNodeName'].append(
                            'pod-%s/%s' % (
                                port_info['podId'],
                                self.get_node_name(
                                    node_id
                                )
                            )
                        )
                    port_info['pathEp'] = port_info['tDn'].split('[')[1].split(']')[0]

                if port_info['tDn'].split('/')[2].startswith('paths-'):
                    port_info['pathType'] = 'Intf'
                    port_info['podId'] = port_info['tDn'].split('/')[1][4:]
                    port_info['pathNode'] = port_info['tDn'].split('/')[2][6:]
                    port_info['pathNodeT'] = 'node-%s' % (port_info['pathNode'])
                    for node_id in port_info['pathNode'].split('-'):
                        port_info['pathNodeName'].append(
                            'pod-%s/%s' % (
                                port_info['podId'],
                                self.get_node_name(
                                    node_id
                                )
                            )
                        )
                    port_info['pathEp'] = port_info['tDn'].split('[')[1].split(']')[0]

            info['staticPort'].append(
                port_info
            )

        info['staticPort'] = sorted(
            info['staticPort'],
            key=lambda i: (
                i['pathNode'],
                i['pathEp']
            )
        )
        info['staticPortCount'] = len(info['staticPort'])

        return info

    def get_epg_domain_info(self, managed_object, info):
        info['domain'] = []

        for item in managed_object['fvRsDomAtt']:
            domain_info = {}
            domain_info['__Output'] = {}

            for key in item:
                domain_info[key] = item[key]

            if domain_info['tCl'] not in ['physDomP', 'vmmDomP', 'infraDomP']:
                self.log.error(
                    'get_epg_domain_info',
                    'Unsupported epg domain type: %s' % (domain_info['tCl'])
                )
                self.log.error(
                    'get_epg_domain_info',
                    json.dumps(domain_info, indent=4)
                )
                return None

            domain_info['type'] = domain_info['tCl']
            if domain_info['type'] == 'physDomP':
                domain_info['typeT'] = 'Physical'
                domain_info['name'] = domain_info['tDn'].split('/')[1][5:]

            if domain_info['type'] == 'infraDomP':
                domain_info['typeT'] = 'Infra'
                domain_info['name'] = domain_info['tDn'].split('/')[1][5:]

            if domain_info['type'] == 'vmmDomP':
                domain_info['typeT'] = 'VMM'
                domain_info['vmmType'] = domain_info['tDn'].split('/')[1][5:]
                domain_info['vmmName'] = domain_info['tDn'].split('/')[2][4:]
                domain_info['name'] = '%s/%s' % (
                    domain_info['vmmType'],
                    domain_info['vmmName']
                )

            info['domain'].append(
                domain_info
            )

        info['domain'] = sorted(
            info['domain'],
            key=lambda i: i['name']
        )

        info['domainCount'] = len(info['domain'])

        return info

    def get_epg_name_from_dn(self, epg_dn):
        # [0]: uni/tn-{name}/ap-{name}/epg-{name}
        if len(epg_dn) == 0:
            return ''

        tenant = epg_dn.split('/')[1][3:]
        application_profile = epg_dn.split('/')[2][3:]
        name = epg_dn.split('/')[3][4:]
        epg_name = '%s/%s/%s' % (
            tenant,
            application_profile,
            name
        )
        return epg_name

    def get_epg_info(self, managed_object):
        keys = [
            'annotation',
            'configSt',
            'descr',
            'dn',
            'exceptionTag',
            'floodOnEncap',
            'hasMcastSource',
            'isAttrBasedEPg',
            'matchT',
            'name',
            'nameAlias',
            'pcEnfPref',
            'pcTag',
            'prefGrMemb',
            'prio',
            'shutdown'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # state
        if info['shutdown'] == 'no':
            info['adminUp'] = True
            info['adminUpTick'] = '\u2713'
            info['__Output']['adminUpTick'] = 'Green'
        else:
            info['adminUp'] = False
            info['adminUpTick'] = '\u2717'
            info['__Output']['adminUpTick'] = 'Red'

        if info['configSt'] == 'applied':
            info['__Output']['configSt'] = 'Green'
        else:
            info['__Output']['configSt'] = 'Red'

        # pcTag Number Ranges
        # System Reserved pcTag – This pcTag is used for system internal rules (1-15).
        # Globally scoped pcTag – This pcTag is used for shared service (16-16385).
        # Locally scoped pcTag – This pcTag is locally used per VRF (range from 16386-65535).
        info['pcTagT'] = info['pcTag']
        try:
            if 15 < int(info['pcTag']) < 16386:
                info['pcTagT'] = '%s (global)' % (info['pcTag'])
                info['__Output']['pcTagT'] = 'Red'

            if int(info['pcTag']) < 16:
                info['pcTagT'] = '%s (system)' % (info['pcTag'])
                info['__Output']['pcTagT'] = 'Red'
        except BaseException:
            pass

        # Dn format
        # [0]: uni/tn-{name}/ap-{name}/epg-{name}
        info['tenant'] = info['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )
        info['application_profile'] = info['dn'].split('/')[2][3:]
        info['nameApTenant'] = '%s/%s/%s' % (
            info['tenant'],
            info['application_profile'],
            info['name']
        )

        info = self.get_epg_contract_info(
            managed_object,
            info
        )
        if info is None:
            return None

        info = self.get_epg_bd_info(
            managed_object,
            info
        )
        if info is None:
            return None

        info = self.get_epg_static_ports_info(
            managed_object,
            info
        )
        if info is None:
            return None

        info = self.get_epg_domain_info(
            managed_object,
            info
        )
        if info is None:
            return None

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_epgs_info(self, cache_enabled=True):
        if self.epg is not None:
            return self.epg

        epgs_mo = self.get_epg_mo(cache_enabled=cache_enabled)
        if epgs_mo is None:
            return None

        self.epg = []
        for epg_mo in epgs_mo:
            epg_info = self.get_epg_info(
                epg_mo
            )
            if epg_info is None:
                continue

            self.epg.append(
                epg_info
            )

        self.log.apic_mo(
            'fvAEPg.info',
            self.epg
        )

        return self.epg

    def match_epg_member(self, epg_member_info, epg_filter):
        if epg_filter is None or len(epg_filter) == 0:
            return True

        for aepg_rule in epg_filter:
            (key, value) = aepg_rule.split(':')

            if key == 'pg':
                if epg_member_info['pathType'] != 'Policy Group':
                    return False

                if not filter_helper.match_string(value, epg_member_info['pathName']):
                    return False

        return True

    def match_epg(self, epg_info, epg_filter):
        if epg_filter is None or len(epg_filter) == 0:
            return True

        for aepg_rule in epg_filter:
            (key, value) = aepg_rule.split(':')
            key_found = False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, epg_info['tenant']):
                    return False

            if key == 'profile':
                key_found = True
                if not filter_helper.match_string(value, epg_info['application_profile']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_ap_name(value, epg_info['nameApTenant']):
                    return False

            if key == 'dn':
                key_found = True
                if not filter_helper.match_string(value, epg_info['dn']):
                    return False

            if key == 'node':
                key_found = True
                if 'fabricNode' in epg_info:
                    found = False

                    for node_info in epg_info['fabricNode']:
                        if filter_helper.match_string(value, node_info['name']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'contract':
                key_found = True
                found = False

                for contract in epg_info['contractConsumed']:
                    if filter_helper.match_tenant_name(value, contract['nameTenant']):
                        found = True
                        break

                for contract in epg_info['contractProvided']:
                    if filter_helper.match_tenant_name(value, contract['nameTenant']):
                        found = True
                        break

                for contract in epg_info['contractTaboo']:
                    if filter_helper.match_tenant_name(value, contract['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'bd':
                key_found = True
                if 'fvBD' in epg_info:
                    if epg_info['fvBD'] is None:
                        return False

                    if not filter_helper.match_tenant_name(value, epg_info['fvBD']['nameTenant']):
                        return False

            if key == 'subnet':
                key_found = True
                if 'fvBD' in epg_info:
                    if epg_info['fvBD'] is None:
                        return False

                    found = False
                    for bd_subnet in epg_info['fvBD']['fvSubnet']:
                        if ip_helper.is_subnet_in_subnet(value, bd_subnet['network']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'ip':
                key_found = True
                if 'fvBD' in epg_info:
                    if epg_info['fvBD'] is None:
                        return False

                    found = False
                    for bd_subnet in epg_info['fvBD']['fvSubnet']:
                        if ip_helper.is_ipv4_in_cidr(value, bd_subnet['network']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'pctag':
                key_found = True
                if value == 'global':
                    if int(epg_info['pcTag']) >= 16386:
                        return False

                if value == 'system':
                    if int(epg_info['pcTag']) >= 16:
                        return False

                if value not in ['global', 'system']:
                    if not filter_helper.match_integer(value, epg_info['pcTag']):
                        return False

            if key == 'domain':
                key_found = True
                if 'domain' in epg_info:
                    found = False

                    for domain_info in epg_info['domain']:
                        if filter_helper.match_string(value, domain_info['name']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'pg':
                key_found = True
                if 'member' in epg_info:
                    found = False

                    for member_info in epg_info['member']:
                        if member_info['pathType'] == 'Policy Group':
                            if filter_helper.match_string(value, member_info['pathName']):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'member_type':
                key_found = True
                if 'member' in epg_info:
                    found = False

                    for member_info in epg_info['member']:
                        if member_info['memberType'] == 'dynamic' and value == 'dyn':
                            found = True
                            break

                        if member_info['memberType'] == 'static' and value == 'st':
                            found = True
                            break

                    if not found:
                        return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not epg_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_epg',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_epg',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_epg_contract_filter(self, epg_contracts):
        contracts = []
        for contract in epg_contracts:
            contracts.append(
                contract['nameTenant']
            )

        contract_filter = ''
        if len(contracts) > 0:
            contract_filter = ['names:%s' % (','.join(contracts))]

        return contract_filter

    def get_epgs_contract_filter(self, epgs_info):
        contracts = []
        for epg in epgs_info:
            for contract in epg['contractConsumed']:
                if contract['nameTenant'] not in contracts:
                    contracts.append(
                        contract['nameTenant']
                    )

            for contract in epg['contractProvided']:
                if contract['nameTenant'] not in contracts:
                    contracts.append(
                        contract['nameTenant']
                    )

        contract_filter = ''
        if len(contracts) > 0:
            contract_filter = ['names:%s' % (','.join(contracts))]

        return contract_filter

    def get_epgs_taboo_filter(self, epgs_info):
        contracts = []
        for epg in epgs_info:
            for contract in epg['contractTaboo']:
                if contract['nameTenant'] not in contracts:
                    contracts.append(
                        contract['nameTenant']
                    )

        contract_filter = ''
        if len(contracts) > 0:
            contract_filter = ['names:%s' % (','.join(contracts))]

        return contract_filter

    def get_epg_l3out_filter(self, epg_info):
        l3outs = []
        for l3out in epg_info['fvBD']['fvRsBDToOut']:
            l3outs.append(
                l3out['nameTenant']
            )

        l3out_filter = ''
        if len(l3outs) > 0:
            l3out_filter = ['names:%s' % (','.join(l3outs))]

        return l3out_filter

    def get_epgs(
            self,
            epg_filter=None,
            bd_info=False,
            locale_info=False,
            ifconn_info=False,
            endpoint_info=False,
            endpoint_vm_info=False,
            endpoint_fabric_info=False,
            contract_info=False,
            vrf_info=False,
            l3out_info=False,
            node_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None,
            cache_enabled=True
            ):

        if not cache_enabled:
            self.init_epg()
            self.init_epg_mo()

        all_epgs = self.get_epgs_info(cache_enabled=cache_enabled)
        if all_epgs is None:
            return None

        epgs = []

        for epg_info in all_epgs:
            if not self.match_epg(epg_info, epg_filter):
                continue

            if ifconn_info:
                epg_info['ifconn'] = self.get_epg_ifconn(
                    epg_ifconn_filter=['name:%s' % (epg_info['nameApTenant'])]
                )

                epg_info['ifconnSummary'] = self.get_epg_ifconn_summary(
                    epg_info['ifconn']
                )

                epg_info['member'] = []
                for ifconn in epg_info['ifconn']:
                    if ifconn['type'] in ['stpathatt', 'dyatt']:
                        if self.match_epg_member(ifconn, epg_filter):
                            epg_info['member'].append(
                                ifconn
                            )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if locale_info:
                epg_info['locale'] = self.get_epg_locale(
                    epg_locale_filter=['name:%s' % (epg_info['nameApTenant'])]
                )

                epg_info['fabricNode'] = self.get_epg_locale_node(
                    epg_info['locale']
                )

                epg_info['nodeCount'] = 0
                if epg_info['fabricNode'] is not None:
                    epg_info['nodeCount'] = len(
                        epg_info['fabricNode']
                    )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if bd_info:
                epg_info['fvBD'] = self.get_bridge_domain(
                    epg_info['bd_tenant_name'],
                    epg_info['bd_name']
                )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if endpoint_info:
                endpoint_filter = ['epg:%s' % (epg_info['name'])]
                epg_info['fvCEp'] = self.get_endpoints(
                    endpoint_filter=endpoint_filter,
                    vm_info=endpoint_vm_info,
                    fabric_info=endpoint_fabric_info
                )

                epg_info['endpointCount'] = 0
                if epg_info['fvCEp'] is not None:
                    epg_info['endpointCount'] = len(
                        epg_info['fvCEp']
                    )

                if epg_info['fvBD'] is not None:
                    epg_info['fvBD']['fvSubnet'] = self.get_subnet_usage(
                        epg_info['fvBD']['fvSubnet'],
                        epg_info['fvCEp']
                    )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if contract_info:
                epg_info['contractConsumedInfo'] = []
                contract_filter = self.get_epg_contract_filter(
                    epg_info['contractConsumed']
                )
                if len(contract_filter) > 0:
                    epg_info['contractConsumedInfo'] = copy.deepcopy(
                        self.get_standard_contracts(
                            contract_filter=contract_filter
                        )
                    )

                epg_info['contractProvidedInfo'] = []
                contract_filter = self.get_epg_contract_filter(
                    epg_info['contractProvided']
                )
                if len(contract_filter) > 0:
                    epg_info['contractProvidedInfo'] = copy.deepcopy(
                        self.get_standard_contracts(
                            contract_filter=contract_filter
                        )
                    )

                epg_info['contractTabooInfo'] = []
                contract_filter = self.get_epg_contract_filter(
                    epg_info['contractTaboo']
                )
                if len(contract_filter) > 0:
                    epg_info['contractTabooInfo'] = copy.deepcopy(
                        self.get_taboo_contracts(
                            taboo_filter=contract_filter
                        )
                    )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if vrf_info:
                if epg_info['fvBD'] is not None:
                    vrf_dn = epg_info['fvBD']['fvRsCtx']['dn']
                    epg_info['fvBD']['fvCtxInfo'] = copy.deepcopy(
                        self.get_vrf_by_dn(
                            vrf_dn
                        )
                    )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if l3out_info:
                if epg_info['fvBD'] is not None:
                    epg_info['fvBD']['l3extOutInfo'] = []
                    l3out_filter = self.get_epg_l3out_filter(
                        epg_info
                    )
                    if len(l3out_filter) > 0:
                        epg_info['fvBD']['l3extOutInfo'] = copy.deepcopy(
                            self.get_l3outs(
                                l3out_filter=l3out_filter
                            )
                        )

                if not self.match_epg(epg_info, epg_filter):
                    continue

            if node_info:
                ap_node_info = self.get_bridge_domain_node(
                    epg_info['bd_tenant_name'],
                    epg_info['bd_name']
                )
                epg_info['node'] = None
                epg_info['interface'] = None
                if ap_node_info is not None:
                    epg_info['node'] = ap_node_info['node']
                    epg_info['interface'] = ap_node_info['interface']

            if fault_info:
                epg_info['faultInst'] = self.get_epg_id_fault(
                    epg_info['tenant'],
                    epg_info['application_profile'],
                    epg_info['name'],
                    'faultInst'
                )

            if hfault_info:
                epg_info['faultRecord'] = self.get_epg_id_fault(
                    epg_info['tenant'],
                    epg_info['application_profile'],
                    epg_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                epg_info['eventLog'] = self.get_epg_id_event(
                    epg_info['tenant'],
                    epg_info['application_profile'],
                    epg_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                epg_info['auditLog'] = self.get_epg_id_audit(
                    epg_info['tenant'],
                    epg_info['application_profile'],
                    epg_info['name'],
                    audit_filter=audit_filter
                )

            epgs.append(epg_info)

        epgs = sorted(
            epgs,
            key=lambda i: i['nameApTenant'].lower()
        )

        return epgs

    def wait_epg(self, tenant_name, ap_name, epg_name, max_time=180):
        start_time = int(time.time())
        while True:
            if self.is_epg(tenant_name, ap_name, epg_name, cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'aci.wait_epg',
                    'Max time reached: %s/%s/%s' % (tenant_name, ap_name, epg_name)
                )
                return False

            time.sleep(5)

    def wait_no_epg(self, tenant_name, ap_name, epg_name, max_time=180):
        start_time = int(time.time())
        while True:
            if not self.is_epg(tenant_name, ap_name, epg_name, cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'aci.wait_epg',
                    'Max time reached: %s/%s/%s' % (tenant_name, ap_name, epg_name)
                )
                return False

            time.sleep(5)
