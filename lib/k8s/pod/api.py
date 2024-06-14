import time
import traceback


class K8sPodApi():
    def __init__(self):
        self.pod_mo = None
        self.pod_log_mo = {}

    def get_pod_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pod_mo is not None:
                return self.pod_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_pod_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'pod',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pod_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'pod',
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pod_mo = []
        for item in response.items:
            pod_mo = self.convert_object(item.to_dict())
            self.pod_mo.append(
                pod_mo
            )

        self.log.k8s_mo(
            'pod',
            self.pod_mo
        )

        return self.pod_mo

    def get_pod_log_mo(self, namespace, name, cache_enabled=True):
        key = '%s.%s' % (namespace, name)
        if cache_enabled:
            if key in self.pod_log_mo:
                return self.pod_log_mo[key]

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#read_namespaced_pod_log
            start_time = int(time.time() * 1000)
            response = api_handler.read_namespaced_pod_log(
                name,
                namespace
            )
            self.log.k8s(
                'get',
                'pod_log',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pod_log_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'pod_log',
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pod_log_mo[key] = response

        return self.pod_log_mo[key]
