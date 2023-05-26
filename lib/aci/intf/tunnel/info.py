from lib import filter_helper
from lib import ip_helper


class InterfaceTunnelInfo():
    def __init__(self):
        self.interface_tunnel = {}

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

        info['apic'] = self.apic_label
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
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

        info['dest_node'] = None
        info['dest_ip_node'] = info['dest']

        destination_node_info = self.get_node(
            node_ip=info['dest'].split('/')[0]
        )
        if destination_node_info is not None:
            info['dest_node'] = destination_node_info['name']
            info['dest_ip_node'] = '%s (%s)' % (
                info['dest'],
                info['dest_node']
            )

        return info

    def get_interfaces_tunnel_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_tunnel:
            return self.interface_tunnel[key]

        interfaces_mo = self.get_interface_tunnel_mo(pod_id, node_id)
        if interfaces_mo is not None:
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
                source_ip = interface_info['src'].split('/')[0]
                destination_ip = interface_info['dest']
                if not filter_helper.match_string(value, source_ip) and not filter_helper.match_string(value, destination_ip):
                    return False

            if key == 'subnet':
                source_ip = interface_info['src'].split('/')[0]
                destination_ip = interface_info['dest']
                if not ip_helper.is_ipv4_in_cidr(source_ip, value) and not ip_helper.is_ipv4_in_cidr(destination_ip, value):
                    return False

        return True

    def get_interfaces_tunnel(self, pod_id, node_id, interface_filter=None):
        all_interfaces = self.get_interfaces_tunnel_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_tunnel(interface_info, interface_filter):
                continue

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
