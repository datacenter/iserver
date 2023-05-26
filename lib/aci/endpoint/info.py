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

            if key == 'tenant':
                if not filter_helper.match_string(value, endpoint_info['tenant']):
                    return False

            if key == 'bd':
                if not filter_helper.match_string(value, endpoint_info['bdName']):
                    return False

            if key == 'epg':
                if not filter_helper.match_string(value, endpoint_info['epgName']):
                    return False

            if key == 'ap':
                if not filter_helper.match_string(value, endpoint_info['apName']):
                    return False

            if key == 'vrf':
                if not filter_helper.match_string(value, endpoint_info['vrfName']):
                    return False

            if key == 'bdDn':
                if not filter_helper.match_string(value, endpoint_info['bdDn']):
                    return False

            if key == 'ip':
                found = False
                for ip_address in endpoint_info['fvIp']:
                    if value == ip_address['addr']:
                        found = True
                        break

                if not found:
                    return False

            if key == 'subnet':
                found = False
                for ip_address in endpoint_info['fvIp']:
                    if ip_helper.is_ipv4_in_cidr(ip_address['addr'], value):
                        found = True
                        break

                if not found:
                    return False

            if key == 'vm-info':
                if value not in ['enabled']:
                    self.log.error(
                        'match_endpoint',
                        'Unsupported key:value %s:%s' % (key, value)
                    )

                if value == 'enabled':
                    if endpoint_info['fvRsToVm'] is None:
                        return False

            if key == 'vmm':
                if 'vm' in endpoint_info:
                    if not filter_helper.match_string(value, endpoint_info['vm']['vmm']):
                        return False

            if key == 'hv':
                if 'hv' in endpoint_info:
                    if not filter_helper.match_string(value, endpoint_info['hv']['name']):
                        return False

            if key == 'vm':
                if 'vm' in endpoint_info:
                    if not filter_helper.match_string(value, endpoint_info['vm']['name']):
                        return False

            if key == 'node':
                nodes = value.split(',')
                if 'fabric' in endpoint_info:
                    node_match = False
                    for fabric in endpoint_info['fabric']:
                        if fabric['node_id'] in nodes:
                            node_match = True
                            break

                    if not node_match:
                        return False

        return True

    def get_endpoint_info(self, managed_object):
        # "attributes": {
        #     "annotation": "",
        #     "baseEpgDn": "",
        #     "bdDn": "uni/tn-MPC-E/BD-E-sPBR-IPS-IN_BD",
        #     "childAction": "",
        #     "contName": "mpc-e-IPS-NF32",
        #     "dn": "uni/tn-MPC-E/LDevInst-[uni/tn-MPC-E/lDevVip-IPS]-ctx-MPC-E-sPBR-IN_VRF/G-IPSctxMPC-E-sPBR-IN_VRF-N-E-sPBR-IPS-IN_BD-C-mpc-IPS-IN/cep-00:50:56:B2:82:3A",
        #     "encap": "vlan-3004",
        #     "esgUsegDn": "",
        #     "extMngdBy": "",
        #     "fabricPathDn": "",
        #     "hostingServer": "esx52-eu-spdc.cisco.com",
        #     "id": "0",
        #     "idepdn": "",
        #     "lcC": "vmm",
        #     "lcOwn": "local",
        #     "mac": "00:50:56:B2:82:3A",
        #     "mcastAddr": "not-applicable",
        #     "modTs": "2022-12-22T00:05:11.549+01:00",
        #     "monPolDn": "uni/tn-common/monepg-default",
        #     "name": "00:50:56:B2:82:3A",
        #     "nameAlias": "",
        #     "reportingControllerName": "EU-SPDC-R3DC",
        #     "status": "",
        #     "uid": "0",
        #     "userdom": "all",
        #     "uuid": "",
        #     "vmmSrc": "dvs",
        #     "vrfDn": "uni/tn-MPC-E/ctx-MPC-E-sPBR-IN_VRF"
        # }

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

        # Dn format
        # [0]: uni/tn-{name}/ap-{name}/esg-{name}/cep-{name}
        # [1]: uni/tn-{name}/Tnlepg-{name}/cep-{name}
        # [2]: uni/ldev-[{priKey}]-ctx-[{ctxDn}]-bd-[{bdDn}]/cep-{name}
        # [3]: uni/tn-{name}/LDevInst-[{priKey}]-ctx-{ctxName}/G-{graphRn}-N-{nodeRn}-C-{connRn}/cep-{name}
        # [4]: uni/vDev-[{priKey}]-tn-[{tnDn}]-ctx-{ctxName}/rndrInfo/eppContr/G-{graphRn}-N-{nodeRn}-C-{connRn}/cep-{name}
        # [5]: uni/tn-{name}/ctx-{name}/cep-{name}
        # [6]: uni/tn-{name}/ap-{name}/epg-{name}/cep-{name}
        # [7]: uni/tn-{name}/l2out-{name}/instP-{name}/cep-{name}

        info['tenant'] = ''
        info['vrfTenant'] = ''
        info['vrfCtx'] = ''
        info['vrfName'] = ''
        info['bdTenant'] = ''
        info['bdCtx'] = ''
        info['bdName'] = ''
        info['epgName'] = ''
        info['apName'] = ''

        if info['bdDn'] is not None and len(info['bdDn']) > 0:
            info['bdTenant'] = info['bdDn'].split('/')[1].split('tn-')[1]
            info['bdCtx'] = info['bdDn'].split('/')[2].split('BD-')[1]
            info['bdName'] = '%s/%s' % (
                info['bdTenant'],
                info['bdCtx']
            )

        if info['vrfDn'] is not None and len(info['vrfDn']) > 0:
            info['vrfTenant'] = info['vrfDn'].split('/')[1].split('tn-')[1]
            info['vrfCtx'] = info['vrfDn'].split('/')[2].split('ctx-')[1]
            info['vrfName'] = '%s/%s' % (
                info['vrfTenant'],
                info['vrfCtx']
            )

        if info['dn'].startswith('uni/tn-'):
            info['tenant'] = info['dn'].split('/')[1][3:]

        if info['dn'].startswith('uni/tn-') and '/ap-' in info['dn']:
            info['epgName'] = info['dn'].split('/')[3][4:]
            info['apName'] = info['dn'].split('/')[2][3:]

        info['fvIp'] = []
        for ip_managed_object in managed_object['fvIp']:
            info['fvIp'].append(
                self.get_endpoint_ip_info(
                    ip_managed_object
                )
            )

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
