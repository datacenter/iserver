import time
import traceback
from kubernetes import client


class K8sSecretApi():
    def __init__(self):
        self.secret_mo = None

    def get_secret_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.secret_mo is not None:
                return self.secret_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_secret_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'secret',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_secret_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'secret',
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        self.secret_mo = []
        for item in response.items:
            secret_mo = self.convert_object(item.to_dict())
            self.secret_mo.append(
                secret_mo
            )

        self.log.k8s_mo(
            'secret',
            self.secret_mo
        )

        return self.secret_mo

    def create_secret_mo(self, namespace, secret_definition):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            api_response = api_handler.create_namespaced_secret(
                namespace,
                secret_definition
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.create_namespaced_secret',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'create',
                'secret',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'create',
            'secret',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def update_secret_mo(self, namespace, name, secret_definition):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            api_response = api_handler.patch_namespaced_secret(
                name,
                namespace,
                secret_definition
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.update_namespaced_secret',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'update',
                'secret',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'update',
            'secret',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def create_secret_kv_mo(self, namespace, name, kv, labels=None, secret_type='Opaque'):
        body = client.V1Secret()
        if labels is None or len(labels) == 0:
            body.metadata = client.V1ObjectMeta(name=name, namespace=namespace)
        else:
            body.metadata = client.V1ObjectMeta(name=name, namespace=namespace, labels=labels)
        body.data = kv
        body.type = secret_type
        return self.create_secret_mo(namespace, body)

    def update_secret_kv_mo(self, namespace, name, kv):
        body = client.V1Secret()
        body.metadata = client.V1ObjectMeta(name=name, namespace=namespace)
        body.data = kv
        body.type = 'Opaque'
        return self.update_secret_mo(namespace, name, body)

    def delete_secret_mo(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)
        try:
            api_response = api_handler.delete_namespaced_secret(
                name,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.delete_namespaced_secret',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'delete',
                'secret',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'delete',
            'secret',
            True,
            int(time.time() * 1000) - start_time
        )

        return True
