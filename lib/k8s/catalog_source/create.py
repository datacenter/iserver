class K8sCatalogSourceCreate():
    def __init__(self):
        pass

    def get_catalog_source_body(self, namespace, name, source, image):
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1alpha1'
        body['kind'] = 'CatalogSource'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['sourceType'] = source
        body['spec']['image'] = image
        return body
    
    def create_catalog_source(self, namespace, name, image, source='grpc', confirmation=False, my_output=None, wait=True):
        body = self.get_catalog_source_body(
            namespace,
            name,
            source,
            image
        )
        success = self.create_resource_and_wait(
            body, 
            'catalog_source', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        return success