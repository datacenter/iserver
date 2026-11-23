import time
import traceback
import kubernetes.client


class K8sNamespaceAnnotation():
    def __init__(self):
        self.namespace_mo = None

    def add_namespace_annotation(self, namespace, key, value, my_output=None, confirmation=False):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Namespace'
        body['metadata'] = {}
        body['metadata']['name'] = namespace
        body['metadata']['annotations'] = {}
        body['metadata']['annotations'][key] = value

        return self.patch_resource(body, object_name='namespace', my_output=my_output, confirmation=confirmation)
        
    def delete_namespace_annotation(self, namespace_name, key, my_output=None, confirmation=False):
        return self.add_namespace_annotation(namespace_name, key, None, my_output=my_output, confirmation=confirmation)
    
    def add_namespace_label(self, namespace, key, value, my_output=None, confirmation=False):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Namespace'
        body['metadata'] = {}
        body['metadata']['name'] = namespace
        body['metadata']['labels'] = {}
        body['metadata']['labels'][key] = value

        return self.patch_resource(body, object_name='namespace', my_output=my_output, confirmation=confirmation)
        
    def delete_namespace_label(self, namespace_name, key, my_output=None, confirmation=False):
        return self.add_namespace_label(namespace_name, key, None, my_output=my_output, confirmation=confirmation)