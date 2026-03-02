import time


class CiliumLoadBalancerIpPoolWait():
    def __init__(self):
        pass

    def wait_cilium_load_balancer_ip_pool(self, name, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_cilium_load_balancer_ip_pool(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)

    def wait_no_cilium_load_balancer_ip_pool(self, name, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_cilium_load_balancer_ip_pool(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)
