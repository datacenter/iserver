import time
import traceback


class K8sDaemonSetApi():
    def __init__(self):
        self.daemon_set_mo = None
        self.daemon_set_namespace_mo = {}

    def get_daemon_set_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.daemon_set_mo,
            self.daemon_set_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.daemon_set_mo, self.daemon_set_namespace_mo = self.get_namespaced_resources(
            'DaemonSet', 
            'apps/v1', 
            self.daemon_set_mo,
            self.daemon_set_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def patch_daemon_set_mo(self, namespace, name, body):
        api_handler = self.get_api(cluster_type='standard', api_type='apps')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.patch_namespaced_daemon_set(
                name,
                namespace,
                body
            )

        except BaseException:
            self.log.error('k8s.patch_daemon_set_mo', traceback.format_exc())
            self.log.k8s(
                'patch',
                'daemon_set',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True
