import time
from lib import filter_helper


class K8sEndpointWait():
    def __init__(self):
        pass

    def wait_endpoint(self, namespace, name, max_time=600, my_output=None):
        if my_output is not None:
            my_output.default('Wait for endpoint %s/%s...' % (namespace, name))

        start_time = int(time.time())
        while True:
            try:
                endpoint = self.get_endpoint(
                    namespace,
                    name,
                    cache_enabled=False
                )
                if endpoint is not None:
                    return True
            except BaseException:
                pass

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_endpoint',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_endpoint_endpoint_address(self, namespace, name, max_time=600, my_output=None):
        if my_output is not None:
            my_output.default('Wait for endpoint address %s/%s...' % (namespace, name))

        start_time = int(time.time())
        while True:
            try:
                endpoint = self.get_endpoint(
                    namespace,
                    name,
                    cache_enabled=False
                )
                if endpoint is not None:
                    if len(endpoint['address']) > 0:
                        return True
            except BaseException:
                pass

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_endpoint_endpoint_address',
                    'Max time reached'
                )
                return False

            time.sleep(5)
