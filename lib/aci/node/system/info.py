from lib import filter_helper


class NodeSystemInfo():
    def __init__(self):
        self.nodes_system = None

    def get_node_system_info(self, managed_object):
        # "address": "10.3.0.1",
        # "bootstrapState": "none",
        # "childAction": "",
        # "clusterTimeDiff": "196197",
        # "configIssues": "",
        # "controlPlaneMTU": "9000",
        # "currentTime": "2023-05-19T09:13:06.801+02:00",
        # "dn": "topology/pod-1/node-1/sys",
        # "enforceSubnetCheck": "no",
        # "etepAddr": "0.0.0.0",
        # "fabricDomain": "ACI1-EU-SPDC",
        # "fabricId": "1",
        # "fabricMAC": "00:22:BD:F8:19:FF",
        # "id": "1",
        # "inbMgmtAddr": "10.58.28.161",
        # "inbMgmtAddr6": "fc00::1",
        # "inbMgmtAddr6Mask": "0",
        # "inbMgmtAddrMask": "27",
        # "inbMgmtGateway": "10.58.28.190",
        # "inbMgmtGateway6": "::",
        # "lastRebootTime": "2023-03-02T00:55:32.780+02:00",
        # "lastResetReason": "unknown",
        # "lcOwn": "local",
        # "modTs": "2023-05-19T08:22:01.158+02:00",
        # "mode": "unspecified",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "apic1",
        # "nameAlias": "",
        # "nodeType": "unspecified",
        # "oobMgmtAddr": "10.58.28.131",
        # "oobMgmtAddr6": "fe80::5e71:dff:fe9d:e4ca",
        # "oobMgmtAddr6Mask": "0",
        # "oobMgmtAddrMask": "27",
        # "oobMgmtGateway": "10.58.28.158",
        # "oobMgmtGateway6": "2001:420:28e:2020:acc:68ff:fe28:b540",
        # "podId": "1",
        # "remoteNetworkId": "0",
        # "remoteNode": "no",
        # "rlOperPodId": "0",
        # "rlRoutableMode": "no",
        # "rldirectMode": "no",
        # "role": "controller",
        # "serial": "WZP234408RN",
        # "serverType": "unspecified",
        # "siteId": "0",
        # "state": "in-service",
        # "status": "",
        # "systemUpTime": "78:08:20:50.000",
        # "tepPool": "0.0.0.0",
        # "unicastXrEpLearnDisable": "no",
        # "version": "5.2(7f)",
        # "virtualMode": "no"
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
