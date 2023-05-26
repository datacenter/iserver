import time
import traceback


class K8sNamespaceApi():
    def __init__(self):
        self.namespaces = None

    def get_namespaces(self, cache=True):
        if not self.connect():
            return False

        if self.namespaces is not None and cache:
            return True

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1NodeList.md
        try:
            start_time = int(time.time() * 1000)
            response = self.api.list_namespace(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'namespaces',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_namespaces.get_namespaces', traceback.format_exc())
            self.log.k8s(
                'get',
                'namespaces',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.namespaces = []
        for item in response.items:
            namespace = self.convert_namespace(item)
            if namespace is not None:
                self.namespaces.append(namespace)

        return True
