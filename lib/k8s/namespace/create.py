class K8sNamespaceCreate():
    def __init__(self):
        pass
    
    def get_namespace_body(self, name, labels=None, annotations=None):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Namespace'
        body['metadata'] = {}
        body['metadata']['name'] = name
        if labels is not None:
            body['metadata']['labels'] = {}
            for key in labels:
                body['metadata']['labels'][key] = labels[key]

        if annotations is not None:
            body['metadata']['annotations'] = {}
            for key in annotations:
                body['metadata']['annotations'][key] = annotations[key]

        return body

    def create_namespace(
            self,
            name,
            labels=None,
            annotations=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if labels is not None and len(labels) == 0:
            labels = None
            
        if annotations is not None and len(annotations) == 0:
            annotations = None

        body = self.get_namespace_body(
            name,
            labels=labels,
            annotations=annotations
        )

        success = self.create_resource(body, object_name='namespace', my_output=my_output, confirmation=confirmation)
        if not success:
            return False

        if wait:
            if my_output is not None:
                my_output.default('Wait for namespace [timeout:60]...')

            if not self.wait_namespace(name, max_time=60):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        if labels is not None:
            if my_output is not None:
                my_output.default('Check labels', before_newline=True)

            for key in labels:
                if self.is_namespace_label(name, key, label_value=labels[key], cache_enabled=False):
                    if my_output is not None:
                        my_output.default('- %s:%s found' % (key, labels[key]))

                    continue

                if my_output is not None:
                    my_output.default('- %s:%s not found' % (key, labels[key]))

                if not self.add_namespace_label(name, key, labels[key]):
                    if my_output is not None:
                        my_output.error('REST API failed')
                    return False

                if my_output is not None:
                    my_output.default('- %s:%s %s' % (key, labels[key], my_output.add_color('added', 'Green')))

        if annotations is not None:
            if my_output is not None:
                my_output.default('Check annotations', before_newline=True)
                
            for key in annotations:
                if self.is_namespace_annotation(name, key, annotation_value=annotations[key], cache_enabled=False):
                    if my_output is not None:
                        my_output.default('- %s:%s found' % (key, annotations[key]))

                    continue

                if my_output is not None:
                    my_output.default('- %s:%s not found' % (key, annotations[key]))

                if not self.add_namespace_annotation(name, key, annotations[key]):
                    if my_output is not None:
                        my_output.error('REST API failed')
                    return False

                if my_output is not None:
                    my_output.default('- %s:%s %s' % (key, annotations[key], my_output.add_color('added', 'Green')))

        return True        
