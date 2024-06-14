import copy

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
            'pcTag',
            'seg',
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

        # pcTag Number Ranges
        # System Reserved pcTag – This pcTag is used for system internal rules (1-15).
        # Globally scoped pcTag – This pcTag is used for shared service (16-16385).
        # Locally scoped pcTag – This pcTag is locally used per VRF (range from 16386-65535).
        info['pcTagT'] = info['pcTag']
        if 15 < int(info['pcTag']) < 16386:
            info['pcTagT'] = '%s (global)' % (info['pcTag'])
            info['__Output']['pcTagT'] = 'Red'

        if int(info['pcTag']) < 16:
            info['pcTagT'] = '%s (system)' % (info['pcTag'])
            info['__Output']['pcTagT'] = 'Red'

        if info['ipDataPlaneLearning'] == 'enabled':
            info['ipDataPlaneLearningTick'] = '\u2713'
        else:
            info['ipDataPlaneLearningTick'] = '\u2717'

        if info['bdEnforcedEnable'] == 'yes':
            info['bdEnforcedEnableTick'] = '\u2713'
        else:
            info['bdEnforcedEnableTick'] = '\u2717'

        if info['knwMcastAct'] == 'permit':
            info['knwMcastActTick'] = '\u2713'
        else:
            info['knwMcastActTick'] = '\u2717'

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
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, vrf_info['nameTenant']):
                    return False

            if key == 'dn':
                key_found = True
                if not filter_helper.match_string(value, vrf_info['dn']):
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, vrf_info['tenant']):
                    return False

            if key == 'bd':
                key_found = True

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
                key_found = True

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
                key_found = True

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
                key_found = True

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
                key_found = True

                if 'fvSubnet' not in vrf_info or vrf_info['fvSubnet'] is None:
                    return False

                found = False
                for bd_subnet in vrf_info['fvSubnet']:
                    if ip_helper.is_ipv4_in_cidr(value, bd_subnet['network']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'pctag':
                key_found = True

                if value == 'global':
                    if int(vrf_info['pcTag']) >= 16386:
                        return False

                if value == 'system':
                    if int(vrf_info['pcTag']) >= 16:
                        return False

                if value not in ['global', 'system']:
                    if not filter_helper.match_integer(value, vrf_info['pcTag']):
                        return False

            if key == 'vnid':
                key_found = True

                if not filter_helper.match_integer(value, vrf_info['seg']):
                    return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not vrf_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_vrf',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_vrf',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_vrf(self, vrf_distinguished_name):
        vrf_filter = ['dn:%s' % (vrf_distinguished_name)]
        vrfs = self.get_vrfs(
            vrf_filter=vrf_filter
        )

        if len(vrfs) == 1:
            return vrfs[0]

        return None

    def get_vrfs(
            self,
            vrf_filter=None,
            bridge_domain_info=False,
            l3out_info=False,
            epg_info=False,
            route_info=False,
            node_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_vrfs = self.get_vrfs_info()
        if all_vrfs is None:
            return None

        vrfs = []

        for vrf_info in all_vrfs:
            if epg_info or bridge_domain_info:
                vrf_info['endpointCount'] = 0

                vrf_info['fvBD'] = copy.deepcopy(
                    self.get_bridge_domains(
                        bridge_domain_filter=['vrf:%s/%s' % (vrf_info['tenant'], vrf_info['name'])],
                        endpoint_info=True
                    )
                )

                vrf_info['fvSubnet'] = []
                for bd_info in vrf_info['fvBD']:
                    vrf_info['fvSubnet'] = vrf_info['fvSubnet'] + bd_info['fvSubnet']
                    vrf_info['endpointCount'] = vrf_info['endpointCount'] + bd_info['endpointCount']

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

            if node_info:
                ap_node_info = self.get_vrf_node(
                    vrf_info['tenant'],
                    vrf_info['name']
                )
                vrf_info['node'] = None
                vrf_info['interface'] = None
                if ap_node_info is not None:
                    vrf_info['node'] = ap_node_info['node']
                    vrf_info['interface'] = ap_node_info['interface']

            if fault_info:
                vrf_info['faultInst'] = self.get_vrf_id_fault(
                    vrf_info['tenant'],
                    vrf_info['name'],
                    'faultInst'
                )

            if hfault_info:
                vrf_info['faultRecord'] = self.get_vrf_id_fault(
                    vrf_info['tenant'],
                    vrf_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                vrf_info['eventLog'] = self.get_vrf_id_event(
                    vrf_info['tenant'],
                    vrf_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                vrf_info['auditLog'] = self.get_vrf_id_audit(
                    vrf_info['tenant'],
                    vrf_info['name'],
                    audit_filter=audit_filter
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
