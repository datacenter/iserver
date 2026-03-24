import time


class K8sIsovalentBGPClusterConfigWait():
    def __init__(self):
        pass

    def wait_isovalent_bgp_cluster_config(self, name, my_output=None, prompt='IsovalentBGPClusterConfig', max_time=360):
        return self.wait_managed_object(
            'isovalent_bgp_cluster_config',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_isovalent_bgp_cluster_config(self, name, my_output=None, prompt='IsovalentBGPClusterConfig', max_time=360):
        return self.wait_no_managed_object(
            'isovalent_bgp_cluster_config',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
    
    def wait_isovalent_bgp_cluster_config_crd(self, max_time=360):
        start_time = int(time.time())
        while True:
            crds = self.get_isovalent_bgp_cluster_configs(
                cache_enabled=False
            )
            if crds is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)

    def wait_no_isovalent_bgp_cluster_config_crd(self, max_time=360):
        start_time = int(time.time())
        while True:
            crds = self.get_isovalent_bgp_cluster_configs(
                cache_enabled=False
            )
            if crds is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)
