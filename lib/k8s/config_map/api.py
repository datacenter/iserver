import time
import traceback
from kubernetes import client


class K8sConfigMapApi():
    def __init__(self):
        self.config_map_mo = None

    def get_config_map_namespace_name_mo(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            api_response = api_handler.read_namespaced_config_map(name, namespace)
            response = self.convert_object(api_response.to_dict())
            self.log.k8s(
                'get',
                'config_map_%s_%s' % (namespace, name),
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            return None
        
        return response

    def get_config_map_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.config_map_mo is not None:
                return self.config_map_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_config_map_for_all_namespaces
        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_config_map_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'config_map',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_config_map_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'config_map',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.config_map_mo = []
        for item in response.items:
            config_map_mo = self.convert_object(item.to_dict())
            self.config_map_mo.append(
                config_map_mo
            )

        self.log.k8s_mo(
            'config_map',
            self.config_map_mo
        )

        return self.config_map_mo

    def create_config_map_data_mo(self, namespace, name, destination, content, labels=None):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        if labels is None or len(labels) == 0:
            metadata = client.V1ObjectMeta(
                name=name,
                namespace=namespace
            )
        else:
            metadata = client.V1ObjectMeta(
                labels=labels,
                name=name,
                namespace=namespace
            )

        data = {}
        data[destination] = content

        body = client.V1ConfigMap(
            api_version='v1',
            kind='ConfigMap',
            data=data,
            metadata=metadata
        )

        try:
            api_response = api_handler.create_namespaced_config_map(
                namespace,
                body
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.create_config_map_data_mo',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'create',
                'configmap',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'create',
            'configmap',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def set_config_map_mo(self, config_map_mo):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        namespace = config_map_mo['metadata']['namespace']
        name = config_map_mo['metadata']['name']
        if 'labels' not in config_map_mo['metadata']:
            metadata = client.V1ObjectMeta(
                name=name,
                namespace=namespace
            )
        else:
            metadata = client.V1ObjectMeta(
                labels=config_map_mo['metadata']['labels'],
                name=name,
                namespace=namespace
            )

        data = config_map_mo['data']

        body = client.V1ConfigMap(
            api_version='v1',
            kind='ConfigMap',
            data=data,
            metadata=metadata
        )

        try:
            api_response = api_handler.patch_namespaced_config_map(
                name,
                namespace,
                body
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.set_config_map_mo',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'set',
                'configmap',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'set',
            'configmap',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def delete_config_map_mo(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            api_response = api_handler.delete_namespaced_config_map(
                name,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.delete_config_map_mo',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'delete',
                'configmap',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'delete',
            'configmap',
            True,
            int(time.time() * 1000) - start_time
        )

        return True
