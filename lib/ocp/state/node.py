from lib.linux import main as linux


class OcpStateNode():
    def __init__(self):
        pass

    def get_ocp_node_linux_handler(self, host_ip):
        if 'nodes' in self.ocp_cluster_settings['parameters']:
            for node in self.ocp_cluster_settings['parameters']['nodes']:
                if node['ip'] == host_ip:
                    linux_handler = linux.Linux(
                        host_ip,
                        node['username'],
                        password=node['password'],
                        key_filename=node['key_filename'],
                        verbose=False,
                        debug=False
                    )
                    return linux_handler

        return None

    def get_ocp_node_info(self, node_mo):
        info = self.k8s_handler.get_node_info(node_mo)
        if info is None:
            return None

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
        if not self.k8s_handler.get_nodes():
            return None

        info = []
        for node_mo in self.k8s_handler.nodes:
            node_info = self.get_ocp_node_info(node_mo)
            if node_info is not None:
                info.append(node_info)

        info = sorted(
            info,
            key=lambda i: i['name']
        )

        return info

    def print_ocp_nodes_list(self, nodes):
        order = [
            'type',
            'name',
            'ready',
            'mcp.tick',
            'cnv.tick',
            'roles',
            'age',
            'node_info.kubelet_version'
        ]

        headers = [
            'TF',
            'Name',
            'Status',
            'MCP',
            'CNV',
            'Roles',
            'Age',
            'Version'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
