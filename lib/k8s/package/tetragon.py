import time


class K8sPackageTetragon():
    def __init__(self):
        pass

    def wait_tetragon_package(self, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_package(
                'tetragon', 
                'tetragon-operator', 
                return_mo=False, 
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_tetragon_package',
                    'Max time reached'
                )
                return False

            time.sleep(5)