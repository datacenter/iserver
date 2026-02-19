import time


class K8sDataScienceClusterWait():
    def __init__(self):
        pass
    
    def wait_data_science_cluster(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_data_science_cluster(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_data_science_cluster',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    
    def wait_data_science_cluster_ready(self, name, max_time=900, my_output=None):
        start_time = int(time.time())
        last = -1
        while True:
            info = self.get_data_science_cluster(
                name,
                cache_enabled=False
            )
            if info is not None:
                if my_output is not None:
                    if last < 0 and len(info['componentNotReady']) > 0:
                        last = len(info['componentNotReady']) + 1
                    
                    if last > 0:
                        if last > len(info['componentNotReady']):
                            my_output.default('Waiting for: %s' % (', '.join(info['componentNotReady'])))

                        last = len(info['componentNotReady'])
                        if last == 0:                            
                            my_output.default('Waiting for ready state...')

                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_data_science_cluster',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_no_data_science_cluster(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_data_science_cluster(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_data_science_cluster',
                    'Max time reached: %s' % ( name)
                )
                return False

            time.sleep(5)
