import time
import traceback


class K8sServiceApi():
    def __init__(self):
        self.services = None

    def get_service(self, namespace, name, cache=True):
        services = self.get_services(cache=cache)
        if services is None:
            return None

        for service in services:
            if service['metadata']['namespace'] == namespace and service['metadata']['name'] == name:
                return service

        return None

    def get_services(self, cache=True):
        if not self.connect():
            return None

        if self.services is not None and cache:
            return self.services

        try:
            start_time = int(time.time() * 1000)
            response = self.api.list_service_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'services',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_services', traceback.format_exc())
            self.log.k8s(
                'get',
                'services',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.services = []
        for item in response.items:
            service = self.convert_object(item.to_dict())
            self.services.append(
                service
            )

        self.log.k8s_mo(
            'service',
            self.services
        )

        return self.services

    def create_namespaced_service(self, service_definition):
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        namespace = service_definition['metadata']['namespace']
        try:
            api_response = self.api.create_namespaced_service(
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
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)
        try:
            api_response = self.api.delete_namespaced_service(
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
