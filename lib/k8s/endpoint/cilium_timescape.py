import time
from lib import filter_helper


class K8sEndpointCiliumTimescape():
    def __init__(self):
        pass

    def is_endpoint_cilium_timescape(self, endpoint):
        if 'metadata' in endpoint:
            labels_mo = filter_helper.get(endpoint, 'metadata:labels')
            if labels_mo is not None:
                if 'app.kubernetes.io/name' in labels_mo:
                    if labels_mo['app.kubernetes.io/name'] == 'hubble-timescape':
                        return True
                    
        if 'metadata' not in endpoint:
            if 'app.kubernetes.io/name' in endpoint['label']:
                if endpoint['label']['app.kubernetes.io/name'] == 'hubble-timescape':
                    return True
                            
        return False
    
    def get_cilium_timescape_endpoints_name(self, cache_enabled=True):
        endpoints = self.get_cilium_timescape_endpoints(cache_enabled=cache_enabled)
        if endpoints is None:
            return None
        
        names = []
        for endpoint in endpoints:
            names.append(endpoint['name'])

        return names

    def get_cilium_timescape_endpoints(self, return_mo=False, cache_enabled=False, include_headless=True):
        endpoints = self.get_endpoints(
            object_filter=['namespace:%s' % self.cilium_namespace],
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if endpoints is None:
            return None
        
        cilium_endpoints = []
        for endpoint in endpoints:
            if not self.is_endpoint_cilium_timescape(endpoint=endpoint):
                continue

            if not include_headless and endpoint['headless']:
                continue

            cilium_endpoints.append(endpoint)

        return cilium_endpoints

    def wait_cilium_timescape_endpoints_ready(self, expected_pods_count=None, max_time=300):
        start_time = int(time.time())
        while True:
            endpoints = self.get_cilium_timescape_endpoints(cache_enabled=False, include_headless=False)
            if endpoints is not None and len(endpoints) > 0:
                ready = True
                for endpoint in endpoints:
                    if expected_pods_count is not None:
                        if len(endpoint['address']) != expected_pods_count:
                            ready = False

                if ready:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)

    def wait_no_cilium_timescape_endpoints(self, max_time=300):
        start_time = int(time.time())
        while True:
            endpoints = self.get_cilium_timescape_endpoints(cache_enabled=False, include_headless=True)
            if endpoints is not None and len(endpoints) == 0:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)
