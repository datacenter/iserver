import time
import traceback
import kubernetes.client


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

    def create_namespace_mo(self, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            body = kubernetes.client.V1Namespace(metadata=kubernetes.client.V1ObjectMeta(name=name))
            api_response = api_handler.create_namespace(
                body
            )

        except BaseException:
            api_response = None
            self.log.error(
                'k8s.create_namespace',
                'Namespace create failed: %s' % (name)
            )
            self.log.error(
                'k8s.create_namespace',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'create',
                'namespace',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'create',
            'namespace',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def create_namespace_mo_from_body(self, body):
        success = self.create_namespace_mo(body['metadata']['name'])
        if not success:
            return False
        
        success = self.set_namespace_mo(body)
        if not success:
            return False
        
        return True

    def set_namespace_mo(self, body):
        api_handler = self.get_api()
        if api_handler is None:
            return False

        try:
            response = api_handler.patch_namespace(
                body['metadata']['name'],
                body
            )

        except BaseException:
            self.log.error('set_namespace_mo', traceback.format_exc())
            return False

        return True

    def add_namespace_label(self, namespace, key, value):
        api_handler = self.get_api()
        if api_handler is None:
            return False

        try:
            labels = {
                'metadata': {
                    'labels': {
                        key:value
                    }
                }
            }

            response = api_handler.patch_namespace(
                namespace,
                labels
            )

        except BaseException:
            self.log.error('k8s_nodes.add_namespace_label', traceback.format_exc())
            return False

        return True
    
    def delete_namespace_label(self, namespace, key):
        api_handler = self.get_api()
        if api_handler is None:
            return False

        try:
            labels = {
                'metadata': {
                    'labels': {
                        key:None
                    }
                }
            }

            response = api_handler.patch_namespace(
                namespace,
                labels
            )

        except BaseException:
            self.log.error('k8s_nodes.add_namespace_label', traceback.format_exc())
            return False

        return True
    
    def delete_namespace_mo(self, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            api_response = api_handler.delete_namespace(
                name
            )

        except BaseException:
            api_response = None
            self.log.error(
                'k8s.delete_namespace',
                'Namespace delete failed: %s' % (name)
            )
            self.log.error(
                'k8s.delete_namespace',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'delete',
                'namespace',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'delete',
            'namespace',
            True,
            int(time.time() * 1000) - start_time
        )

        return True
