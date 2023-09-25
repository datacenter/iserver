import time
import traceback


class K8sServiceApi():
    def __init__(self):
        self.service_mo = None

    def get_service_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.service_mo is not None:
                return self.service_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_service_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'service',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_service_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'service',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.service_mo = []
        for item in response.items:
            service = self.convert_object(item.to_dict())
            self.service_mo.append(
                service
            )

        self.log.k8s_mo(
            'service',
            self.service_mo
        )

        return self.service_mo

    def create_namespaced_service(self, service_definition):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        namespace = service_definition['metadata']['namespace']
        try:
            api_response = api_handler.create_namespaced_service(
                namespace,
                service_definition
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.create_namespaced_service',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'create',
                'service',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'create',
            'service',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def delete_namespaced_service(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)
        try:
            api_response = api_handler.delete_namespaced_service(
                name,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.delete_namespaced_service',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'delete',
                'service',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'delete',
            'service',
            True,
            int(time.time() * 1000) - start_time
        )

        return True
