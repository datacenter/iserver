from lib import filter_helper


class NodePsuInfo():
    def __init__(self):
        self.nodes_psu = None

    def convert_node_psu_value(self, value):
        if len(value) == 0:
            return None

        return round(float(value), 2)

    def get_node_psu_info(self, managed_object):
        # "almReg": "0",
        # "cap": "4.000000",
        # "childAction": "",
        # "cimcVersion": "",
        # "descr": "FRU_PSU1 (ID 4)",
        # "dn": "topology/pod-1/node-1/sys/ch/psuslot-5/psu",
        # "drawnCurr": "0.000000",
        # "fanOpSt": "unknown",
        # "hwVer": "A",
        # "id": "1",
        # "mfgTm": "not-applicable",
        # "modTs": "2023-05-19T09:15:45.143+02:00",
        # "model": "UCSC-PSU1-770W",
        # "monPolDn": "uni/fabric/monfab-default",
        # "operSt": "ok",
        # "rev": "0",
        # "ser": "APS234101KU",
        # "status": "",
        # "tc": "770",
        # "vId": "",
        # "vSrc": "unknown",
        # "vendor": "Cisco Systems Inc",
        # "volt": "12.000000"
        info = {}
        info['__Output'] = {}

        keys = [
            'cap',
            'descr',
            'dn',
            'drawnCurr',
            'fanOpSt',
            'hwVer',
            'id',
            'model',
            'operSt',
            'rev',
            'ser',
            'tc',
            'vendor',
            'volt'
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

        info['volt'] = self.convert_node_psu_value(info['volt'])
        info['drawnCurr'] = self.convert_node_psu_value(info['drawnCurr'])

        # "dn": "topology/pod-1/node-1/sys/ch/psuslot-5/psu"
        info['slotId'] = info['dn'].split('/')[5][8:]

        if info['operSt'] == 'ok':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_nodes_psu_info(self):
        if self.nodes_psu is not None:
            return self.nodes_psu

        nodes_psu_mo = self.get_node_psu_mo()
        if nodes_psu_mo is not None:
            self.nodes_psu = []
            for node_psu_mo in nodes_psu_mo:
                node_psu_info = self.get_node_psu_info(
                    node_psu_mo
                )

                self.nodes_psu.append(
                    node_psu_info
                )

        return self.nodes_psu

    def get_node_psu(self, pod_id, node_id):
        node_filter = []
        node_filter.append(
            'pod:%s' % (pod_id)
        )

        node_filter.append(
            'id:%s' % (node_id)
        )

        node_psu = self.get_nodes_psu(
            node_filter=node_filter
        )

        return node_psu

    def match_node_psu(self, node_info, node_filter):
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

    def get_nodes_psu(self, node_filter=None):
        all_nodes = self.get_nodes_psu_info()
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node_psu(node_info, node_filter):
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
