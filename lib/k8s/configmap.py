import time
import traceback


class K8sConfigMap():
    def __init__(self):
        pass

    def get_configmap(self, name, namespace):
        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_secret_for_all_namespaces
        try:
            start_time = int(time.time() * 1000)
            response = self.api.read_namespaced_config_map(
                name=name,
                namespace=namespace
            )
            self.log.k8s(
                'get',
                'read_namespaced_config_map:%s:%s' % (namespace, name),
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_configmap.get_configmap', traceback.format_exc())
            self.log.k8s(
                'get',
                'read_namespaced_config_map:%s:%s' % (namespace, name),
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        return response
