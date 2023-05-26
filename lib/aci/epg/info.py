import time
import copy

from lib import filter_helper
from lib import ip_helper


class EpgInfo():
    def __init__(self):
        self.epgs = None
        self.epgs_with_leaves = None

    def get_epg_count(self, tenant_name=None):
        epg_filter = None
        if tenant_name is not None:
            epg_filter = ['tenant:%s' % (tenant_name)]

        aepgs = self.get_epgs(
            epg_filter=epg_filter
        )
        return len(aepgs)

    def get_epg(self, epg_distinguished_name):
        epg_filter = ['dn:%s' % (epg_distinguished_name)]
        aepgs = self.get_epgs(
            epg_filter=epg_filter
        )

        if len(aepgs) == 1:
            return aepgs[0]

        return None

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

        info['contractConsumed'] = []
        for item in managed_object['fvRsCons']:
            if item['tCl'] == 'vzBrCP':
                contract = {}
                contract['dn'] = item['tDn']
                contract['tenant'] = item['tDn'].split('/')[1][3:]
                contract['name'] = item['tDn'].split('/')[2][4:]
                contract['nameTenant'] = '%s/%s' % (
                    contract['tenant'],
                    contract['name']
                )
                info['contractConsumed'].append(contract)

        info['contractProvided'] = []
        for item in managed_object['fvRsProv']:
            if item['tCl'] == 'vzBrCP':
                contract = {}
                contract['dn'] = item['tDn']
                contract['tenant'] = item['tDn'].split('/')[1][3:]
                contract['name'] = item['tDn'].split('/')[2][4:]
                contract['nameTenant'] = '%s/%s' % (
                    contract['tenant'],
                    contract['name']
                )
                info['contractProvided'].append(contract)

        info['contractTick'] = ''
        if len(info['contractConsumed']) > 0 or len(info['contractProvided']) > 0:
            info['contractTick'] = '\u2713'
            info['__Output']['contractTick'] = 'Green'

        if len(managed_object['fvBD']) != 1:
            self.log.error(
                'get_epg_info',
                'Unexpected fvBD count: %s' % (managed_object)
            )
            return None

        info['fvBD'] = self.get_bridge_domain(
            managed_object['fvBD'][0]['tDn'].split('/')[1][3:],
            managed_object['fvBD'][0]['tDn'].split('/')[2][3:]
        )

        return info

    def get_epgs_info(self, deployed_leaves_info=False):
        if self.epgs is None:
            epgs = self.get_epgs_mo()
            if epgs is not None:
                self.epgs = []
                for managed_object in epgs:
                    self.epgs.append(
                        self.get_epg_info(
                            managed_object
                        )
                    )

        if not deployed_leaves_info:
            return self.epgs

        if self.epgs_with_leaves is not None:
            return self.epgs_with_leaves

        epgs_with_leaves_mo = self.get_epgs_deployed_leaves_mo()
        if epgs_with_leaves_mo is None:
            return None

        self.epgs_with_leaves = copy.deepcopy(
            self.epgs
        )

        for epg_with_leaves_info in self.epgs_with_leaves:
            epg_with_leaves_info['fabricNode'] = []
            for managed_object in epgs_with_leaves_mo:
                if epg_with_leaves_info['dn'] == managed_object['epgPKey']:
                    for item in managed_object['fvLocale']:
                        node_info = copy.deepcopy(
                            self.get_node(node_id=item['id'])
                        )
                        if node_info is not None:
                            epg_with_leaves_info['fabricNode'].append(
                                node_info
                            )

        return self.epgs_with_leaves

    def match_epg(self, epg_info, epg_filter):
        if epg_filter is None or len(epg_filter) == 0:
            return True

        for aepg_rule in epg_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, epg_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, epg_info['dn']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, epg_info['tenant']):
                    return False

            if key == 'profile':
                if not filter_helper.match_string(value, epg_info['application_profile']):
                    return False

            if key == 'node':
                found = False
                for node_info in epg_info['fabricNode']:
                    if filter_helper.match_string(value, node_info['name']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'contract':
                found = False
                for contract in epg_info['contractConsumed']:
                    if filter_helper.match_string(value, contract['nameTenant']):
                        found = True
                        break

                for contract in epg_info['contractProvided']:
                    if filter_helper.match_string(value, contract['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'bd':
                if not filter_helper.match_string(value, epg_info['fvBD']['nameTenant']):
                    return False

            if key == 'subnet':
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
                if epg_info['fvBD'] is None:
                    return False

                found = False
                for bd_subnet in epg_info['fvBD']['fvSubnet']:
                    if ip_helper.is_ipv4_in_cidr(value, bd_subnet['network']):
                        found = True
                        break

                if not found:
                    return False

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

    def get_epg_l3out_filter(self, epg_info):
        l3outs = []
        for l3out in epg_info['fvBD']['fvRsBDToOut']:
            l3outs.append(
                l3out['name']
            )

        l3out_filter = ''
        if len(l3outs) > 0:
            l3out_filter = ['names:%s' % (','.join(l3outs))]

        return l3out_filter

    def get_epgs(self, epg_filter=None, deployed_leaves_info=False, endpoint_info=False, endpoint_vm_info=False, endpoint_fabric_info=False, contract_info=False, vrf_info=False, l3out_info=False):
        start_time = int(time.time() * 1000)

        all_epgs = self.get_epgs_info(
            deployed_leaves_info=deployed_leaves_info
        )
        if all_epgs is None:
            return None

        epgs = []

        for epg_info in all_epgs:
            if not self.match_epg(epg_info, epg_filter):
                continue

            if endpoint_info:
                endpoint_filter = ['epg:%s' % (epg_info['name'])]
                epg_info['fvCEp'] = self.get_endpoints(
                    endpoint_filter=endpoint_filter,
                    vm_info=endpoint_vm_info,
                    fabric_info=endpoint_fabric_info
                )

                epg_info['endpointsCount'] = 0
                if epg_info['fvCEp'] is not None:
                    epg_info['endpointsCount'] = len(
                        epg_info['fvCEp']
                    )

                epg_info['fvBD']['fvSubnet'] = self.get_subnet_usage(
                    epg_info['fvBD']['fvSubnet'],
                    epg_info['fvCEp']
                )

            if contract_info:
                epg_info['contractConsumedInfo'] = []
                contract_filter = self.get_epg_contract_filter(
                    epg_info['contractConsumed']
                )
                if len(contract_filter) > 0:
                    epg_info['contractConsumedInfo'] = copy.deepcopy(
                        self.get_contracts(
                            contract_filter=contract_filter
                        )
                    )

                epg_info['contractProvidedInfo'] = []
                contract_filter = self.get_epg_contract_filter(
                    epg_info['contractProvided']
                )
                if len(contract_filter) > 0:
                    epg_info['contractProvidedInfo'] = copy.deepcopy(
                        self.get_contracts(
                            contract_filter=contract_filter
                        )
                    )

            if vrf_info:
                vrf_dn = epg_info['fvBD']['fvRsCtx']['dn']
                epg_info['fvBD']['fvCtxInfo'] = copy.deepcopy(
                    self.get_vrf(
                        vrf_dn
                    )
                )

            if l3out_info:
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

            epgs.append(epg_info)

        epgs = sorted(
            epgs,
            key=lambda i: i['nameApTenant'].lower()
        )

        self.log.apic_mo(
            'fvAEPg.info',
            epgs
        )

        self.log.trace(
            'get_epgs',
            start_time
        )

        return epgs
