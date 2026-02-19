import time


class K8sIsovalentBGPAdvertisementWait():
    def __init__(self):
        pass

    def wait_isovalent_bgp_advertisement(self, name, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_isovalent_bgp_advertisement(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)

    def wait_no_isovalent_bgp_advertisement(self, name, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_isovalent_bgp_advertisement(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)
