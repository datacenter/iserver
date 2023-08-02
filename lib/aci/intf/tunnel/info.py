from lib import filter_helper
from lib import ip_helper


class InterfaceTunnelInfo():
    def __init__(self):
        self.interface_tunnel = {}

        self.interface_tunnel_endpoint_type = {
            'physical': 'Physical',
            'proxy-acast-mac': 'Proxy Anycast MAC',
            'proxy-acast-v4': 'Proxy Anycast IPv4',
            'proxy-acast-v6': 'Proxy Anycast IPv6',
            'fabric-ext': 'Fabric External',
            'rl-mcast-hrep': 'Remote Leaf Multicast',
            'rl-ucast': 'Remote Leaf Unicast'
        }

    def get_interface_tunnel_summary(self, pod_id, node_id):
        ports = self.get_interfaces_tunnel(
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

    def get_interface_tunnel_count(self, pod_id, node_id):
        interfaces = self.get_interfaces_tunnel(pod_id, node_id)
        return len(interfaces)

    def get_interface_tunnel_info(self, managed_object):
        keys = [
            'aclTcamStQual',
            'adminSt',
            'cfgdMtu',
            'delInProg',
            'dest',
            'dn',
            'id',
            'idRequestorDn',
            'iod',
            'keepAlvIntvl',
            'keepAlvRetries',
            'mac',
            'operSt',
            'operStQual',
            'src',
            'tLayer',
            'tType',
            'tmCfgFailedBmp',
            'tmCfgFailedTs',
            'tmCfgState',
            'type',
            'underlayVrfName',
            'v6Src',
            'vrfName'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # topology/pod-1/node-201/sys/tunnel/inst/if-[eth1/97]
        info['podId'] = info['dn'].split('/')[1].split('-')[1]
        info['nodeId'] = info['dn'].split('/')[2].split('-')[1]

        info['apic'] = self.apic_name
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
        )

        info['src_ip'] = info['src']
        if info['src'].endswith('/32'):
            info['src_ip'] = info['src_ip'].split('/32')[0]

        info['dest_ip'] = info['dest']
        if info['dest'].endswith('/32'):
            info['dest_ip'] = info['dest_ip'].split('/32')[0]

        info['typeT'] = []
        for tunnel_type in info['type'].split(','):
            if tunnel_type in self.interface_tunnel_endpoint_type:
                info['typeT'].append(
                    self.interface_tunnel_endpoint_type[tunnel_type]
                )
            else:
                info['typeT'].append(
                    tunnel_type
                )

        info['typeT'] = sorted(
            info['typeT']
        )

        info['tunnelId'] = int(info['id'].strip('tunnel'))
        info['__Output']['id'] = 'Blue'

        if info['adminSt'] == 'up':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
            if info['operStQual'] == 'none':
                info['operStQual'] = ''
        else:
            info['__Output']['operSt'] = 'Red'

        if info['adminSt'] == 'up' and info['operSt'] == 'up':
            info['up'] = True
        else:
            info['up'] = False

        info['requestor'] = ''
        if len(info['idRequestorDn']) > 0:
            if info['idRequestorDn'].startswith('topology'):
                if len(info['idRequestorDn'].split('/')) > 4:
                    info['requestor'] = info['idRequestorDn'].split('/')[4]

        info['dest_node'] = []

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

    def get_interface_tunnel_info_resolved(self, info):
        tep_found = False
        nodes = self.get_nodes()
        for node in nodes:
            node_address_info = self.get_node_address_ipv4(
                node['podId'],
                node['id'],
                address_filter=['ip:%s' % (info['dest_ip'])]
            )
            if node_address_info is not None and len(node_address_info) == 1:
                tep_found = True
                info['dest_node'].append(
                    'pod-%s/%s/%s' % (
                        node['podId'],
                        node['name'],
                        node_address_info[0]['interface']
                    )
                )

        if not tep_found:
            # Tunnel destined to node (tep)
            destination_node_info = self.get_node(
                node_ip=info['dest_ip']
            )
            if destination_node_info is not None:
                info['dest_node'].append(
                    destination_node_info['pod_node_name']
                )
                tep_found = True

        return info

    def get_interfaces_tunnel_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_tunnel:
            return self.interface_tunnel[key]

        interfaces_mo = self.get_interface_tunnel_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_tunnel[key] = []
        for interface_mo in interfaces_mo:
            self.interface_tunnel[key].append(
                self.get_interface_tunnel_info(
                    interface_mo
                )
            )

        self.log.apic_mo(
            'tunnelIf.info.%s' % (key),
            self.interface_tunnel[key]
        )

        return self.interface_tunnel[key]

    def match_interface_tunnel(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            if key == 'admin':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['adminSt']):
                        return False

            if key == 'oper':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['operSt']):
                        return False

            if key == 'vrf':
                if not filter_helper.match_string(value, interface_info['vrfName']):
                    return False

            if key == 'layer':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['tLayer']):
                        return False

            if key == 'ip':
                if not filter_helper.match_string(value, interface_info['src_ip']) and not filter_helper.match_string(value, interface_info['dest']):
                    return False

            if key == 'subnet':
                if not ip_helper.is_ipv4_in_cidr(interface_info['src_ip'], value) and not ip_helper.is_ipv4_in_cidr(interface_info['dest'], value):
                    return False

            if key == 'fault':
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_tunnel',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_interfaces_tunnel(
            self,
            pod_id,
            node_id,
            interface_filter=None,
            resolve=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_interfaces = self.get_interfaces_tunnel_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_tunnel(interface_info, interface_filter):
                continue

            if resolve:
                interface_info = self.get_interface_tunnel_info_resolved(
                    interface_info
                )

            if fault_info:
                interface_info['faultInst'] = self.get_interface_tunnel_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_tunnel_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_tunnel_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_tunnel_id_audit(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    audit_filter=audit_filter
                )

            interfaces.append(
                interface_info
            )

        interfaces = sorted(
            interfaces,
            key=lambda i: i['tunnelId']
        )

        return interfaces

    def get_interface_tunnel(self, pod_id, node_id, port_id):
        interfaces = self.get_interfaces_tunnel(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (port_id)]
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
