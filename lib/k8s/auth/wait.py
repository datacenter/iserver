import time


class K8sAuthWait():
    def __init__(self):
        pass

    def wait_any_auth(self, max_time=360, my_output=None):
        start_time = int(time.time())
        if my_output is not None:
            my_output.default('Wait for auth...')

        while True:
            info = self.get_auths(
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
                    'k8s.wait_any_auth',
                    'Max time reached'
                )
                return None

            time.sleep(5)

    def wait_auth(self, name, max_time=60, my_output=None):
        start_time = int(time.time())
        if my_output is not None:
            my_output.default('Wait for auth [%s]...' % (name))

        while True:
            info = self.get_auth(
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
                    'k8s.wait_no_auth',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    
    def wait_auth_ready(self, name, max_time=600, my_output=None):
        start_time = int(time.time())
        if my_output is not None:
            my_output.default('Wait for auth [%s] ready...' % (name))

        while True:
            info = self.get_auth(
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
                    'k8s.wait_no_auth',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_no_auth(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_auth(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_auth',
                    'Max time reached: %s' % ( name)
                )
                return False

            time.sleep(5)
