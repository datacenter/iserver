from lib import ip_helper
from lib import filter_helper


class EndpointInfo():
    def __init__(self):
        self.endpoints = None

    def get_endpoint_count(self, tenant_name=None):
        endpoint_filter = []
        if tenant_name is not None:
            endpoint_filter.append(
                'tenant:%s' % (tenant_name)
            )

        endpoints = self.get_endpoints(
            endpoint_filter=endpoint_filter
        )
        return len(endpoints)

    def get_endpoint_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'bdDn',
            'dn',
            'encap',
            'fabricPathDn',
            'lcC',
            'lcOwn',
            'mac',
            'name',
            'userdom',
            'vrfDn'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['flags'] = ''
        if 'learned' in managed_object['lcC'].split(','):
            info['flags'] = '%sL' % (info['flags'])
        if 'vmm' in managed_object['lcC'].split(','):
            info['flags'] = '%sV' % (info['flags'])

        info['encapT'] = info['encap']
        info['encapVlan'] = info['encap']
        if info['encap'].startswith('vlan-'):
            info['encapVlan'] = info['encap'].split('vlan-')[1]

        # Dn format
        # [0]: uni/tn-{name}/ap-{name}/esg-{name}/cep-{name}
        # [1]: uni/tn-{name}/Tnlepg-{name}/cep-{name}
        # [2]: uni/ldev-[{priKey}]-ctx-[{ctxDn}]-bd-[{bdDn}]/cep-{name}
        # [3]: uni/tn-{name}/LDevInst-[{priKey}]-ctx-{ctxName}/G-{graphRn}-N-{nodeRn}-C-{connRn}/cep-{name}
        # [4]: uni/vDev-[{priKey}]-tn-[{tnDn}]-ctx-{ctxName}/rndrInfo/eppContr/G-{graphRn}-N-{nodeRn}-C-{connRn}/cep-{name}
        # [5]: uni/tn-{name}/ctx-{name}/cep-{name}
        # [6]: uni/tn-{name}/ap-{name}/epg-{name}/cep-{name}
        # [7]: uni/tn-{name}/l2out-{name}/instP-{name}/cep-{name}

        info['apic'] = self.apic_name
        info['tenant'] = ''
        info['vrfTenant'] = ''
        info['vrfName'] = ''
        info['vrfNameTenant'] = ''
        info['bdTenant'] = ''
        info['bdName'] = ''
        info['bdNameTenant'] = ''
        info['epgName'] = ''
        info['apName'] = ''
        info['epgNameApTenant'] = ''

        if info['bdDn'] is not None and len(info['bdDn']) > 0:
            info['bdTenant'] = info['bdDn'].split('/')[1].split('tn-')[1]
            info['bdName'] = info['bdDn'].split('/')[2].split('BD-')[1]
            info['bdNameTenant'] = '%s/%s' % (
                info['bdTenant'],
                info['bdName']
            )

        if info['vrfDn'] is not None and len(info['vrfDn']) > 0:
            info['vrfTenant'] = info['vrfDn'].split('/')[1].split('tn-')[1]
            info['vrfName'] = info['vrfDn'].split('/')[2].split('ctx-')[1]
            info['vrfNameTenant'] = '%s/%s' % (
                info['vrfTenant'],
                info['vrfName']
            )

        if info['dn'].startswith('uni/tn-'):
            info['tenant'] = info['dn'].split('/')[1][3:]

        if info['dn'].startswith('uni/tn-') and '/ap-' in info['dn']:
            info['epgName'] = info['dn'].split('/')[3][4:]
            info['apName'] = info['dn'].split('/')[2][3:]
            info['epgNameApTenant'] = '%s/%s/%s' % (
                info['tenant'],
                info['apName'],
                info['epgName']
            )

        info['fvIp'] = []
        address = []
        for ip_managed_object in managed_object['fvIp']:
            ip_info = self.get_endpoint_ip_info(
                ip_managed_object
            )
            info['fvIp'].append(
                ip_info
            )
            address.append(ip_info['addr'])

        info['ip'] = ','.join(address)

        info['fvRsToVm'] = None
        if 'fvRsToVm' in managed_object and managed_object['fvRsToVm'] is not None:
            info['fvRsToVm'] = self.get_endpoint_vm_info(
                managed_object['fvRsToVm']
            )

        info['fvRsHyper'] = None
        if 'fvRsHyper' in managed_object and managed_object['fvRsHyper'] is not None:
            info['fvRsHyper'] = self.get_endpoint_hv_info(
                managed_object['fvRsHyper']
            )

        if len(info['fabricPathDn']) == 0:
            if managed_object['fvRsCEpToPathEp'] is not None:
                if 'tDn' in managed_object['fvRsCEpToPathEp']:
                    info['fabricPathDn'] = managed_object['fvRsCEpToPathEp']['tDn']

        return info

    def get_endpoints_info(self):
        if self.endpoints is not None:
            return self.endpoints

        managed_objects = self.get_endpoints_mo()
        if managed_objects is None:
            return None

        self.endpoints = []
        for managed_object in managed_objects:
            self.endpoints.append(
                self.get_endpoint_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'fvCEp.info',
            self.endpoints
        )

        return self.endpoints

    def match_endpoint(self, endpoint_info, endpoint_filter):
        if endpoint_filter is None or len(endpoint_filter) == 0:
            return True

        # support multiple mac: filtering with 'or' logic

        mac_filtering = False
        mac_match = False
        for rule in endpoint_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            if key == 'mac':
                mac_filtering = True
                if ip_helper.is_mac_match(value, endpoint_info['mac']):
                    mac_match = True

        if mac_filtering and not mac_match:
            return False

        for rule in endpoint_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])
            key_found = False

            if key == 'mac':
                key_found = True

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, endpoint_info['tenant']):
                    return False

            if key == 'bd':
                key_found = True
                if not filter_helper.match_tenant_name(value, endpoint_info['bdNameTenant']):
                    return False

            if key == 'epg':
                key_found = True
                if not filter_helper.match_tenant_ap_name(value, endpoint_info['epgNameApTenant']):
                    return False

            if key == 'ap':
                key_found = True
                if not filter_helper.match_string(value, endpoint_info['apName']):
                    return False

            if key == 'vrf':
                key_found = True
                if not filter_helper.match_tenant_name(value, endpoint_info['vrfNameTenant']):
                    return False

            if key == 'bdDn':
                key_found = True
                if not filter_helper.match(value, endpoint_info['bdDn']):
                    return False

            if key == 'vlan':
                key_found = True
                if not filter_helper.match_integer(value, endpoint_info['encapVlan']):
                    return False

            if key == 'ip':
                key_found = True
                found = False
                for ip_address in endpoint_info['fvIp']:
                    if value == ip_address['addr']:
                        found = True
                        break

                if not found:
                    return False

            if key == 'subnet':
                key_found = True
                found = False
                for ip_address in endpoint_info['fvIp']:
                    if ip_helper.is_ipv4_in_cidr(ip_address['addr'], value):
                        found = True
                        break

                if not found:
                    return False

            if key == 'vm-info':
                key_found = True
                if value not in ['enabled']:
                    self.log.error(
                        'match_endpoint',
                        'Unsupported key:value %s:%s' % (key, value)
                    )

                if value == 'enabled':
                    if endpoint_info['fvRsToVm'] is None:
                        return False

            if key == 'vmm':
                key_found = True
                if 'vm' in endpoint_info:
                    if not filter_helper.match_string(value, endpoint_info['vm']['vmm']):
                        return False

            if key == 'hv':
                key_found = True
                if 'hv' in endpoint_info:
                    if not filter_helper.match_string(value, endpoint_info['hv']['name']):
                        return False

            if key == 'vm':
                key_found = True
                if 'vm' in endpoint_info:
                    if not filter_helper.match_string(value, endpoint_info['vm']['name']):
                        return False

            if key == 'node':
                key_found = True
                nodes = value.split(',')
                if 'fabric' in endpoint_info:
                    node_match = False
                    for fabric in endpoint_info['fabric']:
                        if fabric['node_id'] in nodes:
                            node_match = True
                            break

                    if not node_match:
                        return False

            if not key_found:
                self.log.error(
                    'match_endpoint',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_endpoints(self, endpoint_filter=None, vm_info=False, fabric_info=False):
        all_endpoints = self.get_endpoints_info()
        if all_endpoints is None:
            return None

        endpoints = []

        for endpoint_info in all_endpoints:
            if not self.match_endpoint(endpoint_info, endpoint_filter):
                continue

            if vm_info:
                if 'fvRsToVm' in endpoint_info and endpoint_info['fvRsToVm'] is not None:
                    vm_dn = endpoint_info['fvRsToVm']['tDn']
                    vm_mac = endpoint_info['mac']
                    hv_dn = endpoint_info['fvRsHyper']['tDn']

                    endpoint_info['vm'] = self.get_endpoint_vmm_vm(
                        vm_filter=['dn:%s' % (vm_dn)],
                        expected_single=True
                    )

                    endpoint_info['vnic'] = self.get_endpoint_vmm_vnic(
                        vm_filter=[
                            'dn:%s' % (vm_dn),
                            'mac:%s' % (vm_mac)
                        ],
                        expected_single=True
                    )

                    endpoint_info['hv'] = self.get_endpoint_vmm_hv(
                        vm_filter=['dn:%s' % (hv_dn)],
                        expected_single=True
                    )

                    if not self.match_endpoint(endpoint_info, endpoint_filter):
                        continue

            if fabric_info:
                endpoint_info['fabric'] = self.get_fabric_path_ports(
                    endpoint_info['fabricPathDn'],
                    resolve=True
                )
                if not self.match_endpoint(endpoint_info, endpoint_filter):
                    continue

            endpoints.append(endpoint_info)

        endpoints = sorted(
            endpoints,
            key=lambda i: i['mac']
        )

        return endpoints
