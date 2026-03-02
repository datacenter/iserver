import traceback


class K8sNodeApi():
    def __init__(self):
        self.node_mo = None

    def get_node_mo(self, name=None, cache_enabled=True, fast=False):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.node_mo
        )
        if cache_hit:
            return response

        response, self.node_mo = self.get_resources(
            'Node', 
            'v1', 
            self.node_mo,
            name=name,
            fast=fast
        )

        return response
    
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
