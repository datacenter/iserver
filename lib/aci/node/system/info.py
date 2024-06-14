from lib import filter_helper


class NodeSystemInfo():
    def __init__(self):
        self.nodes_system = None

    def get_node_system_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['podId'] = managed_object['dn'].split('/')[1][4:]
        info['nodeId'] = managed_object['dn'].split('/')[2][5:]
        info['nodeName'] = self.get_node_name(
            info['nodeId']
        )

        info['apic'] = self.apic_name
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            info['nodeName']
        )

        info['inbMgmtCidr'] = '%s/%s' % (
            info['inbMgmtAddr'],
            info['inbMgmtAddrMask']
        )

        info['oobMgmtCidr'] = '%s/%s' % (
            info['oobMgmtAddr'],
            info['oobMgmtAddrMask']
        )

        return info

    def get_nodes_system_info(self):
        if self.nodes_system is not None:
            return self.nodes_system

        nodes_system_mo = self.get_node_system_mo()
        if nodes_system_mo is not None:
            self.nodes_system = []
            for node_system_mo in nodes_system_mo:
                node_system_info = self.get_node_system_info(
                    node_system_mo
                )

                self.nodes_system.append(
                    node_system_info
                )

        return self.nodes_system

    def get_node_system(self, pod_id, node_id):
        node_filter = []
        node_filter.append(
            'pod:%s' % (pod_id)
        )

        node_filter.append(
            'id:%s' % (node_id)
        )

        node_system = self.get_nodes_system(
            node_filter=node_filter
        )

        if node_system is not None and len(node_system) == 1:
            return node_system[0]

        return None

    def match_node_system(self, node_info, node_filter):
        if node_filter is None or len(node_filter) == 0:
            return True

        for ap_rule in node_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, node_info['nodeId']):
                    return False

            if key == 'pod':
                if not filter_helper.match_string(value, node_info['podId']):
                    return False

        return True

    def get_nodes_system(self, node_filter=None):
        all_nodes = self.get_nodes_system_info()
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node_system(node_info, node_filter):
                continue

            nodes.append(
                node_info
            )

        nodes = sorted(
            nodes,
            key=lambda i: i['pod_node_name']
        )

        return nodes
