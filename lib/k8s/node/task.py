import time


class K8sNodeTask():
    def __init__(self):
        pass

    def wait_node_ready(self, node_name, max_time=360):
        start_time = int(time.time())
        while True:
            node_mo = self.get_node_mo(
                node_name,
                cache=False
            )
            if node_mo is not None:
                if self.is_node_ready(node_mo):
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_node_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_node_not_ready(self, node_name, max_time=360):
        start_time = int(time.time())
        while True:
            node_mo = self.get_node_mo(
                node_name,
                cache=False
            )
            if node_mo is not None:
                if not self.is_node_ready(node_mo):
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_node_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)
