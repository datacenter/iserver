import copy
from lib.linux import main as linux


class OcpNodeLinux():
    def __init__(self):
        self.node_linux_handler = {}
        self.k8s_nodes = None

    def get_ocp_nodes_linux_access(self):
        if 'ssh' not in self.ocp_cluster_settings:
            self.log.error(
                'get_ocp_nodes_linux_access',
                'No ssh settings for ocp cluster'
            )
            return None

        if self.k8s_nodes is None:
            self.k8s_nodes = self.k8s_handler.get_nodes()
            if self.k8s_nodes is None:
                self.log.error(
                    'get_ocp_nodes_linux_access',
                    'Failed to get k8s nodes info'
                )
                return None

        nodes = []
        for k8s_node in self.k8s_nodes:
            node_access = {}
            node_access['ip'] = k8s_node['ssh_ip']
            node_access['username'] = self.ocp_cluster_settings['ssh']['username']
            node_access['password'] = self.ocp_cluster_settings['ssh']['password'],
            node_access['key_filename'] = self.ocp_cluster_settings['ssh']['key_filename']
            node_access['name'] = k8s_node['name']

            nodes.append(
                node_access
            )

        return nodes

    def get_ocp_nodes_linux_handlers(self):
        nodes = self.get_ocp_nodes_linux_access()
        if nodes is None:
            self.log.error(
                'get_ocp_nodes_linux_handlers',
                'No nodes'
            )
            return None

        handlers = []

        for node in nodes:
            handler = copy.deepcopy(node)
            handler['handler'] = linux.Linux(
                node['ip'],
                node['username'],
                password=node['password'],
                key_filename=node['key_filename'],
                verbose=False,
                debug=False,
                log_id=self.log_id
            )

            handlers.append(
                handler
            )

        return handlers

    def get_ocp_node_linux_handler(self, node_ip=None, node_name=None):
        if node_ip is None and node_name is None:
            self.log.error(
                'get_ocp_node_linux_handler',
                'Define node with ip or name'
            )
            return None

        if 'parameters' not in self.ocp_cluster_settings or 'nodes' not in self.ocp_cluster_settings['parameters']:
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
