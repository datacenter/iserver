import copy
import time

from lib import filter_helper
from lib import ip_helper


class VrfInfo():
    def __init__(self):
        self.vrfs = None
        self.vrf_ipv4 = {}
        self.vrf_ipv6 = {}

    def get_vrf_count(self, tenant_name=None):
        vrf_filter = None
        if tenant_name is not None:
            vrf_filter = ['tenant:%s' % (tenant_name)]

        vrfs = self.get_vrfs(
            vrf_filter=vrf_filter
        )
        return len(vrfs)

    def get_vrf_info(self, managed_object):
        keys = [
            'bdEnforcedEnable',
            'descr',
            'dn',
            'ipDataPlaneLearning',
            'knwMcastAct',
            'name',
            'pcEnfDir',
            'pcEnfPref',
            'userdom',
            'vrfIndex'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # [0]: uni/tn-{name}/ctx-{name}
        info['tenant'] = info['dn'].split('/')[1][3:]

        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info

    def get_vrfs_info(self):
        if self.vrfs is not None:
            return self.vrfs

        vrfs_mo = self.get_vrfs_mo()
        if vrfs_mo is not None:
            self.vrfs = []
            for managed_object in vrfs_mo:
                self.vrfs.append(
                    self.get_vrf_info(
                        managed_object
                    )
                )

        return self.vrfs

    def get_vrf_v4_info(self, managed_object):
        # {
        #     "Nhmetric": "0",
        #     "Nhtag": "4294967294",
        #     "PcTag": "0",
        #     "active": "yes",
        #     "addr": "10.5.80.66/32",
        #     "childAction": "",
        #     "createTs": "2023-04-08T00:02:10.000+02:00",
        #     "dn": "topology/pod-1/node-2207/sys/uribv4/dom-k8s:k8s_SRIoV_VRF/db-rt/rt-[15.20.16.0/24]/nh-[static]-[10.5.80.66/32]-[unspecified]-[overlay-1]",
        #     "if": "unspecified",
        #     "metric": "0",
        #     "modTs": "2023-04-08T00:02:10.000+02:00",
        #     "monPolDn": "",
        #     "mplsLabel": "0",
        #     "name": "",
        #     "owner": "static",
        #     "pref": "1",
        #     "routeType": "static",
        #     "rwVnid": "unknown",
        #     "status": "",
        #     "tag": "4294967294",
        #     "type": "attached,direct,pervasive,recursive",
        #     "vrf": "overlay-1"
        # },
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['types'] = info['type'].split(',')

        info['pod'] = ''
        info['node'] = ''
        if info['dn'].split('/')[0] == 'topology':
            info['pod'] = info['dn'].split('/')[1]
            info['node'] = info['dn'].split('/')[2]

        info['prefix'] = info['dn'].split('rt-[')[1].split(']')[0]

        return info

    def get_vrf_v4s_info(self, tenant, name):
        key = '%s:%s' % (tenant, name)
        if key in self.vrf_ipv4:
            return self.vrf_ipv4[key]

        ipv4_mo = self.get_vrf_ipv4_mo(tenant, name)
        if ipv4_mo is not None:
            self.vrf_ipv4[key] = []
            for managed_object in ipv4_mo:
                self.vrf_ipv4[key].append(
                    self.get_vrf_v4_info(
                        managed_object
                    )
                )

        self.vrf_ipv4[key] = sorted(
            self.vrf_ipv4[key],
            key=lambda i: i['prefix']
        )

        return self.vrf_ipv4[key]

    def match_vrf(self, vrf_info, vrf_filter):
        if vrf_filter is None or len(vrf_filter) == 0:
            return True

        for vrf_rule in vrf_filter:
            (key, value) = vrf_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, vrf_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, vrf_info['dn']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, vrf_info['tenant']):
                    return False

            if key == 'bd':
                if 'fvBD' not in vrf_info or vrf_info['fvBD'] is None:
                    return False

                found = False
                for bd_info in vrf_info['fvBD']:
                    if filter_helper.match_string(value, bd_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'epg':
                if 'fvAEPg' not in vrf_info or vrf_info['fvAEPg'] is None:
                    return False

                found = False
                for epg_info in vrf_info['fvAEPg']:
                    if filter_helper.match_string(value, epg_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'l3out':
                if 'l3out' not in vrf_info or vrf_info['l3out'] is None:
                    return False

                found = False
                for l3out_info in vrf_info['l3out']:
                    if filter_helper.match_string(value, l3out_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'subnet':
                if 'fvSubnet' not in vrf_info or vrf_info['fvSubnet'] is None:
                    return False

                found = False
                for bd_subnet in vrf_info['fvSubnet']:
                    if ip_helper.is_subnet_in_subnet(value, bd_subnet['network']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'ip':
                if 'fvSubnet' not in vrf_info or vrf_info['fvSubnet'] is None:
                    return False

                found = False
                for bd_subnet in vrf_info['fvSubnet']:
                    if ip_helper.is_ipv4_in_cidr(value, bd_subnet['network']):
                        found = True
                        break

                if not found:
                    return False

        return True

    def get_vrf(self, vrf_distinguished_name):
        vrf_filter = ['dn:%s' % (vrf_distinguished_name)]
        vrfs = self.get_vrfs(
            vrf_filter=vrf_filter
        )

        if len(vrfs) == 1:
            return vrfs[0]

        return None

    def get_vrfs(self, vrf_filter=None, bridge_domain_info=False, l3out_info=False, epg_info=False, route_info=False):
        start_time = int(time.time() * 1000)

        all_vrfs = self.get_vrfs_info()
        if all_vrfs is None:
            return None

        vrfs = []

        for vrf_info in all_vrfs:
            if epg_info or bridge_domain_info:
                vrf_info['endpointsCount'] = 0

                vrf_info['fvBD'] = copy.deepcopy(
                    self.get_bridge_domains(
                        bridge_domain_filter=['vrf:%s/%s' % (vrf_info['tenant'], vrf_info['name'])],
                        endpoint_info=True
                    )
                )

                vrf_info['fvSubnet'] = []
                for bd_info in vrf_info['fvBD']:
                    vrf_info['fvSubnet'] = vrf_info['fvSubnet'] + bd_info['fvSubnet']
                    vrf_info['endpointsCount'] = vrf_info['endpointsCount'] + bd_info['endpointsCount']

            if epg_info:
                vrf_info['fvAEPg'] = []

                for bd_info in vrf_info['fvBD']:
                    bd_epg_info = copy.deepcopy(
                        self.get_epgs(
                            epg_filter=['bd:%s/%s' % (bd_info['tenant'], bd_info['name'])],
                            bd_info=True,
                            locale_info=True,
                            endpoint_info=True
                        )
                    )
                    if bd_epg_info is not None:
                        vrf_info['fvAEPg'] = vrf_info['fvAEPg'] + bd_epg_info

            if l3out_info:
                vrf_info['l3out'] = copy.deepcopy(
                    self.get_l3outs(
                        l3out_filter=['vrf:%s/%s' % (vrf_info['tenant'], vrf_info['name'])]
                    )
                )

            if not self.match_vrf(vrf_info, vrf_filter):
                continue

            if route_info:
                vrf_info['v4route'] = copy.deepcopy(
                    self.get_vrf_v4s_info(
                        vrf_info['tenant'],
                        vrf_info['name']
                    )
                )

            vrfs.append(vrf_info)

        vrfs = sorted(
            vrfs,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'fvCtx.info',
            vrfs
        )

        return vrfs
