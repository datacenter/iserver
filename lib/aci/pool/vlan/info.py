import time
from lib import filter_helper


class PoolVlanInfo():
    def __init__(self):
        pass

    def get_pool_vlan_domain_info(self, managed_object):
        keys = [
            'dn',
            'tCl',
            'tDn'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['domainName'] = info['tDn']

        if info['tCl'] == 'l2extDomP':
            info['domainName'] = info['tDn'].split('uni/l2dom-')[1]

        if info['tCl'] == 'l3extDomP':
            info['domainName'] = info['tDn'].split('uni/l3dom-')[1]

        if info['tCl'] == 'physDomP':
            info['domainName'] = info['tDn'].split('uni/phys-')[1]

        if info['tCl'] == 'vmmDomP':
            info['domainName'] = info['tDn'].split('uni/vmmp-VMware/dom-')[1]

        return info

    def get_pool_vlan_block_info(self, managed_object, parent_alloc_mode):
        keys = [
            'allocMode',
            'descr',
            'dn',
            'from',
            'name',
            'rn',
            'role',
            'to'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['allocMode'] == 'inherit':
            info['allocMode'] = parent_alloc_mode

        info['fromVlan'] = info['from'][5:]
        info['toVlan'] = info['to'][5:]
        info['blockInfo'] = '[%s-%s] (%s)' % (
            info['fromVlan'],
            info['toVlan'],
            info['allocMode']
        )

        return info

    def get_pool_vlan_info(self, managed_object):
        keys = [
            'allocMode',
            'descr',
            'dn',
            'name',
            'VlanNsToInterface',
            'VlanNsToVirtualMachines',
            'VlanNsToVmmPortGroups'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['VlanNsToInterface'] is not None:
            for item in info['VlanNsToInterface']:
                item['interface_name'] = None
                if item['ctxClass'] == 'l1PhysIf':
                    item['interface_name'] = item['ctxDn'].split('phys-[')[1].split(']')[0]

        info['fvnsEncapBlk'] = []
        info['vlanCount'] = 0
        info['vlanIds'] = []

        domain_vmm_epg_filter = ['pool:%s' % (info['name'])]
        for block_managed_object in managed_object['fvnsEncapBlk']:
            block_info = self.get_pool_vlan_block_info(
                block_managed_object,
                info['allocMode']
            )

            domain_vmm_epg_filter.append(
                'range:%s,%s' % (
                    block_info['fromVlan'],
                    block_info['toVlan']
                )
            )

            info['vlanCount'] = info['vlanCount'] + int(block_info['toVlan']) - int(block_info['fromVlan']) + 1

            for vlan_id in range(int(block_info['toVlan']), int(block_info['fromVlan']) + 1):
                info['vlanIds'].append(vlan_id)

            info['fvnsEncapBlk'].append(
                block_info
            )

        info['fvnsEncapBlk'] = sorted(
            info['fvnsEncapBlk'],
            key=lambda i: int(i['fromVlan'])
        )

        info['fvnsRtVlanNs'] = []
        for domain_managed_object in managed_object['fvnsRtVlanNs']:
            info['fvnsRtVlanNs'].append(
                self.get_pool_vlan_domain_info(
                    domain_managed_object
                )
            )
        info['fvnsRtVlanNs'] = sorted(
            info['fvnsRtVlanNs'],
            key=lambda i: i['domainName'].lower()
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def match_pool_vlan(self, pool_vlan_info, pool_vlan_filter):
        if pool_vlan_filter is None or len(pool_vlan_filter) == 0:
            return True

        for aepg_rule in pool_vlan_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, pool_vlan_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, pool_vlan_info['dn']):
                    return False

            if key == 'vlan':
                try:
                    vlan_id = int(value)
                except BaseException:
                    return False

                found = False
                for vlan_block_info in pool_vlan_info['fvnsEncapBlk']:
                    if int(vlan_block_info['fromVlan']) <= vlan_id <= int(vlan_block_info['toVlan']):
                        found = True

                if not found:
                    return False

            if key == 'domain':
                found = False
                for domain_info in pool_vlan_info['fvnsRtVlanNs']:
                    if filter_helper.match_string(value, domain_info['domainName']):
                        found = True

                if not found:
                    return False

            if key == 'fault':
                if value == 'any':
                    if not pool_vlan_info['isAnyFault']:
                        return False

        return True

    def get_pool_vlans(
            self,
            pool_vlan_filter=None,
            vlan_usage_info=False,
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
            self.init_pool_vlan_mo()

        all_pools = self.get_pool_vlan_mo(node_info=node_info, cache_enabled=cache_enabled)
        if all_pools is None:
            return None

        pool_vlans = []

        for managed_object in all_pools:
            pool_vlan_info = self.get_pool_vlan_info(
                managed_object
            )

            if not self.match_pool_vlan(pool_vlan_info, pool_vlan_filter):
                continue

            if vlan_usage_info:
                domain_vmm_epg_filter = ['pool:%s' % (pool_vlan_info['name'])]
                pool_vlan_info['epg'] = self.get_domain_vmm_epgs(
                    domain_vmm_epg_filter=domain_vmm_epg_filter
                )

                pool_vlan_info['epgCount'] = len(
                    pool_vlan_info['epg']
                )

                pool_vlan_info['epgUsage'] = '%s/%s' % (
                    pool_vlan_info['epgCount'],
                    pool_vlan_info['vlanCount']
                )

            if fault_info:
                pool_vlan_info['faultInst'] = self.get_pool_vlan_id_fault(
                    pool_vlan_info['name'],
                    'faultInst'
                )

            if hfault_info:
                pool_vlan_info['faultRecord'] = self.get_pool_vlan_id_fault(
                    pool_vlan_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                pool_vlan_info['eventLog'] = self.get_pool_vlan_id_event(
                    pool_vlan_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                pool_vlan_info['auditLog'] = self.get_pool_vlan_id_audit(
                    pool_vlan_info['name'],
                    audit_filter=audit_filter
                )

            pool_vlans.append(pool_vlan_info)

        pool_vlans = sorted(
            pool_vlans,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'fvnsVlanInstP.info',
            pool_vlans
        )

        return pool_vlans

    def get_pool_vlan(self, pool_vlan_name, vlan_usage_info=False, node_info=False, domain_name=None, cache_enabled=True):
        pool_vlan_filter = ['name:%s' % (pool_vlan_name)]
        if domain_name is not None:
            pool_vlan_filter.append(
                'domain:%s' % (domain_name)
            )

        vlans = self.get_pool_vlans(
            pool_vlan_filter=pool_vlan_filter,
            vlan_usage_info=vlan_usage_info,
            node_info=node_info,
            cache_enabled=cache_enabled
        )

        if vlans is None or len(vlans) == 0:
            return None

        if len(vlans) > 1:
            return None

        return vlans[0]

    def is_pool_vlan(self, pool_vlan_name, cache_enabled=True):
        if self.get_pool_vlan(pool_vlan_name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def wait_pool_vlan(self, pool_vlan_name, max_time=180):
        start_time = int(time.time())
        while True:
            if self.is_pool_vlan(pool_vlan_name, cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'aci.wait_pool_vlan',
                    'Max time reached: %s' % (pool_vlan_name)
                )
                return False

            time.sleep(5)

    def check_pool_vlan_consistency(self, blocks, values):
        requested = filter_helper.get_range_from_values(values)

        vlans = []
        for block in blocks:
            if block['fromVlan'] == block['toVlan']:
                vlans.append(block['fromVlan'])
            else:
                vlans.append('%s-%s' % (block['fromVlan'], block['toVlan']))

        configured = filter_helper.get_range_from_values(vlans)

        inconsistent = []
        for vlan in vlans:
            if vlan not in configured:
                inconsistent.append(vlan)

        return inconsistent
