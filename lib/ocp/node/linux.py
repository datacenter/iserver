from lib.linux import main as linux


class OcpNodeLinux():
    def __init__(self):
        self.node_linux_handler = {}

    def get_ocp_node_linux_handler(self, node_ip=None, node_name=None):
        if node_ip is None and node_name is None:
            self.log.error(
                'get_ocp_node_linux_handler',
                'Define node with ip or name'
            )
            return None

        if 'nodes' not in self.ocp_cluster_settings['parameters']:
            self.log.error(
                'get_ocp_node_linux_handler',
                'No nodes in ocp settings'
            )
            return None

        if node_ip is None:
            node_ip = self.k8s_handler.get_node_ip(
                node_name
            )
            if node_ip is None:
                self.log.error(
                    'get_ocp_node_linux_handler',
                    'No node ip found: %s' % (node_name)
                )
                return None

        if node_ip in self.node_linux_handler:
            return self.node_linux_handler[node_ip]

        for node in self.ocp_cluster_settings['parameters']['nodes']:
            if node['ip'] == node_ip:
                self.node_linux_handler[node_ip] = linux.Linux(
                    node_ip,
                    node['username'],
                    password=node['password'],
                    key_filename=node['key_filename'],
                    verbose=False,
                    debug=False,
                    log_id=self.log_id
                )
                return self.node_linux_handler[node_ip]

        self.log.error(
            'get_ocp_node_linux_handler',
            'No linux handler: %s' % (node_ip)
        )
        return None
