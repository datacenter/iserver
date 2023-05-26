from lib import filter_helper


class InterfacePortChannelInfo():
    def __init__(self):
        self.interfaces_pc = {}

    def get_interface_port_channel_count(self, pod_id, node_id):
        interfaces = self.get_interface_port_channels(pod_id, node_id)
        return len(interfaces)

    def get_interface_port_channel_state_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'accessVlan',
            'activeMbrs',
            'allowedVlans',
            'backplaneMac',
            'bundleBupId',
            'bundleIndex',
            'cfgAccessVlan',
            'cfgNativeVlan',
            'errVlans',
            'hwBdId',
            'hwResourceId',
            'intfT',
            'iod',
            'lastErrors',
            'lastLinkStChg',
            'nativeVlan',
            'numActivePorts',
            'numMbrUp',
            'operDceMode',
            'operDuplex',
            'operMode',
            'operRouterMac',
            'operSpeed',
            'operSt',
            'operStQual',
            'operVlans',
            'primaryVlan'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['portId'] = []
        for active_member in managed_object['activeMbrs'].split(','):
            if active_member != 'unspecified':
                info['portId'].append(active_member)

        info['portIds'] = ','.join(info['portId'])

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
            if info['operStQual'] == 'none':
                info['operStQual'] = ''
        else:
            info['__Output']['operSt'] = 'Red'

        if info['accessVlan'] == 'unknown':
            info['accessVlan'] = ''

        if info['nativeVlan'] == 'unknown':
            info['nativeVlan'] = ''

        if info['cfgAccessVlan'] == 'unknown':
            info['cfgAccessVlan'] = ''

        if info['cfgNativeVlan'] == 'unknown':
            info['cfgNativeVlan'] = ''

        return info

    def get_interface_port_channel_info(self, managed_object):
        keys = [
            'activePorts',
            'adminSt',
            'autoNeg',
            'bw',
            'ctrl',
            'delay',
            'dn',
            'dot1qEtherType',
            'ethpmCfgFailedBmp',
            'ethpmCfgFailedTs',
            'ethpmCfgState',
            'fcotChannelNumber',
            'fop',
            'hashDist',
            'id',
            'iod',
            'isPlatformSupported',
            'isReflectiveRelayCfgSupported',
            'lastBundleMbr',
            'lastBundleTime',
            'lastSt',
            'lastStCause',
            'lastUnbundleMbr',
            'lastUnbundleTime',
            'layer',
            'linkDebounce',
            'ltl',
            'maxActive',
            'maxLinks',
            'mdix',
            'medium',
            'minLinks',
            'mode',
            'mtu',
            'name',
            'operChannelMode',
            'pcId',
            'pcMode',
            'pcmCfgFailedBmp',
            'pcmCfgFailedTs',
            'pcmCfgState',
            'portT',
            'prioFlowCtrl',
            'reflectiveRelayEn',
            'routerMac',
            'snmpTrapSt',
            'spanMode',
            'speed',
            'suspMinlinks',
            'switchingSt',
            'usage'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['state'] = self.get_interface_port_channel_state_info(managed_object['ethpmAggrIf'])
        info['state'] = self.my_output.merge_output(
            info['state']
        )

        # topology/pod-1/node-201/sys/aggr-[po15]
        info['podId'] = info['dn'].split('/')[1].split('-')[1]
        info['nodeId'] = info['dn'].split('/')[2].split('-')[1]

        info['apic'] = self.apic_label
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
        )

        info['layerT'] = ''
        if info['layer'] == 'Layer2':
            info['layerT'] = 'switched'
        if info['layer'] == 'Layer3':
            info['layerT'] = 'routed'

        info['__Output']['id'] = 'Blue'

        if info['adminSt'] == 'up':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['switchingSt'] == 'enabled':
            info['__Output']['switchingSt'] = 'Green'
        else:
            info['__Output']['switchingSt'] = 'Red'

        if info['pcMode'] == 'active':
            info['__Output']['pcMode'] = 'Green'
        else:
            info['__Output']['pcMode'] = 'Red'

        if info['operChannelMode'] == 'active':
            info['__Output']['operChannelMode'] = 'Green'
        else:
            info['__Output']['operChannelMode'] = 'Red'

        if info['activePorts'] == '0':
            info['__Output']['activePorts'] = 'Red'

        info['up'] = False
        if info['adminSt'] == 'up' and info['state']['operSt'] == 'up':
            info['up'] = True

        return info

    def get_interface_port_channels_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_pc:
            return self.interfaces_pc[key]

        interfaces_pc_mo = self.get_interface_port_channels_mo(pod_id, node_id)
        if interfaces_pc_mo is not None:
            self.interfaces_pc[key] = []
            for interface_pc_mo in interfaces_pc_mo:
                self.interfaces_pc[key].append(
                    self.get_interface_port_channel_info(
                        interface_pc_mo
                    )
                )

        self.log.apic_mo(
            'pcAggrIf.info.%s' % (key),
            self.interfaces_pc[key]
        )

        return self.interfaces_pc[key]

    def match_interface_port_channel(self, interface_port_channel_info, interface_port_channel_filter):
        if interface_port_channel_filter is None or len(interface_port_channel_filter) == 0:
            return True

        for ap_rule in interface_port_channel_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_port_channel_info['id']):
                    return False

            if key == 'name':
                if not filter_helper.match_string(value, interface_port_channel_info['name']):
                    return False

            if key == 'domain':
                if 'vpcDomain' in interface_port_channel_info:
                    if not filter_helper.match_string(value, interface_port_channel_info['vpcDomain']):
                        return False

            if key == 'speed':
                if not filter_helper.match_string(value, interface_port_channel_info['state']['operSpeed']):
                    return False

            if key == 'state':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_port_channel_info['state']['operSt']):
                        return False

        return True

    def get_interface_port_channel(self, pod_id, node_id, interface_port_channel_filter=None, vpc_domain_info=False, vpc_domains=None, members_info=False, instance_info=False):
        all_interface_port_channels = self.get_interface_port_channels_info(pod_id, node_id)
        if all_interface_port_channels is None:
            return None

        interface_port_channels = []

        for interface_port_channel_info in all_interface_port_channels:
            if not self.match_interface_port_channel(interface_port_channel_info, interface_port_channel_filter):
                continue

            if members_info:
                interface_port_channel_info['members'] = self.get_interface_port_channel_lacp_members(
                    pod_id,
                    node_id,
                    interface_port_channel_info['state']['portId']
                )

            if instance_info:
                interface_port_channel_info['lacp'] = self.get_lacp_instance(
                    pod_id,
                    node_id
                )

            if vpc_domain_info:
                interface_port_channel_info['vpcDomain'] = ''
                interface_port_channel_info['__Output']['vpcDomain'] = 'Yellow'
                if vpc_domains is None:
                    vpc_domains = self.get_interface_virtual_port_channel(
                        pod_id=pod_id,
                        node_id=node_id,
                        members_info=True
                    )

                for vpc_domain in vpc_domains:
                    for vpc_domain_member in vpc_domain['members']:
                        if vpc_domain_member['name'] == interface_port_channel_info['name']:
                            interface_port_channel_info['vpcDomain'] = vpc_domain['id']
                            break

                if not self.match_interface_port_channel(interface_port_channel_info, interface_port_channel_filter):
                    continue

            interface_port_channels.append(
                interface_port_channel_info
            )

        interface_port_channels = sorted(
            interface_port_channels,
            key=lambda i: int(i['id'][2:])
        )

        return interface_port_channels

    def get_interface_port_channel_summary(self, pod_id, node_id):
        ports = self.get_interface_port_channel(
            pod_id,
            node_id
        )

        if ports is None:
            return None

        summary = {}
        summary['__Output'] = {}
        summary['portUp'] = 0
        summary['portDown'] = 0
        summary['portCount'] = 0

        for port in ports:
            if port['up']:
                summary['portUp'] = summary['portUp'] + 1

            if not port['up']:
                summary['portDown'] = summary['portDown'] + 1

        summary['portCount'] = summary['portUp'] + summary['portDown']

        (summary['portSummary'], summary['__Output']['portSummary']) = self.get_interface_summary_output(
            summary['portUp'],
            summary['portDown'],
            summary['portCount']
        )

        return summary
