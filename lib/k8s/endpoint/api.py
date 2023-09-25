import time
import traceback


class K8sEndpointApi():
    def __init__(self):
        self.endpoint_mo = None

    def get_endpoint_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.endpoint_mo is not None:
                return self.endpoint_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_endpoints_for_all_namespaces
        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_endpoints_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'endpoint',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_endpoints.get_endpoints', traceback.format_exc())
            self.log.k8s(
                'get',
                'endpoint',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.endpoint_mo = []
        for item in response.items:
            endpoint_mo = self.convert_object(item.to_dict())
            self.endpoint_mo.append(
                endpoint_mo
            )

        self.log.k8s_mo(
            'endpoint',
            self.endpoint_mo
        )

        return self.endpoint_mo
