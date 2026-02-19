import time
import traceback


class K8sNodeApi():
    def __init__(self):
        self.node_mo = None

    def get_node_mo(self, cache_enabled=True, fast=False):
        if cache_enabled:
            if self.node_mo is not None:
                return self.node_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1NodeList.md
        try:
            start_time = int(time.time() * 1000)
            if fast:
                response = api_handler.list_node(
                    timeout_seconds=1
                )
            else:
                response = api_handler.list_node(
                    timeout_seconds=self.api_timeout_seconds
                )
            self.log.k8s(
                'get',
                'node',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_nodes.get_nodes', traceback.format_exc())
            self.log.k8s(
                'get',
                'node',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.node_mo = []
        for item in response.items:
            node_mo = self.convert_object(item.to_dict())
            self.node_mo.append(
                node_mo
            )

        self.log.k8s_mo(
            'node',
            self.node_mo
        )

        return self.node_mo

    def add_node_annotation(self, node_name, key, value):
        api_handler = self.get_api()
        if api_handler is None:
            return False

        try:
            annotations = {
                'metadata': {
                    'annotations': {
                        key:value
                    }
                }
            }

            response = api_handler.patch_node(
                node_name,
                annotations
            )

        except BaseException:
            self.log.error('k8s_nodes.add_node_annotation', traceback.format_exc())
            return False

        return True
    
    def add_node_label(self, node_name, key, value):
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

            response = api_handler.patch_node(
                node_name,
                labels
            )

        except BaseException:
            self.log.error('k8s_nodes.add_node_label', traceback.format_exc())
            return False

        return True
    
    def delete_node_label(self, node_name, key):
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

            response = api_handler.patch_node(
                node_name,
                labels
            )

        except BaseException:
            self.log.error('k8s_nodes.add_node_label', traceback.format_exc())
            return False

        return True

    
    def delete_node_annotation(self, node_name, key):
        api_handler = self.get_api()
        if api_handler is None:
            return False

        try:
            annotations = {
                'metadata': {
                    'annotations': {
                        key:None
                    }
                }
            }

            response = api_handler.patch_node(
                node_name,
                annotations
            )

        except BaseException:
            self.log.error('k8s_nodes.delete_node_annotation', traceback.format_exc())
            return False

        return True
    
    def patch_node_mo(self, node_name, body):
        api_handler = self.get_api()
        if api_handler is None:
            return False

        try:
            response = api_handler.patch_node(
                node_name,
                body
            )

        except BaseException:
            self.log.error('k8s_nodes.patch_node_mo', traceback.format_exc())
            return False

        return True
