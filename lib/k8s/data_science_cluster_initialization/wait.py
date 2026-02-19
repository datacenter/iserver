import time


class K8sDataScienceClusterInitializationWait():
    def __init__(self):
        pass

    def wait_any_data_science_cluster_initialization(self, max_time=360, my_output=None):
        start_time = int(time.time())
        if my_output is not None:
            my_output.default('Wait for data science cluster initialization...')

        while True:
            info = self.get_data_science_cluster_initializations(
                cache_enabled=False
            )
            if info is not None and len(info) == 1:
                if my_output is not None:
                    my_output.default(info[0]['name'])

                return info[0]['name']

            duration = int(time.time()) - start_time
            if duration > max_time:
                if my_output is not None:
                    my_output.error('timed out')

                self.log.error(
                    'k8s.wait_any_data_science_cluster_initialization',
                    'Max time reached'
                )
                return None

            time.sleep(5)

    def wait_data_science_cluster_initialization(self, name, max_time=60, my_output=None):
        start_time = int(time.time())
        if my_output is not None:
            my_output.default('Wait for data science cluster initialization [%s]...' % (name))

        while True:
            info = self.get_data_science_cluster_initialization(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if my_output is not None:
                    my_output.error('timed out')
                    
                self.log.error(
                    'k8s.wait_no_data_science_cluster_initialization',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_data_science_cluster_initialization_ready(self, name, max_time=360, my_output=None):
        start_time = int(time.time())
        if my_output is not None:
            my_output.default('Wait for data science cluster initialization [%s] ready...' % (name))

        while True:
            info = self.get_data_science_cluster_initialization(
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if my_output is not None:
                    my_output.error('timed out')

                self.log.error(
                    'k8s.wait_no_data_science_cluster_initialization',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_no_data_science_cluster_initialization(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_data_science_cluster_initialization(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_data_science_cluster_initialization',
                    'Max time reached: %s' % ( name)
                )
                return False

            time.sleep(5)
