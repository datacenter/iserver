import time
import copy

from lib import filter_helper
from lib import ip_helper


class EpgStatsInfo():
    def __init__(self):
        self.epg_stats = None

    def is_epg_pkey(self, epg_pkey, key1, key2, key3):
        # uni/tn-iks-monitoring/ap-Vitria-Monitoring_ANP/epg-Vitria-Mon-BackEnd
        if not epg_pkey.split('/')[1].startswith('%s-' % (key1)):
            return False

        if not epg_pkey.split('/')[2].startswith('%s-' % (key2)):
            return False

        if not epg_pkey.split('/')[3].startswith('%s-' % (key3)):
            return False

        return True

    def get_epg_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        info['dn'] = managed_object['dn']

        # "resPolCont/rtdOutCont/rtdOutDef-[{outDn}]/node-{id}/stnodeatt",
        # "uni/epp/sec-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/cld-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/tnlp-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/instp-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/vns-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/inb-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/oob-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/node-{id}/stnodeatt",
        # "uni/epp/fv-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/rtd-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/br-[{epgPKey}]/node-{id}/stnodeatt",
        # "uni/epp/node-{id}/stnodeatt",
        # "uni/epp/node-{id}/stnodeatt"

        if 'uni/epp/node-' in info['dn']:
            self.log.error(
                'get_epg_stats_info_common',
                'Unsupported dn: %s' % (info['dn'])
            )
            return None

        info['node_id'] = managed_object['dn'].split(']')[1].split('/')[1].split('-')[1]
        info['type'] = managed_object['type']

        info['aae'] = None
        info['pg'] = None
        info['interface_id'] = None
        info['lsnode'] = None

        info['epg_dn'] = ''.join(managed_object['dn'].split(']/node-')[0].split('[')[1:])
        epg_resolved = False

        if info['dn'].startswith('uni/epp/fv-'):
            # "dn": "uni/epp/fv-[uni/tn-iks-monitoring/ap-Vitria-Monitoring_ANP/epg-Vitria-Mon-BackEnd]/node-206/attEntitypathatt-[UCSB1_AAEP]"
            # "dn": "uni/epp/fv-[uni/tn-MPC-F5T/ap-F5_ANP/epg-F5_OUT]/node-206/dyatt-[topology/pod-1/node-206/sys/lsnode-10.58.24.17]"
            # "dn": "uni/epp/fv-[uni/tn-P5G/ap-P5G_App/epg-P5G-mgmt]/node-201/dyatt-[topology/pod-1/paths-201/pathep-[eth1/34]]"
            if self.is_epg_pkey(info['epg_dn'], 'tn', 'ap', 'epg'):
                info['tenant'] = info['epg_dn'].split('/')[1][3:]
                info['domain'] = info['epg_dn'].split('/')[2][3:]
                info['name'] = info['epg_dn'].split('/')[3][4:]
                info['path'] = 'epg'

                if managed_object['type'] == 'fvAttEntityPathAtt':
                    info['aae'] = managed_object['pathName']
                    epg_resolved = True

                if managed_object['type'] == 'fvStPathAtt':
                    info['interface_id'] = managed_object['pathName']
                    epg_resolved = True

                if managed_object['type'] == 'fvDyPathAtt':
                    item = managed_object['dn'].split('/')[-1]
                    if '/pathep-[' in managed_object['dn']:
                        info['interface_id'] = managed_object['dn'].split('/pathep-[')[1].split(']')[0]
                        epg_resolved = True

                    if '/lsnode-' in managed_object['dn']:
                        info['lsnode'] = managed_object['dn'].split('/lsnode-')[1].split(']')[0]
                        epg_resolved = True

        if managed_object['type'] == 'fvDyPathAtt':
            # uni/epp/fv-[uni/tn-MPC/LDevInst-[uni/tn-MPC/lDevVip-IPS]-ctx-MPC-sPBR-IN_VRF/G-IPSctxMPC-sPBR-IN_VRF-N-sPBR-IPS-IN_BD-C-mpc-IPS-IN]/node-205/dyatt-[topology/pod-1/node-205/sys/lsnode-10.58.24.17]
            if info['epg_dn'].split('/')[2].startswith('LDevInst-'):
                info['tenant'] = info['epg_dn'].split('/')[1][3:]
                info['domain'] = 'unknown'
                info['name'] = 'unknown'
                info['path'] = 'graph'
                epg_resolved = True

        # "dn": "uni/epp/br-[uni/tn-common/l2out-VNF-mgmt_L2out/instP-VNF-mgmt_L2ext]/node-201/stpathatt-[Infra_PolGrp]"
        if info['dn'].startswith('uni/epp/br-'):
            if self.is_epg_pkey(info['epg_dn'], 'tn', 'l2out', 'instP'):
                info['tenant'] = info['epg_dn'].split('/')[1][3:]
                info['domain'] = info['epg_dn'].split('/')[2][6:]
                info['name'] = info['epg_dn'].split('/')[3][6:]
                info['path'] = 'l2out'
                info['pg'] = managed_object['pathName']
                epg_resolved = True

        # 'dn': 'uni/epp/rtd-[uni/tn-infra/out-multipodL3Out/instP-ipnInstP]/node-101/stpathatt-[eth1/16]'
        if info['dn'].startswith('uni/epp/rtd-'):
            if self.is_epg_pkey(info['epg_dn'], 'tn', 'out', 'instP'):
                info['tenant'] = info['epg_dn'].split('/')[1][3:]
                info['domain'] = info['epg_dn'].split('/')[2][6:]
                info['name'] = info['epg_dn'].split('/')[3][6:]
                info['path'] = 'l3out'
                info['interface_id'] = managed_object['pathName']
                epg_resolved = True

        # 'dn': 'resPolCont/rtdOutCont/rtdOutDef-[uni/tn-infra/out-RL-L3Out]/node-302/stpathatt-[eth1/36]'
        if info['dn'].startswith('resPolCont/'):
            info['tenant'] = 'unknown'
            info['domain'] = 'unknown'
            info['name'] = 'unknown'
            info['path'] = 'l3out'
            info['interface_id'] = managed_object['pathName']
            epg_resolved = True

        if not epg_resolved:
            self.log.error(
                'get_epg_stats_info_common',
                'Unsupported epg dn: %s' % (managed_object)
            )
            return None

        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )
        info['nameDomainTenant'] = '%s/%s/%s' % (
            info['tenant'],
            info['domain'],
            info['name']
        )

        return info

    def get_epgs_stats_info(self):
        if self.epg_stats is not None:
            return self.epg_stats

        managed_objects = self.get_epg_stats_mo()
        if managed_objects is None:
            return None

        self.epg_stats = []
        for managed_object in managed_objects:
            epg_stats_info = self.get_epg_stats_info(
                managed_object
            )
            if epg_stats_info is None:
                return self.epg_stats

            if epg_stats_info is not None:
                self.epg_stats.append(
                    epg_stats_info
                )

        self.log.apic_mo(
            'fvAPathAtt.info',
            self.epg_stats
        )

        return self.epg_stats

    def match_epg(self, epg_info, epg_filter):
        if epg_filter is None or len(epg_filter) == 0:
            return True

        for aepg_rule in epg_filter:
            (key, value) = aepg_rule.split(':')

        return True

    def get_epgs_stats(self, epg_stats_filter=None):
        all_stats = self.get_epgs_stats_info()
        if all_stats is None:
            return None

        stats = []
        for epg_stats_info in all_stats:
            if not self.match_epg(epg_stats_info, epg_stats_filter):
                continue

            stats.append(epg_stats_info)

        return stats
