import time


class K8sClusterOperatorWait():
    def __init__(self):
        pass

    def wait_cluster_operator_available(self, name, max_time=600, my_output=None):
        start_time = int(time.time())
        while True:
            info = self.get_cluster_operator(name, cache_enabled=False)
            if info is not None and info['available']:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if my_output is not None:
                    my_output.default('Max wait time reached, cluster operator not available: %s' % (name))

                return False

            time.sleep(5)
            
    def wait_cluster_operators_available(self, max_time=600):
        start_time = int(time.time())
        while True:
            if self.are_cluster_operators_available(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)
    