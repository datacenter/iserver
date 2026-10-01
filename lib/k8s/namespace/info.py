class K8sNamespaceInfo():
    def __init__(self):
        self.namespace = None

    def get_namespace_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(
            managed_object
        )

        info['udn'] = self.is_namespace_udn_enabled(managed_object=managed_object)
        if info['udn']:
            info['udnTick'] = '\u2713'
            info['__Output']['udnTick'] = 'Green'

        info['phase'] = self.get(managed_object, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Active':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        info['conditions'] = self.get(managed_object, 'status:conditions', on_error=[], on_none=[])
        info['faults'] = []
        for condition_mo in info['conditions']:
            type_mo = self.get(condition_mo, 'type')
            if type_mo is None:
                continue

            if type_mo.endswith('Failure'):
                if self.get(condition_mo, 'status') == 'True':
                    info['faults'].append(condition_mo)

                continue

            if type_mo.endswith('Remaining'):
                if self.get(condition_mo, 'status') == 'True':
                    info['faults'].append(condition_mo)

                continue

            info['faults'].append(condition_mo)

        return info

    def add_namespaces_resource_info(self, infos, res_info, threshold=3, cache_enabled=True):
        if not res_info:
            return infos
        
        if not cache_enabled and len(infos) <= threshold:
            pass
        else:
            self.get_pods(cache_enabled=False)

        for info in infos:
            info['pod'] = len(self.get_pods(namespace=info['name'], cache_enabled=True))

        return infos
            
    def get_namespaces(self, res_info=False, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'namespace', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if infos is None:
            return None
        
        infos = self.add_namespaces_resource_info(infos, res_info)
        return infos

    def is_namespace(self, name, cache_enabled=True, optimized=True):
        if self.get_namespace(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_namespace(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'namespace', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_namespace_label(self, namespace, label_key, label_value=None, cache_enabled=True):
        namespace_mo = self.get_namespace(namespace, cache_enabled=cache_enabled, return_mo=True)
        if namespace_mo is None:
            return False

        labels = self.get(namespace_mo, 'metadata:labels')
        if labels is None:
            return False

        for label in labels:
            if label == label_key:
                if label_value is None:
                    return True

                if labels[label] == label_value:
                    return True

        return False

    def is_namespace_annotation(self, namespace, annotation_key, annotation_value=None, cache_enabled=True):
        namespace_mo = self.get_namespace(namespace, cache_enabled=cache_enabled, return_mo=True)
        if namespace_mo is None:
            return False

        annotations = self.get(namespace_mo, 'metadata:annotations')
        if annotations is None:
            return False

        for annotation in annotations:
            if annotation == annotation_key:
                if annotation_value is None:
                    return True

                if annotations[annotation] == annotation_value:
                    return True

        return False