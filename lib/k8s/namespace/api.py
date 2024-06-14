import time
import traceback


class K8sNamespaceApi():
    def __init__(self):
        self.namespace_mo = None

    def get_namespace_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.namespace_mo is not None:
                return self.namespace_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_namespace(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'namespace',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_namespace_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'namespace',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.namespace_mo = []
        for item in response.items:
            namespace_mo = self.convert_object(item.to_dict())
            self.namespace_mo.append(
                namespace_mo
            )

        self.log.k8s_mo(
            'namespace',
            self.namespace_mo
        )

        return self.namespace_mo
