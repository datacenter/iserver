import time
import json
import traceback
from kubernetes.stream import stream
from kubernetes import client


class K8sPodApi():
    def __init__(self):
        self.pod_mo = None
        self.pod_namespace_mo = {}
        self.pod_log_mo = {}

    def get_pod_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.pod_mo,
            self.pod_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.pod_mo, self.pod_namespace_mo = self.get_namespaced_resources(
            'Pod', 
            'v1', 
            self.pod_mo,
            self.pod_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def get_pod_log_mo(self, namespace, name, container=None, cache_enabled=True):
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
            if container is None:
                response = api_handler.read_namespaced_pod_log(
                    name,
                    namespace
                )
            else:
                response = api_handler.read_namespaced_pod_log(
                    name,
                    namespace,
                    container=container
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

    def delete_pod_mo(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)
        try:
            api_response = api_handler.delete_namespaced_pod(
                name,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.delete_namespaced_pod',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'delete',
                'pod',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'delete',
            'pod',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def get_pod_exec(self, namespace, name, command, container=None):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        output = None

        if isinstance(command, str):
            if container is None:
                try:
                    output = stream(
                        api_handler.connect_get_namespaced_pod_exec,
                        name,
                        namespace,
                        command=command.split(' '),
                        stderr=True,
                        stdin=False,
                        stdout=True,
                        tty=False
                    )
                except BaseException:
                    self.log.error('get_pod_exec', traceback.format_exc())
                    self.log.error('get_pod_exec', command)
            else:
                try:
                    output = stream(
                        api_handler.connect_get_namespaced_pod_exec,
                        name,
                        namespace,
                        container=container,
                        command=command.split(' '),
                        stderr=True,
                        stdin=False,
                        stdout=True,
                        tty=False
                    )
                except BaseException:
                    self.log.error('get_pod_exec', traceback.format_exc())
                    self.log.error('get_pod_exec', command)

        if isinstance(command, list):
            if container is None:
                try:
                    output = stream(
                        api_handler.connect_get_namespaced_pod_exec,
                        name,
                        namespace,
                        command=command,
                        stderr=True,
                        stdin=False,
                        stdout=True,
                        tty=False
                    )
                except BaseException:
                    self.log.error('get_pod_exec', traceback.format_exc())
                    self.log.error('get_pod_exec', ' '.join(command))
            else:
                try:
                    output = stream(
                        api_handler.connect_get_namespaced_pod_exec,
                        name,
                        namespace,
                        container=container,
                        command=command,
                        stderr=True,
                        stdin=False,
                        stdout=True,
                        tty=False
                    )
                except BaseException:
                    self.log.error('get_pod_exec', traceback.format_exc())
                    self.log.error('get_pod_exec', ' '.join(command))

        return output

    def evict_pod_mo(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            body = client.V1Eviction(metadata=client.V1ObjectMeta(name=name, namespace=namespace))
            response = api_handler.create_pod_mo_eviction(name, namespace, body)
        except BaseException:
            self.log.error(
                'k8s.evict_pod_mo',
                traceback.format_exc()
            )
            return False
    
        return True