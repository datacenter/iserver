from lib import filter_helper


class OcpNodeInfo():
    def __init__(self):
        self.nodes = None

    def get_ocp_node_info(self, node_mo):
        info = self.k8s_handler.get_node_info(node_mo)
        if info is None:
            return None

        # change labels from dict to list of dict
        labels = []
        for key in info['label']:
            label = {}
            label['key'] = key
            label['value'] = info['label'][key]
            labels.append(
                label
            )
        info['labels'] = labels

        info['cluster'] = self.ocp_cluster_settings['name']
        info['mcp'] = {}
        info['mcp']['current_config'] = None
        info['mcp']['desired_config'] = None
        info['mcp']['match'] = False
        info['mcp']['tick'] = '\u2717'
        info['__Output']['mcp.tick'] = 'Red'

        info['cnv'] = {}
        info['cnv']['schedulable'] = False
        info['cnv']['tick'] = '\u2717'
        info['__Output']['cnv.tick'] = 'Red'

        for annotation in node_mo['metadata']['annotations']:
            if annotation == 'machineconfiguration.openshift.io/currentConfig':
                info['mcp']['current_config'] = node_mo['metadata']['annotations']['machineconfiguration.openshift.io/currentConfig']

            if annotation == 'machineconfiguration.openshift.io/desiredConfig':
                info['mcp']['desired_config'] = node_mo['metadata']['annotations']['machineconfiguration.openshift.io/desiredConfig']

        if info['mcp']['current_config'] is not None and info['mcp']['desired_config'] is not None:
            if info['mcp']['current_config'] == info['mcp']['desired_config']:
                info['mcp']['match'] = True
                info['mcp']['tick'] = '\u2713'
                info['__Output']['mcp.tick'] = 'Green'

        for label in node_mo['metadata']['labels']:
            if label == 'kubevirt.io/schedulable' and node_mo['metadata']['labels'][label] == 'true':
                info['cnv']['schedulable'] = False
                info['cnv']['tick'] = '\u2713'
                info['__Output']['cnv.tick'] = 'Green'

        return info

    def get_ocp_nodes_info(self):
        if self.nodes is not None:
            return self.nodes

        nodes_mo = self.k8s_handler.get_nodes(return_mo=True)

        self.nodes = []
        for node_mo in nodes_mo:
            node_info = self.get_ocp_node_info(node_mo)
            if node_info is not None:
                self.nodes.append(
                    node_info
                )

        self.nodes = sorted(
            self.nodes,
            key=lambda i: i['name']
        )

        return self.nodes

    def filter_ocp_node_labels(self, node_labels, node_filter):
        if node_filter is None or len(node_filter) == 0:
            return node_labels

        labels = []

        for node_label in node_labels:
            match = True
            for ap_rule in node_filter:
                (key, value) = ap_rule.split(':')
                if key == 'label':
                    if not filter_helper.match_string(value, node_label['key']):
                        match = False
                        break

            if match:
                labels.append(
                    node_label
                )

        return labels

    def match_ocp_node(self, node_info, node_filter):
        if node_filter is None or len(node_filter) == 0:
            return True

        for ap_rule in node_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_info['name']):
                    return False

            if key == 'worker':
                key_found = True
                if value == 'true' and not node_info['worker']:
                    return False
                if value == 'false' and node_info['worker']:
                    return False

            if key == 'master':
                key_found = True
                if value == 'true' and not node_info['master']:
                    return False
                if value == 'false' and node_info['master']:
                    return False

            if key == 'label':
                key_found = True
                found = False
                for label in node_info['labels']:
                    if filter_helper.match_string(value, label['key']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_ocp_node',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ocp_nodes(self, node_filter=None, sriov_phy_info=False, sriov_policy_info=False, sriov_network_info=False, sriov_vf_info=False):
        all_nodes = self.get_ocp_nodes_info()

        nodes = []
        for node_info in all_nodes:
            if not self.match_ocp_node(node_info, node_filter):
                continue

            node_info['labels'] = self.filter_ocp_node_labels(node_info['labels'], node_filter)

            if sriov_phy_info or sriov_policy_info or sriov_network_info or sriov_vf_info:
                node_sriov = self.get_ocp_node_sriov(
                    node_info['name'],
                    sriov_phy_info=sriov_phy_info,
                    sriov_policy_info=sriov_policy_info,
                    sriov_network_info=sriov_network_info,
                    sriov_vf_info=sriov_vf_info
                )
                for key in node_sriov:
                    node_info[key] = node_sriov[key]

            nodes.append(
                node_info
            )

        nodes = sorted(
            nodes,
            key=lambda i: i['name']
        )

        return nodes
