class K8sNodeAnnotation():
    def __init__(self):
        pass

    def add_node_annotation(self, node_name, key, value, my_output=None, confirmation=False):
        node = self.get_node(node_name, cache_enabled=False)
        if node is None:
            return False
        
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Node'
        body['metadata'] = {}
        body['metadata']['name'] = node_name
        body['metadata']['annotations'] = {}
        body['metadata']['annotations'][key] = value

        return self.patch_resource(body, object_name='node', my_output=my_output, confirmation=confirmation)

    def delete_node_annotation(self, node_name, key, my_output=None, confirmation=False):
        return self.add_node_annotation(node_name, key, None, my_output=my_output, confirmation=confirmation)
        
    def add_node_label(self, node_name, key, value, my_output=None, confirmation=False):
        node = self.get_node(node_name, cache_enabled=False)
        if node is None:
            return False
        
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Node'
        body['metadata'] = {}
        body['metadata']['name'] = node_name
        body['metadata']['labels'] = {}
        body['metadata']['labels'][key] = value

        return self.patch_resource(body, object_name='node', my_output=my_output, confirmation=confirmation)

    def delete_node_label(self, node_name, key, my_output=None, confirmation=False):
        return self.add_node_label(node_name, key, None, my_output=my_output, confirmation=confirmation)