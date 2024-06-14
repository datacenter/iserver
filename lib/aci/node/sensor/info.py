from lib import filter_helper


class NodeSensorInfo():
    def __init__(self):
        self.nodes_sensor = None

    def get_node_sensor_info(self, managed_object):
        # "childAction": "",
        # "cimcVersion": "",
        # "descr": "Inlet",
        # "dn": "topology/pod-1/node-101/sys/ch/supslot-1/sup/sensor-1",
        # "id": "1",
        # "majorThresh": "70",
        # "mfgTm": "not-applicable",
        # "minorThresh": "42",
        # "modTs": "2023-05-19T09:13:06.651+02:00",
        # "model": "Inlet",
        # "monPolDn": "uni/fabric/monfab-default",
        # "operSt": "normal",
        # "rev": "n/a",
        # "ser": "n/a",
        # "status": "",
        # "type": "inlet",
        # "value": "0",
        # "vendor": "n/a"
        info = {}
        info['__Output'] = {}

        keys = [
            'descr',
            'id',
            'majorThresh',
            'minorThresh',
            'model',
            'operSt',
            'type',
            'value'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
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

        if info['operSt'] == 'normal':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_nodes_sensor_info(self):
        if self.nodes_sensor is not None:
            return self.nodes_sensor

        nodes_sensor_mo = self.get_node_sensor_mo()
        if nodes_sensor_mo is not None:
            self.nodes_sensor = []
            for node_sensor_mo in nodes_sensor_mo:
                node_sensor_info = self.get_node_sensor_info(
                    node_sensor_mo
                )

                self.nodes_sensor.append(
                    node_sensor_info
                )

        return self.nodes_sensor

    def get_node_sensor(self, pod_id, node_id):
        node_filter = []
        node_filter.append(
            'pod:%s' % (pod_id)
        )

        node_filter.append(
            'id:%s' % (node_id)
        )

        node_sensor = self.get_nodes_sensor(
            node_filter=node_filter
        )

        return node_sensor

    def match_node_sensor(self, node_info, node_filter):
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

    def get_nodes_sensor(self, node_filter=None):
        all_nodes = self.get_nodes_sensor_info()
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node_sensor(node_info, node_filter):
                continue

            nodes.append(
                node_info
            )

        nodes = sorted(
            nodes,
            key=lambda i: (
                i['pod_node_name'],
                i['descr']
            )
        )

        return nodes
