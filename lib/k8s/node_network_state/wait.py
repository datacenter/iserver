import time


class K8sNodeNetworkStateWait():
    def __init__(self):
        pass

    def wait_node_network_state(self, node_name, max_time=360):
        start_time = int(time.time())
        while True:
            nns = self.get_node_network_state(
                node_name,
                cache_enabled=False
            )
            if nns is not None:
                return nns

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_node_network_state',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_nodes_network_state(self, max_time=360, my_output=None):
        nodes = self.get_nodes()
        if nodes is None:
            return False

        if my_output is not None:
            my_output.default('Wait for nns ready on all cluster nodes')

        for node in nodes:
            success = self.wait_node_network_state(node['name'], max_time=max_time)
            if not success:
                if my_output is not None:
                    my_output.error('Node [%s] nns collection failed' % (node['name']))
                return False

            my_output.default('Node [%s] nns collected' % (node['name']))

        return True
