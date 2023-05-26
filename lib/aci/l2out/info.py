import copy
from lib import filter_helper


class L2OutInfo():
    def __init__(self):
        self.l2outs = None
        self.l2outs_with_path = None

    def get_l2out_count(self, tenant_name=None):
        l2out_filter = None
        if tenant_name is not None:
            l2out_filter = ['tenant:%s' % (tenant_name)]

        l2outs = self.get_l2outs(
            l2out_filter=l2out_filter
        )
        return len(l2outs)

    def get_l2out_ext_epg_info(self, managed_object):
        keys = [
            'annotation',
            'configSt',
            'descr',
            'exceptionTag',
            'floodOnEncap',
            'isSharedSrvMsiteEPg',
            'matchT',
            'name',
            'nameAlias',
            'pcEnfPref',
            'pcTag',
            'prefGrMemb',
            'prio',
            'rn',
            'targetDscp'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['configSt'] == 'applied':
            info['__Output']['configSt'] = 'Green'
        else:
            info['__Output']['configSt'] = 'Red'

        # "rn": "instP-L2Out-ext-epg"
        info['name'] = info['rn'][6:]

        return info

    def get_l2out_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
            'targetDscp',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # [0]: uni/tn-{name}/ap-{name}
        info['tenant'] = info['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        # Associated BD
        info['fvBD'] = None
        if managed_object['l2extRsEBd']['tCl'] == 'fvBD':
            info['fvBD'] = {}
            info['fvBD']['dn'] = managed_object['l2extRsEBd']['tDn']
            info['fvBD']['tenant'] = info['fvBD']['dn'].split('/')[1][3:]
            info['fvBD']['name'] = info['fvBD']['dn'].split('/')[2][3:]
            info['fvBD']['encap'] = managed_object['l2extRsEBd']['encap']
            info['fvBD']['nameTenant'] = '%s/%s' % (
                info['fvBD']['tenant'],
                info['fvBD']['name']
            )

        # Associated external physical domain
        info['l2extDomP'] = None
        if managed_object['l2extRsL2DomAtt'] is not None:
            if managed_object['l2extRsL2DomAtt']['tCl'] == 'l2extDomP':
                info['l2extDomP'] = {}
                info['l2extDomP']['dn'] = managed_object['l2extRsL2DomAtt']['tDn']
                # "tDn": "uni/l2dom-Infra_L2dom"
                info['l2extDomP']['name'] = info['l2extDomP']['dn'].split('/')[1][6:]

        # External EPG
        info['l2extInstP'] = []
        for epg_mo in managed_object['l2extInstP']:
            info['l2extInstP'].append(
                self.get_l2out_ext_epg_info(
                    epg_mo
                )
            )

        return info

    def get_l2outs_info(self, path_info=False):
        if self.l2outs is None:
            l2outs = self.get_l2outs_mo()
            if l2outs is not None:
                self.l2outs = []
                for managed_object in l2outs:
                    self.l2outs.append(
                        self.get_l2out_info(
                            managed_object
                        )
                    )

        if not path_info:
            return self.l2outs

        if self.l2outs_with_path is not None:
            return self.l2outs_with_path

        l2outs_with_path_mo = self.get_l2out_paths_mo()
        if l2outs_with_path_mo is None:
            return None

        self.l2outs_with_path = copy.deepcopy(
            self.l2outs
        )

        for l2out_with_path in self.l2outs_with_path:
            l2out_with_path['path'] = []
            for managed_object in l2outs_with_path_mo:
                if managed_object['tCl'] == 'fabricPathEp':
                    # dn: "uni/tn-k8s/l2out-Test/lnodep-default/lifp-default/rspathL2OutAtt-[topology/pod-1/paths-2207/pathep-[eth1/30]]"
                    path_l2out_tenant = managed_object['dn'].split('/')[1][3:]
                    path_l2out_name = managed_object['dn'].split('/')[2][6:]
                    if path_l2out_tenant != l2out_with_path['tenant']:
                        continue
                    if path_l2out_name != l2out_with_path['name']:
                        continue

                    l2out_with_path['path'].append(
                        managed_object['dn'].split('rspathL2OutAtt-[')[1][:-1]
                    )

        return self.l2outs_with_path

    def match_l2out(self, l2out_info, l2out_filter):
        if l2out_filter is None or len(l2out_filter) == 0:
            return True

        for ap_rule in l2out_filter:
            (key, value) = ap_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, l2out_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, l2out_info['dn']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, l2out_info['tenant']):
                    return False

        return True

    def get_l2outs(self, l2out_filter=None, path_info=False):
        all_l2outs = self.get_l2outs_info(
            path_info=path_info
        )
        if all_l2outs is None:
            return None

        l2outs = []

        for l2out_info in all_l2outs:
            if not self.match_l2out(l2out_info, l2out_filter):
                continue

            l2outs.append(l2out_info)

        l2outs = sorted(
            l2outs,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'l2extOut.info',
            l2outs
        )

        return l2outs
