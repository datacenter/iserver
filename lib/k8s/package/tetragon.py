import time


class K8sPackageTetragon():
    def __init__(self):
        pass

    def get_tetragon_package(self, cache_enabled=True):
        object_filter = []
        object_filter.append('catalog:tetragon-catalog')
        object_filter.append('name:tetragon-operator')

        package = self.get_packages(
            object_filter=object_filter,
            return_mo=True,
            cache_enabled=cache_enabled
        )

        if package is None:
            self.log.error(
                'get_nfd_package',
                'failed to get packages'
            )
            return None
        
        if len(package) != 1:
            self.log.error(
                'get_nfd_package',
                'Unexpected package count: %s' % (len(package))
            )
            return None
        
        return package[0]

    def wait_tetragon_package(self, max_time=360):
        start_time = int(time.time())
        while True:
            info = self.get_tetragon_package(
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