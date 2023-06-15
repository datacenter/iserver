from lib import filter_helper


class NodePowerInfo():
    def __init__(self):
        self.nodes_power = None

    def convert_node_power_value(self, value):
        if len(value) == 0:
            return None

        return round(float(value), 2)

    def get_node_power_info(self, managed_object):
        # "childAction": "",
        # "cnt": "1",
        # "dn": "topology/pod-1/node-3/sys/ch/psuslot-5/psu/CDeqptPsPower15min",
        # "drawnAvg": "64.000000",
        # "drawnLast": "64.000000",
        # "drawnMax": "64.000000",
        # "drawnMin": "64.000000",
        # "drawnSpct": "0",
        # "drawnThr": "",
        # "drawnTr": "0.000000",
        # "drawnTrBase": "58.666667",
        # "drawnTtl": "64.000000",
        # "lastCollOffset": "300",
        # "repIntvEnd": "2023-05-19T09:05:29.169+02:00",
        # "repIntvStart": "2023-05-19T09:00:28.504+02:00",
        # "status": "",
        # "suppliedAvg": "72.000000",
        # "suppliedLast": "72.000000",
        # "suppliedMax": "72.000000",
        # "suppliedMin": "72.000000",
        # "suppliedSpct": "0",
        # "suppliedThr": "",
        # "suppliedTr": "0.000000",
        # "suppliedTrBase": "66.666667",
        # "suppliedTtl": "72.000000"
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            if key.startswith('drawn'):
                info[key] = self.convert_node_power_value(managed_object[key])
                continue

            if key.startswith('supplied'):
                info[key] = self.convert_node_power_value(managed_object[key])
                continue

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

        # "dn": "topology/pod-1/node-3/sys/ch/psuslot-5/psu/CDeqptPsPower15min"
        info['slotId'] = info['dn'].split('/')[5][8:]

        return info

    def get_nodes_power_info(self):
        if self.nodes_power is not None:
            return self.nodes_power

        nodes_power_mo = self.get_node_power_mo()
        if nodes_power_mo is not None:
            self.nodes_power = []
            for node_power_mo in nodes_power_mo:
                node_power_info = self.get_node_power_info(
                    node_power_mo
                )

                self.nodes_power.append(
                    node_power_info
                )

        return self.nodes_power

    def get_node_power(self, pod_id, node_id):
        node_filter = []
        node_filter.append(
            'pod:%s' % (pod_id)
        )

        node_filter.append(
            'id:%s' % (node_id)
        )

        node_power = self.get_nodes_power(
            node_filter=node_filter
        )

        return node_power

    def match_node_power(self, node_info, node_filter):
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

            if key == 'serial':
                if not filter_helper.match_string(value, node_info['ser']):
                    return False

        return True

    def get_nodes_power(self, node_filter=None):
        all_nodes = self.get_nodes_power_info()
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node_power(node_info, node_filter):
                continue

            nodes.append(
                node_info
            )

        nodes = sorted(
            nodes,
            key=lambda i: (
                i['pod_node_name'],
                i['slotId']
            )
        )

        return nodes
