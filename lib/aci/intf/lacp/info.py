from lib import filter_helper


class InterfaceLacpInfo():
    def __init__(self):
        self.interfaces_lacp = {}

    def get_interface_lacp_count(self, pod_id, node_id):
        interfaces = self.get_interface_lacp(pod_id, node_id)
        return len(interfaces)

    def get_interface_lacp_info(self, managed_object):
        keys = [
            'activityFlags',
            'adminSt',
            'dn',
            'id',
            'key',
            'lastActive',
            'operPrio',
            'port',
            'prio',
            'txRate',
            'stats'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['__Output']['id'] = 'Blue'

        # Dn format
        # topology/pod-1/node-201/sys/lacp/inst/if-[eth1/2]
        info['apic'] = self.apic_name
        info['podId'] = info['dn'].split('/')[1].split('-')[1]
        info['nodeId'] = info['dn'].split('/')[2].split('-')[1]
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(info['nodeId'])
        )

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_interfaces_lacp_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_lacp:
            return self.interfaces_lacp[key]

        interfaces_lacp_mo = self.get_interfaces_lacp_mo(pod_id, node_id)
        if interfaces_lacp_mo is None:
            return None

        self.interfaces_lacp[key] = []
        for interface_lacp_mo in interfaces_lacp_mo:
            self.interfaces_lacp[key].append(
                self.get_interface_lacp_info(
                    interface_lacp_mo
                )
            )

        self.log.apic_mo(
            'lacpIf.info.%s' % (key),
            self.interfaces_lacp[key]
        )

        return self.interfaces_lacp[key]

    def match_interface_lacp(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

        return True

    def get_interface_lacp(self, pod_id, node_id, interface_filter=None, adjacency_info=False):
        all_interfaces = self.get_interfaces_lacp_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_lacp(interface_info, interface_filter):
                continue

            if adjacency_info:
                interface_info['adjacency'] = self.get_lacp_adjacency_endpoint(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    allow_multiple=False
                )

            interfaces.append(
                interface_info
            )

        interfaces = sorted(
            interfaces,
            key=lambda i: i['id']
        )

        return interfaces
