from lib import filter_helper
from lib import ip_helper


class NodeInfo():
    def __init__(self):
        self.nodes = None

    def get_node_count(self, pod_id=None):
        node_filter = None
        if pod_id is not None:
            node_filter = ['pod:%s' % (pod_id), 'role:!controller']
        else:
            node_filter = ['role:!controller']

        nodes = self.get_nodes(
            node_filter=node_filter
        )
        return len(nodes)

    def get_node_id(self, node_name, pod_id=None):
        node_info = self.get_node(
            pod_id=pod_id,
            node_name=node_name
        )
        if node_info is None:
            return None
        return node_info['id']

    def get_node_name(self, node_id, pod_id=None):
        node_info = self.get_node(
            pod_id=pod_id,
            node_id=node_id
        )
        if node_info is None:
            return None
        return node_info['name']

    def get_node_names(self, pod_id=None):
        node_filter = None
        if pod_id is not None:
            node_filter = ['pod:%s' % (pod_id)]

        nodes = self.get_nodes(
            node_filter=node_filter
        )
        if nodes is None:
            return None

        node_names = []
        for node in nodes:
            node_names.append(
                node['name']
            )

        return node_names

    def get_node_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'address',
            'adSt',
            'apicType',
            'dn',
            'id',
            'fabricSt',
            'model',
            'name',
            'nodeType',
            'role',
            'serial',
            'userdom',
            'vendor',
            'version'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['podId'] = managed_object['dn'].split('/')[1][4:]

        info['apic'] = self.apic_name
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            info['name']
        )
        info['full_name'] = '%s/%s' % (
            info['apic'],
            info['pod_node_name']
        )

        info['roleUi'] = info['role']
        if info['nodeType'] == 'remote-leaf-wan':
            info['roleUi'] = 'r-leaf'

        if info['adSt'] == 'on':
            info['__Output']['adSt'] = 'Green'
        else:
            info['__Output']['adSt'] = 'Red'

        if info['fabricSt'] in ['unknown', 'inactive']:
            if info['role'] == 'controller':
                info['fabricSt'] = 'N/A'
            else:
                info['__Output']['fabricSt'] = 'Red'

        if info['fabricSt'] == 'active':
            info['__Output']['fabricSt'] = 'Green'

        if info['fabricSt'] == 'inactive':
            info['__Output']['fabricSt'] = 'Red'

        return info

    def get_nodes_info(self):
        if self.nodes is not None:
            return self.nodes

        nodes_mo = self.get_node_mo()
        if nodes_mo is not None:
            self.nodes = []
            for node_mo in nodes_mo:
                self.nodes.append(
                    self.get_node_info(
                        node_mo
                    )
                )

        return self.nodes

    def get_node(self, pod_id=None, node_id=None, node_name=None, node_ip=None):
        node_filter = []
        if pod_id is not None:
            node_filter.append(
                'pod:%s' % (pod_id)
            )

        if node_id is not None:
            node_filter.append(
                'id:%s' % (node_id)
            )

        if node_name is not None:
            node_filter.append(
                'name:%s' % (node_name)
            )

        if node_ip is not None:
            node_filter.append(
                'ip:%s' % (node_ip)
            )

        nodes = self.get_nodes(
            node_filter=node_filter
        )

        if nodes is None:
            return None

        if len(nodes) == 1:
            return nodes[0]

        return None

    def match_node(self, node_info, node_filter):
        if node_filter is None or len(node_filter) == 0:
            return True

        for ap_rule in node_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, node_info['id']):
                    return False

            if key == 'name':
                if not filter_helper.match_string(value, node_info['name']):
                    return False

            if key == 'names':
                found = False
                for name in value.split(','):
                    if filter_helper.match_string(name, node_info['name']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'pod':
                if not filter_helper.match_string(value, node_info['podId']):
                    return False

            if key == 'model':
                if not filter_helper.match_string(value, node_info['model']):
                    return False

            if key == 'ip':
                if 'system' in node_info:
                    found = False

                    if filter_helper.match_string(value, node_info['address']):
                        found = True

                    if not found and filter_helper.match_string(value, node_info['system']['inbMgmtAddr']):
                        found = True

                    if not found and filter_helper.match_string(value, node_info['system']['oobMgmtAddr']):
                        found = True

                    if not found:
                        return False

            if key == 'subnet':
                if 'system' in node_info:
                    found = False

                    if ip_helper.is_ipv4_in_cidr(node_info['address'], value):
                        found = True

                    if not found and ip_helper.is_ipv4_in_cidr(node_info['system']['inbMgmtAddr'], value):
                        found = True

                    if not found and ip_helper.is_ipv4_in_cidr(node_info['system']['oobMgmtAddr'], value):
                        found = True

                    if not found:
                        return False

            if key == 'role':
                if value == '!controller':
                    if node_info['role'] == 'controller':
                        return False
                else:
                    if node_info['role'] != value:
                        return False

        return True

    def get_nodes(self, node_filter=None, interfaces_summary_info=False, power_info=False, psu_info=False, sensor_info=False, system_info=False, temp_info=False):
        all_nodes = self.get_nodes_info()
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node(node_info, node_filter):
                continue

            if interfaces_summary_info:
                if node_info['role'] == 'controller':
                    node_info['interfaces_summary'] = ''
                else:
                    node_info['interfaces_summary'] = self.get_interfaces_phy_summary(
                        node_info['podId'],
                        node_info['id']
                    )

            if power_info:
                node_info['power'] = self.get_node_power(
                    node_info['podId'],
                    node_info['id']
                )

            if psu_info:
                node_info['psu'] = self.get_node_psu(
                    node_info['podId'],
                    node_info['id']
                )

            if sensor_info:
                node_info['sensor'] = self.get_node_sensor(
                    node_info['podId'],
                    node_info['id']
                )

            if system_info:
                node_info['system'] = self.get_node_system(
                    node_info['podId'],
                    node_info['id']
                )
                if not self.match_node(node_info, node_filter):
                    continue

            if temp_info:
                node_info['temp'] = self.get_node_temp(
                    node_info['podId'],
                    node_info['id']
                )

            nodes.append(
                node_info
            )

        nodes = sorted(
            nodes,
            key=lambda i: i['name'].lower()
        )

        return nodes
