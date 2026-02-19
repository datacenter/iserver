from lib import filter_helper


class NodeTempInfo():
    def __init__(self):
        self.nodes_temp = None

    def get_node_temp_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['sensorName'] = '%s.%s' % (
            managed_object['dn'].split('/')[5],
            managed_object['dn'].split('/')[7]
        )

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

        return info

    def get_nodes_temp_info(self):
        if self.nodes_temp is not None:
            return self.nodes_temp

        nodes_temp_mo = self.get_node_temp_mo()
        if nodes_temp_mo is not None:
            self.nodes_temp = []
            for node_temp_mo in nodes_temp_mo:
                node_temp_info = self.get_node_temp_info(
                    node_temp_mo
                )

                self.nodes_temp.append(
                    node_temp_info
                )

        return self.nodes_temp

    def get_node_temp(self, pod_id, node_id):
        node_filter = []
        node_filter.append(
            'pod:%s' % (pod_id)
        )

        node_filter.append(
            'id:%s' % (node_id)
        )

        node_temp = self.get_nodes_temp(
            node_filter=node_filter
        )

        return node_temp

    def match_node_temp(self, node_info, node_filter):
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

    def get_nodes_temp(self, node_filter=None):
        all_nodes = self.get_nodes_temp_info()
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node_temp(node_info, node_filter):
                continue

            nodes.append(
                node_info
            )

        nodes = sorted(
            nodes,
            key=lambda i: (
                i['pod_node_name'],
                i['sensorName']
            )
        )

        return nodes
